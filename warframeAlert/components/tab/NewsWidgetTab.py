# coding=utf-8
from PyQt6 import QtWidgets, QtCore, QtGui

from warframeAlert.components.common.CommonImageButton import CommonImageButton
from warframeAlert.components.common.GlobalUpgrade import GlobalUpgrade
from warframeAlert.constants.warframeTypes import GlobalUpgrades, Events
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils, commonUtils
from warframeAlert.utils.commonUtils import remove_widget, bool_to_yes_no, get_last_item_with_backslash
from warframeAlert.utils.fileUtils import get_separator, get_cur_dir
from warframeAlert.utils.gameTranslationUtils import get_node, get_upgrade_type
from warframeAlert.utils.logUtils import LogHandler
from warframeAlert.utils.stringUtils import divide_message
from warframeAlert.utils.warframeUtils import get_operation_type


def get_news_type(message: str, url: str) -> int:
    url = url.lower().replace("\n", "")
    if (url == ""):  # No URL available
        return 2
    elif ("www.youtube.com" in url):  # YouTube
        return 2
    elif ("prime" in url and "access" in url):  # Prime Access
        return 1
    elif ("tennocon" in url):  # Tennocon
        return 1
    elif ("contest" in url or "contest" in message):  # Contest
        return 2
    elif ("forums.warframe.com" in url):  # Hotfix and in Game Events
        return 1
    elif ("update" in url):
        return 1
    else:
        return 2


