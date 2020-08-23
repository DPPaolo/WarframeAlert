# coding=utf-8
from PyQt5 import QtWidgets, QtGui

from warframeAlert.components.common.CommonLabelWithImage import CommonLabelWithImage
from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import bool_to_yes_no
from warframeAlert.utils.fileUtils import get_separator


class SalesBox():

    def __init__(self, index):
        self.index = index
        self.SaleName = QtWidgets.QLabel("N/D")
        platinum_image = "assets" + get_separator() + "icon" + get_separator() + "platinum.png"
        self.SalePricePlatinum = CommonLabelWithImage(platinum_image, "N/D")
        credit_image = "assets" + get_separator() + "icon" + get_separator() + "credit.png"
        self.SalePriceCredit = CommonLabelWithImage(credit_image, "N/D")
        self.SaleDiscount = QtWidgets.QLabel(translate("salesBox", "discount") + ": N/D")
        self.SaleTime = Countdown(translate("salesBox", "end"))
        self.SaleIsShow = QtWidgets.QLabel(translate("salesBox", "isShow") + ": N/D")

        self.Font = QtGui.QFont()
        self.Font.setBold(True)
        self.SaleName.setFont(self.Font)
        self.SaleDiscount.setFont(self.Font)

        self.MerBox = QtWidgets.QVBoxLayout()

        self.SalesBox1 = QtWidgets.QHBoxLayout()
        self.SalesBox2 = QtWidgets.QHBoxLayout()

        self.SalesBox1.addWidget(self.SaleName)
        self.SalesBox1.addWidget(self.SaleTime.TimeLab)
        self.SalesBox1.addWidget(self.SaleIsShow)

        self.SalesBox2.addLayout(self.SalePricePlatinum.LabelWithImage)
        self.SalesBox2.addLayout(self.SalePriceCredit.LabelWithImage)
        self.SalesBox2.addWidget(self.SaleDiscount)

        self.MerBox.addLayout(self.SalesBox1)
        self.MerBox.addLayout(self.SalesBox2)

        self.SaleTime.TimeOut.connect(self.hide)

    def set_sales_data(self, name, credit, plat, discount, end, is_show):
        self.SaleName.setText(name)
        self.SaleIsShow.setText(translate("salesBox", "isShow") + ": " + bool_to_yes_no(is_show))
        self.SaleDiscount.setText(translate("salesBox", "discount") + ": " + str(discount) + "%")
        if (discount == 0):
            self.hide_discount()

        self.SaleTime.set_countdown(end[:10])
        self.SaleTime.start()

        if (credit != 0):
            self.SalePriceCredit.set_before_text(str(credit) + " " + translate("salesBox", "credits"))
        else:
            self.SalePriceCredit.hide()
        if (plat != 0):
            self.SalePricePlatinum.set_before_text(str(plat) + " " + translate("salesBox", "platinum"))
        else:
            self.SalePricePlatinum.hide()

    def set_other_sales_data(self, bogobuy, bogoget, featured, popular, init):
        self.SaleTime.set_tooltip(translate("salesBox", "start") + ": " + init)
        name_tooltip = translate("salesBox", "bogobuy") + ": " + str(bogobuy) + "\n"
        name_tooltip += translate("salesBox", "bogoget") + ": " + str(bogoget)
        self.SaleName.setToolTip(name_tooltip)
        is_show_tooltip = translate("salesBox", "featured") + ": " + bool_to_yes_no(featured) + "\n"
        is_show_tooltip += translate("salesBox", "popular") + ": " + bool_to_yes_no(popular)
        self.SaleIsShow.setToolTip(is_show_tooltip)

    def get_item_name(self):
        return self.SaleName.text()

    def is_expired(self):
        return (int(self.SaleTime.get_time()) - int(timeUtils.get_local_time())) < 0

    def hide_discount(self):
        self.SaleDiscount.hide()

    def hide(self):
        self.SaleName.hide()
        self.SalePriceCredit.hide()
        self.SalePricePlatinum.hide()
        self.hide_discount()
        self.SaleTime.hide()
