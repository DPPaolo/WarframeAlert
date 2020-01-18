from PyQt5 import QtWidgets, QtGui

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.services.translationService import translate
from warframeAlert.utils.stringUtils import set_barred
from warframeAlert.utils.timeUtils import get_time


class DailyDeals:
    def __init__(self):
        font = QtGui.QFont()
        font.setBold(True)

        font_barred = QtGui.QFont()
        font_barred.setStrikeOut(True)

        self.DealsLab = QtWidgets.QLabel(translate("dailyDeals", "dailyDeals") + ": ")
        self.Deals = QtWidgets.QLabel("N/D")
        self.DealsEnd = Countdown(translate("dailyDeals", "end"))

        self.DealsAmount = QtWidgets.QLabel("N/D")
        self.DealsPrice = QtWidgets.QLabel("N/D")
        self.DealsSales = QtWidgets.QLabel("N/D")

        self.DealsBox = QtWidgets.QVBoxLayout()

        self.Dealshbox1 = QtWidgets.QHBoxLayout()
        self.Dealshbox2 = QtWidgets.QHBoxLayout()

        self.Dealshbox1.addWidget(self.DealsLab)
        self.Dealshbox1.addWidget(self.Deals)
        self.Dealshbox1.addWidget(self.DealsEnd.TimeLab)

        self.Dealshbox2.addWidget(self.DealsAmount)
        self.Dealshbox2.addWidget(self.DealsPrice)
        self.Dealshbox2.addWidget(self.DealsSales)

        self.DealsBox.addLayout(self.Dealshbox1)
        self.DealsBox.addLayout(self.Dealshbox2)

    def set_deals_data(self, init, end, item, q_sold, q_total, original_price, sales, price_sales):
        self.DealsEnd.set_countdown(end[:10])
        self.DealsEnd.start()

        self.DealsLab.setToolTip(translate("dailyDeals", "start") + get_time(init))

        price = set_barred(str(original_price)) + "  " + str(price_sales)

        self.Deals.setText(item)
        self.DealsAmount.setText(translate("dailyDeals", "sold") + ": " + str(q_sold) + " / " + str(q_total))
        self.DealsPrice.setText(translate("dailyDeals", "price") + ": " + str(price) + " Platinum")
        self.DealsSales.setText(translate("dailyDeals", "sale") + " " + str(sales) + "%")
