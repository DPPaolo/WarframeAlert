# coding=utf-8
from typing import List

from PyQt6 import QtWidgets, QtCore

from warframeAlert.components.common.InGameMarketBox import InGameMarketBox
from warframeAlert.components.common.SalesBox import SalesBox
from warframeAlert.constants.warframeTypes import FlashSales, InGameMarket, InGameMarketLandingPage
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import print_traceback, remove_widget
from warframeAlert.utils.gameTranslationUtils import get_item_name
from warframeAlert.utils.logUtils import LogHandler


class SalesWidgetTab():

    def __init__(self) -> None:
        self.alerts = {'FlashSales': {}, 'InGameMarket': []}
        self.alerts['FlashSales']['Featured']: List[SalesBox] = []  # Featured Items
        self.alerts['FlashSales']['Discount']: List[SalesBox] = []  # Discounted Items

        self.SalesWidget = QtWidgets.QWidget()

        self.FeaturedWidget = QtWidgets.QWidget()
        self.DiscountedWidget = QtWidgets.QWidget()
        self.InGameMarketWidget = QtWidgets.QWidget()

        self.salesTabber = QtWidgets.QTabWidget()

        self.gridFeaturedSales = QtWidgets.QGridLayout(self.FeaturedWidget)
        self.gridDiscountedSales = QtWidgets.QGridLayout(self.DiscountedWidget)
        self.gridInGameItems = QtWidgets.QGridLayout(self.InGameMarketWidget)

        self.FeaturedSalesScrollBar = QtWidgets.QScrollArea()
        self.FeaturedSalesScrollBar.setWidgetResizable(True)
        self.FeaturedSalesScrollBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.DiscountedSalesScrollBar = QtWidgets.QScrollArea()
        self.DiscountedSalesScrollBar.setWidgetResizable(True)
        self.DiscountedSalesScrollBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.InGameItemsScrollBar = QtWidgets.QScrollArea()
        self.InGameItemsScrollBar.setWidgetResizable(True)
        self.InGameItemsScrollBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.FeaturedWidget.setLayout(self.gridFeaturedSales)
        self.DiscountedWidget.setLayout(self.gridDiscountedSales)
        self.InGameMarketWidget.setLayout(self.gridInGameItems)

        self.FeaturedSalesScrollBar.setWidget(self.FeaturedWidget)
        self.DiscountedSalesScrollBar.setWidget(self.DiscountedWidget)
        self.InGameItemsScrollBar.setWidget(self.InGameMarketWidget)

        self.salesTabber.insertTab(0, self.FeaturedSalesScrollBar, translate("salesWidgetTab", "featuredItems"))
        self.salesTabber.insertTab(1, self.DiscountedSalesScrollBar, translate("salesWidgetTab", "discountedItems"))
        self.salesTabber.insertTab(2, self.InGameItemsScrollBar, translate("salesWidgetTab", "inGameItems"))

        self.gridSales = QtWidgets.QGridLayout(self.SalesWidget)
        self.gridSales.addWidget(self.salesTabber, 0, 0)
        self.gridSales.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.SalesWidget.setLayout(self.gridSales)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.SalesWidget

    def update_tab(self) -> None:
        self.salesTabber.insertTab(1, self.DiscountedSalesScrollBar, translate("salesWidgetTab", "discountedItems"))
        if (not (len(self.alerts['FlashSales']['Discount']) > 0)):
            self.salesTabber.removeTab(self.salesTabber.indexOf(self.DiscountedSalesScrollBar))

    def update_sales(self, data: FlashSales) -> None:
        if (OptionsHandler.get_option("Tab/Market") == 1):
            try:
                self.parse_sales(data)
            except Exception as er:
                LogHandler.err(translate("salesWidgetTab", "salesError") + ": " + str(er))
                print_traceback(translate("salesWidgetTab", "salesError") + ": " + str(er))
                self.reset_sales()
                return
        else:
            self.reset_sales()

    def parse_sales(self, data: FlashSales) -> None:
        self.reset_sales()
        n_featured = len(self.alerts['FlashSales']['Featured'])
        n_discount = len(self.alerts['FlashSales']['Discount'])
        for sales in data:
            init = timeUtils.get_time(sales['StartDate']['$date']['$numberLong'])
            end = sales['EndDate']['$date']['$numberLong']
            if ('ProductExpiryOverride' in sales):
                end = sales['ProductExpiryOverride']['$date']['$numberLong']

            timer = int(end[:10]) - int(timeUtils.get_local_time())
            if (timer > 0):
                item = get_item_name(sales['TypeName'], 0)
                found = 0
                for actualSale in self.alerts['FlashSales']['Featured']:
                    if (actualSale.get_item_name() == item):
                        found = 1

                for actualSale in self.alerts['FlashSales']['Discount']:
                    if (actualSale.get_item_name() == item):
                        found = 1

                if (found == 0):
                    if ('ExperimentFeatured' in sales):
                        index = sales['ExperimentFeatured'][0]['FeaturedIndex']
                    elif ('BannerIndex' in sales):  # temporary item
                        index = sales['BannerIndex']
                    else:
                        index = str(timeUtils.get_local_time())
                    bogobuy = sales['BogoBuy']
                    bogoget = sales['BogoGet']
                    discount = sales['Discount']
                    featured = sales['Featured'] if 'Featured' in sales else False
                    popular = sales['Popular'] if 'Popular' in sales else False
                    plat = sales['PremiumOverride']
                    credit = sales['RegularOverride'] if ('RegularOverride' in sales) else 0
                    is_show = sales['ShowInMarket']
                    if ('HideFromMarket' in sales):
                        is_show = is_show and sales['HideFromMarket']
                    support = sales['SupporterPack'] if ('SupporterPack' in sales) else False
                    show_with_recommended = sales['ShowWithRecommended'] if ('ShowWithRecommended' in sales) else False

                    temp = SalesBox(index)
                    temp.set_sales_data(item, credit, plat, discount, end, is_show)
                    temp.set_other_sales_data(bogobuy, bogoget, featured, popular, init, show_with_recommended, support)

                    if (discount > 0):
                        self.alerts['FlashSales']['Discount'].append(temp)
                    else:
                        self.alerts['FlashSales']['Featured'].append(temp)
                    del temp

        self.add_sales(n_featured, n_discount)

    def add_sales(self, n_featured: int, n_discount: int) -> None:
        for i in range(n_featured, len(self.alerts['FlashSales']['Featured'])):
            if (not self.alerts['FlashSales']['Featured'][i].is_expired()):
                self.gridFeaturedSales.addLayout(self.alerts['FlashSales']['Featured'][i].MerBox,
                                                 self.gridFeaturedSales.count(), 0)

        for i in range(n_discount, len(self.alerts['FlashSales']['Discount'])):
            if (not self.alerts['FlashSales']['Discount'][i].is_expired()):
                self.gridDiscountedSales.addLayout(self.alerts['FlashSales']['Discount'][i].MerBox,
                                                   self.gridDiscountedSales.count(), 0)

    def reset_sales(self) -> None:
        cancelled = []
        for i in range(0, len(self.alerts['FlashSales']['Featured'])):
            if (self.alerts['FlashSales']['Featured'][i].is_expired()):
                cancelled.append(i)
        i = len(cancelled)
        while i > 0:
            self.alerts['FlashSales']['Featured'][cancelled[i - 1]].hide()
            remove_widget(self.alerts['FlashSales']['Featured'][cancelled[i - 1]].MerBox)
            del self.alerts['FlashSales']['Featured'][cancelled[i - 1]]
            i -= 1
        cancelled = []
        for i in range(0, len(self.alerts['FlashSales']['Discount'])):
            if (self.alerts['FlashSales']['Discount'][i].is_expired()):
                cancelled.append(i)
        i = len(cancelled)
        while i > 0:
            self.alerts['FlashSales']['Discount'][cancelled[i - 1]].hide()
            remove_widget(self.alerts['FlashSales']['Discount'][cancelled[i - 1]].MerBox)
            del self.alerts['FlashSales']['Discount'][cancelled[i - 1]]
            i -= 1

    def update_in_game_market(self, data: InGameMarket):
        if (OptionsHandler.get_option("Tab/Market") == 1):
            try:
                self.parse_in_game_market(data)
            except Exception as er:
                LogHandler.err(translate("salesWidgetTab", "inGameMarketError") + ": " + str(er))
                print_traceback(translate("salesWidgetTab", "inGameMarketError") + ": " + str(er))
                self.reset_in_game_market()
                return
        else:
            self.reset_in_game_market()


    def parse_in_game_market(self, data: InGameMarket) -> None:
        self.reset_in_game_market()
        n_in_game_market = len(self.alerts['InGameMarket'])
        for sales in data:
            if ("LandingPage" in sales):
                landing_page: InGameMarketLandingPage = InGameMarket["LandingPage"]
                if ("Categories" in landing_page):
                    for category in landing_page["Categories"]:
                        category_name = category["CategoryName"]
                        name = category["Name"]
                        icon = category["Icon"]
                        add_to_menu = category["AddToMenu"] if ("AddToMenu" in category) else False
                        items = category["Items"]

                        temp = InGameMarketBox()
                        temp.set_in_game_data(category_name, name, icon, add_to_menu, items)
                        self.alerts['InGameMarket'].add(temp)

        self.add_in_game_market(n_in_game_market)

    def add_in_game_market(self, n_in_game_market: int) -> None:
        for i in range(n_in_game_market, len(self.alerts['InGameMarket'])):
            if (not self.alerts['InGameMarket'][i].is_expired()):
                self.gridInGameItems.addLayout(self.alerts['InGameMarket'][i].MerBox,
                                                 self.gridInGameItems.count(), 0)


    def reset_in_game_market(self) -> None:
        cancelled = []
        for i in range(0, len(self.alerts['InGameMarket'])):
            cancelled.append(i)
        i = len(cancelled)
        while i > 0:
            self.alerts['InGameMarket'][cancelled[i - 1]].hide()
            remove_widget(self.alerts['InGameMarket'][cancelled[i - 1]].MerBox)
            del self.alerts['InGameMarket'][cancelled[i - 1]]
            i -= 1
