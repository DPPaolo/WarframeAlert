# coding=utf-8
from PyQt5 import QtWidgets, QtGui

from warframeAlert.components.common.CommonLabelWithImage import CommonLabelWithImage
from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import is_mac_os
from warframeAlert.utils.stringUtils import set_barred
from warframeAlert.utils.timeUtils import get_time


class DailyDeals:
    def __init__(self):
        font = QtGui.QFont()
        font.setBold(True)

        self.DealsLab = QtWidgets.QLabel(translate("dailyDeals", "dailyDeals") + ": ")
        self.Deals = QtWidgets.QLabel("N/D")
        self.DealsEnd = Countdown(translate("dailyDeals", "end"))
        self.DealsSpace1 = QtWidgets.QLabel("")

        self.DealsAmount = QtWidgets.QLabel("N/D")
        self.DealsOriginalPriceLab = QtWidgets.QLabel(translate("dailyDeals", "price") + ": ")
        self.DealsOriginalPrice = QtWidgets.QLabel("N/D")
        self.DealsPrice = CommonLabelWithImage("/assets/icon/platinum.png", "N/D")
        self.DealsSales = QtWidgets.QLabel("N/D")

        font_barred = self.DealsOriginalPrice.font()
        font_barred.setStrikeOut(True)
        self.DealsOriginalPrice.setFont(font_barred)

        self.DealsBox = QtWidgets.QVBoxLayout()

        self.Dealshbox1 = QtWidgets.QHBoxLayout()
        self.Dealshbox2 = QtWidgets.QHBoxLayout()

        self.Dealshbox1.addWidget(self.DealsLab)
        self.Dealshbox1.addWidget(self.Deals)
        self.Dealshbox1.addWidget(self.DealsEnd.TimeLab)

        self.Dealshbox2.addWidget(self.DealsAmount)
        if (is_mac_os()):
            self.Dealshbox2.addWidget(self.DealsSpace1)
            self.Dealshbox2.addWidget(self.DealsOriginalPriceLab)
            self.Dealshbox2.addWidget(self.DealsOriginalPrice)

        self.Dealshbox2.addLayout(self.DealsPrice.LabelWithImage)
        self.Dealshbox2.addWidget(self.DealsSales)

        self.DealsBox.addLayout(self.Dealshbox1)
        self.DealsBox.addLayout(self.Dealshbox2)

    def set_deals_data(self, init, end, item, q_sold, q_total, original_price, sales, price_sales):
        self.DealsEnd.set_countdown(end[:10])
        self.DealsEnd.start()

        self.DealsLab.setToolTip(translate("dailyDeals", "start") + get_time(init))

        self.Deals.setText(item)

        self.DealsSales.setText(translate("dailyDeals", "sale") + " " + str(sales) + "%")

        if (is_mac_os()):
            self.DealsAmount.setText(translate("dailyDeals", "sold") + ": " + str(q_sold) + " / " + str(q_total))
            self.DealsOriginalPrice.setText(str(original_price))
            self.DealsPrice.set_before_text(str(price_sales) + " Platinum")
        else:
            price = set_barred(str(original_price)) + "  " + str(price_sales)

            self.DealsAmount.setText(translate("dailyDeals", "sold") + ": " + str(q_sold) + " / " + str(q_total))
            self.DealsPrice.set_before_text(translate("dailyDeals", "price") + ": " + str(price) + " Platinum")