class NewsWidgetTab():
    def __init__(self) -> None:
        self.NewsWidgetTab = QtWidgets.QWidget()
        self.alerts = {'Events': {}, 'GlobalUpgrades': []}
        self.alerts['Events']['News'] = []
        self.alerts['Events']['Contest'] = []
        self.DEFAULT_IMAGE_PATH = "assets" + get_separator() + "image" + get_separator() + "default_news_image.jpg"

        self.NewsWidget = QtWidgets.QWidget()
        self.ContestWidget = QtWidgets.QWidget()

        self.NewsTabber = QtWidgets.QTabWidget()

        self.grid = QtWidgets.QGridLayout(self.NewsWidget)
        self.gridC = QtWidgets.QGridLayout(self.ContestWidget)

        self.NewsScrollBar = QtWidgets.QScrollArea()
        self.NewsScrollBarC = QtWidgets.QScrollArea()

        self.NewsScrollBar.setWidgetResizable(True)
        self.NewsScrollBarC.setWidgetResizable(True)

        self.NewsScrollBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.NewsScrollBarC.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.NewsScrollBar.setBackgroundRole(QtGui.QPalette.ColorRole.NoRole)
        self.NewsScrollBarC.setBackgroundRole(QtGui.QPalette.ColorRole.NoRole)

        self.NewsWidget.setLayout(self.grid)
        self.ContestWidget.setLayout(self.gridC)

        self.NewsScrollBar.setWidget(self.NewsWidget)
        self.NewsScrollBarC.setWidget(self.ContestWidget)

        self.NewsTabber.insertTab(0, self.NewsScrollBar, translate("newsWidgetTab", "newsLabel"))
        self.NewsTabber.insertTab(1, self.NewsScrollBarC, translate("newsWidgetTab", "communityLabel"))

        self.NewsLabel = QtWidgets.QLabel("")

        self.NoNewsLabel = QtWidgets.QLabel(translate("newsWidgetTab", "noNews"))
        self.NoNewsOtherLabel = QtWidgets.QLabel(translate("newsWidgetTab", "noContest"))

        self.NoNewsLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NoNewsOtherLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.grid.addWidget(self.NoNewsLabel, 0, 0)
        self.gridC.addWidget(self.NoNewsOtherLabel, 0, 0)

        self.GlobalUpgrade = QtWidgets.QLabel("")
        self.GlobalUpgrade.hide()

        self.gridNews = QtWidgets.QGridLayout(self.NewsWidgetTab)
        self.gridNews.addWidget(self.GlobalUpgrade, 0, 0, 1, 3)
        self.gridNews.addWidget(self.NewsLabel, 1, 0, 1, 3)
        self.gridNews.addWidget(self.NewsTabber, 2, 0, 1, 3)
        self.gridNews.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.NewsWidgetTab.setLayout(self.gridNews)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.NewsWidgetTab

    def update_news(self, data: Events) -> None:
        try:
            self.parse_news(data)
        except Exception as er:
            LogHandler.err(translate("newsWidgetTab", "newsError") + ": " + str(er))
            commonUtils.print_traceback(translate("newsWidgetTab", "newsError") + ": " + str(er))
            self.reset_news()

    def parse_news(self, data: Events) -> None:
        n_news = len(self.alerts['Events']['News'])
        n_contest = len(self.alerts['Events']['Contest'])
        for news in data:
            text = ""
            news_id = news['_id']['$oid']
            forum_url = news['Prop']
            community = news['Community'] if ('Community' in news) else None
            message_it = message_en = 0
            for i in range(0, len(news['Messages'])):
                if ('it' == news['Messages'][i]['LanguageCode']):
                    message_it = divide_message(news['Messages'][i]['Message'])
                    break
                elif ('en' == news['Messages'][i]['LanguageCode']):
                    message_en = divide_message(news['Messages'][i]['Message'])
            if (message_it):
                message = message_it
            elif (message_en):
                message = message_en
            else:
                continue

            if (forum_url == "" and 'Links' in news):
                link_it = link_en = ""
                for i in range(0, len(news['Links'])):
                    if ('it' == news['Links'][i]['LanguageCode']):
                        link_it = divide_message(news['Links'][i]['Link'])
                        break
                    elif ('en' == news['Links'][i]['LanguageCode']):
                        link_en = divide_message(news['Links'][i]['Link'])
                if (link_it):
                    forum_url = link_it
                elif (link_en):
                    forum_url = link_en
                else:
                    continue
            news_type = 2 if (community is not None and community) else get_news_type(message, forum_url)

            found = 0
            if (news_type == 1):
                for old_news in self.alerts['Events']['News']:
                    if (old_news.get_news_id() == news_id):
                        found = 1
                        old_news.update_image_news_button()

            elif (news_type == 2):
                for old_news in self.alerts['Events']['Contest']:
                    if (old_news.get_news_id() == news_id):
                        found = 1
                        old_news.update_image_news_button()

            if (found == 0):
                try:
                    date = timeUtils.get_time(news['Date']['$date']['$numberLong'])
                except KeyError:
                    date = "???"
                text += translate("newsWidgetTab", "newsInit") + " " + date + "\n"

                if ('ImageUrl' in news):
                    url = news['ImageUrl'].replace(" ", "")
                    if ("?" in url):
                        for i in range(0, len(url)):
                            if (url[i] == "?"):
                                url = url[:i]
                                break
                else:
                    url = get_cur_dir() + get_separator() + self.DEFAULT_IMAGE_PATH
                if ('EventStartDate' in news):
                    try:
                        date = timeUtils.get_time(news['EventStartDate']['$date']['$numberLong'])
                    except KeyError:
                        date = "???"
                    text += translate("newsWidgetTab", "eventInit") + " " + date + "\n"
                if ('EventEndDate' in news):
                    try:
                        date = timeUtils.get_time(news['EventEndDate']['$date']['$numberLong'])
                    except KeyError:
                        date = "???"
                    text += translate("newsWidgetTab", "eventEnd") + " " + date + "\n"
                if ('EventLiveUrl' in news):
                    text += translate("newsWidgetTab", "newsSite") + ": " + news['EventLiveUrl']
                priority = bool_to_yes_no(news['Priority'])
                mobile = bool_to_yes_no(news['MobileOnly'])
                text += translate("newsWidgetTab", "priority") + ": " + priority + "\n"
                text += translate("newsWidgetTab", "onlyMobile") + ": " + mobile

                temp = CommonImageButton(news_id)

                temp.set_text_news_button(message)
                temp.set_news_url(forum_url)
                temp.set_tooltip(text)
                image = get_last_item_with_backslash(url)
                temp.set_image_news(image, url)

                if (news_type == 1):
                    self.alerts['Events']['News'].append(temp)
                elif (news_type == 2):
                    self.alerts['Events']['Contest'].append(temp)

                del temp

        self.add_news(n_news, n_contest)
        self.reset_news()

    def update_news_info(self, build_label: str, game_time: int) -> None:
        translated_time = timeUtils.get_time(str(game_time * 1000))
        if (OptionsHandler.get_option("Update/Console") == 0):
            console = "PC"
        elif (OptionsHandler.get_option("Update/Console") == 1):
            console = "PS4"
        elif (OptionsHandler.get_option("Update/Console") == 2):
            console = "Xbox One"
        elif (OptionsHandler.get_option("Update/Console") == 3):
            console = "Nintendo Switch"
        else:
            console = "PC"

        news_text = translate("newsWidgetTab", "version") + " " + console + "\t"
        news_text += translate("newsWidgetTab", "build") + ": " + build_label + "\t"
        news_text += translate("newsWidgetTab", "time") + ": " + translated_time
        self.NewsLabel.setText(news_text)

    def add_news(self, n_news: int, n_contest: int) -> None:
        for i in range(n_news, len(self.alerts['Events']['News'])):
            self.grid.addLayout(self.alerts['Events']['News'][i].NewsBox, 1 + int(n_news / 2), n_news % 2)
            self.alerts['Events']['News'][i].show()
            NotificationService.send_notification(
                translate("newsWidgetTab", "newNews!"),
                self.alerts['Events']['News'][i].get_title(),
                None)
            n_news += 1
        for i in range(n_contest, len(self.alerts['Events']['Contest'])):
            self.gridC.addLayout(self.alerts['Events']['Contest'][i].NewsBox, 1 + int(n_contest / 2), n_contest % 2)
            self.alerts['Events']['Contest'][i].show()
            NotificationService.send_notification(
                translate("newsWidgetTab", "newNews!"),
                self.alerts['Events']['Contest'][i].get_title(),
                None)
            n_contest += 1

    def update_global_upgrades(self, data: GlobalUpgrades) -> None:
        try:
            self.parse_global_upgrade(data)
        except Exception as er:
            LogHandler.err(translate("newsWidgetTab", "globalUpgradeError") + ": " + str(er))
            commonUtils.print_traceback(translate("newsWidgetTab", "globalUpgradeError") + ": " + str(er))
            self.reset_global_upgrades()

    def parse_global_upgrade(self, data: GlobalUpgrades) -> None:
        self.reset_global_upgrades()
        if (data):
            n_upgrade = len(self.alerts['GlobalUpgrades'])
            for upgrade in data:
                init = timeUtils.get_time(upgrade['Activation']['$date']['$numberLong'])
                end = upgrade['ExpiryDate']['$date']['$numberLong']
                upgrade_id = upgrade['_id']['$oid']

                remaining_time = int(end[:10]) - int(timeUtils.get_local_time())
                if (remaining_time > 0):
                    found = 0

                    for upgrades in self.alerts['GlobalUpgrades']:
                        if (upgrades.get_id() == upgrade_id):
                            found = 1

                    if (found == 0):
                        upgrade_type = upgrade['UpgradeType']
                        operation = get_operation_type(upgrade['OperationType'])
                        value = upgrade['Value']
                        if ('LocalizeTag' in upgrade):
                            tag = get_last_item_with_backslash(upgrade['LocalizeTag'])
                        else:
                            tag = ""
                        if ('LocalizeDescTag' in upgrade):
                            desc = get_last_item_with_backslash(upgrade['LocalizeDescTag'])
                        else:
                            desc = ""
                        if ('Nodes' in upgrade):
                            node = []
                            for nodes in upgrade['Nodes']:
                                node.append(get_node(nodes))
                        else:
                            node = []
                        if ('ValidType' in upgrade):
                            valid_type = get_upgrade_type(upgrade['ValidType'])
                        else:
                            valid_type = ""
                        temp = GlobalUpgrade(upgrade_id)
                        temp.set_upgrade_data(init, end, upgrade_type, operation, value, node)
                        temp.set_other_data(tag, desc, valid_type)

                        self.alerts['GlobalUpgrades'].append(temp)
                        del temp

            self.add_global_upgrades(n_upgrade)

    def add_global_upgrades(self, n_upgrade: int) -> None:
        for i in range(n_upgrade, len(self.alerts['GlobalUpgrades'])):
            if (not self.alerts['GlobalUpgrades'][i].is_expired()):
                self.GlobalUpgrade.show()
                self.gridNews.addLayout(self.alerts['GlobalUpgrades'][i].UpgradeBox, 0, n_upgrade % 3)
                n_upgrade += 1
                NotificationService.send_notification(
                    translate("newsWidgetTab", "newBooster!"),
                    self.alerts['GlobalUpgrades'][i].to_string(),
                    self.alerts['GlobalUpgrades'][i].get_image())

    def reset_news(self) -> None:
        self.NoNewsLabel.hide()
        self.NoNewsOtherLabel.hide()
        len_n = len(self.alerts['Events']['News'])
        len_no = len(self.alerts['Events']['Contest'])
        if (len_n == 0):
            self.NoNewsLabel.show()
        if (len_no == 0):
            self.NoNewsOtherLabel.show()

    def reset_global_upgrades(self) -> None:
        cancelled = []
        for i in range(0, len(self.alerts['GlobalUpgrades'])):
            if (self.alerts['GlobalUpgrades'][i].is_expired()):
                cancelled.append(i)
        i = len(cancelled)
        while i > 0:
            self.alerts['GlobalUpgrades'][cancelled[i - 1]].hide()
            remove_widget(self.alerts['GlobalUpgrades'][cancelled[i - 1]].UpgradeBox)
            del self.alerts['GlobalUpgrades'][cancelled[i - 1]]
            i -= 1
