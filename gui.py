# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1010, 944)
        MainWindow.setMinimumSize(QSize(554, 934))
        MainWindow.setMaximumSize(QSize(1100, 944))
        icon = QIcon()
        icon.addFile(u":/images2/images/window.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QLineEdit{\n"
"	border: 0.3px solid rgb(0, 0, 0);\n"
"	border-radius : 10px;\n"
"	padding-left:5px;\n"
"	height:26px;\n"
"	\n"
"}\n"
"QLineEdit::hover{\n"
"	border:2px solid rgb(0, 255, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border:2px solid  rgb(0, 170, 255);\n"
"}\n"
"/*QLabel{\n"
"	font-family : Sitka Text\n"
"}*/\n"
"\n"
"\n"
"")
        self.actionSave_as_docx = QAction(MainWindow)
        self.actionSave_as_docx.setObjectName(u"actionSave_as_docx")
        icon1 = QIcon()
        icon1.addFile(u":/images2/images/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_as_docx.setIcon(icon1)
        self.actionSave_as_pdf = QAction(MainWindow)
        self.actionSave_as_pdf.setObjectName(u"actionSave_as_pdf")
        icon2 = QIcon()
        icon2.addFile(u":/images2/images/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_as_pdf.setIcon(icon2)
        self.actionMerge = QAction(MainWindow)
        self.actionMerge.setObjectName(u"actionMerge")
        icon3 = QIcon()
        icon3.addFile(u":/images2/images/merge.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMerge.setIcon(icon3)
        self.actionSplit = QAction(MainWindow)
        self.actionSplit.setObjectName(u"actionSplit")
        icon4 = QIcon()
        icon4.addFile(u":/images2/images/split.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSplit.setIcon(icon4)
        self.actionpreview = QAction(MainWindow)
        self.actionpreview.setObjectName(u"actionpreview")
        self.actionPrivew = QAction(MainWindow)
        self.actionPrivew.setObjectName(u"actionPrivew")
        icon5 = QIcon()
        icon5.addFile(u":/images2/images/preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrivew.setIcon(icon5)
        self.actionBewerbung = QAction(MainWindow)
        self.actionBewerbung.setObjectName(u"actionBewerbung")
        self.actioninternt = QAction(MainWindow)
        self.actioninternt.setObjectName(u"actioninternt")
        self.actionhandy = QAction(MainWindow)
        self.actionhandy.setObjectName(u"actionhandy")
        self.actionwohnung = QAction(MainWindow)
        self.actionwohnung.setObjectName(u"actionwohnung")
        self.actionarbeit = QAction(MainWindow)
        self.actionarbeit.setObjectName(u"actionarbeit")
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionGermany = QAction(MainWindow)
        self.actionGermany.setObjectName(u"actionGermany")
        self.actionEars = QAction(MainWindow)
        self.actionEars.setObjectName(u"actionEars")
        icon6 = QIcon()
        icon6.addFile(u":/images2/images/earse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEars.setIcon(icon6)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon7 = QIcon()
        icon7.addFile(u":/images2/images/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widgetform = QWidget(self.centralwidget)
        self.widgetform.setObjectName(u"widgetform")
        self.gridLayout_8 = QGridLayout(self.widgetform)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.line_3 = QFrame(self.widgetform)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_8.addWidget(self.line_3, 1, 0, 1, 1)

        self.text_label = QLabel(self.widgetform)
        self.text_label.setObjectName(u"text_label")
        self.text_label.setMinimumSize(QSize(500, 370))
        font = QFont()
        font.setFamily(u"Sitka Text")
        self.text_label.setFont(font)
        self.text_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(195, 194, 193);\n"
"border-radius:10px")
        self.text_label.setMargin(10)

        self.gridLayout_8.addWidget(self.text_label, 6, 0, 1, 1)

        self.line_5 = QFrame(self.widgetform)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_8.addWidget(self.line_5, 3, 0, 1, 1)

        self.s_label = QLabel(self.widgetform)
        self.s_label.setObjectName(u"s_label")
        self.s_label.setMinimumSize(QSize(500, 91))
        self.s_label.setFont(font)
        self.s_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(195, 194, 193);\n"
"border-radius:10px")
        self.s_label.setMargin(12)

        self.gridLayout_8.addWidget(self.s_label, 4, 0, 1, 1)

        self.line_10 = QFrame(self.widgetform)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_8.addWidget(self.line_10, 5, 0, 1, 1)

        self.firma_label = QLabel(self.widgetform)
        self.firma_label.setObjectName(u"firma_label")
        self.firma_label.setMinimumSize(QSize(500, 151))
        font1 = QFont()
        font1.setFamily(u"Sitka Text")
        font1.setPointSize(8)
        self.firma_label.setFont(font1)
        self.firma_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(195, 194, 193);\n"
"border-radius:10px")
        self.firma_label.setMargin(8)

        self.gridLayout_8.addWidget(self.firma_label, 2, 0, 1, 1)

        self.your_label = QLabel(self.widgetform)
        self.your_label.setObjectName(u"your_label")
        self.your_label.setMinimumSize(QSize(500, 173))
        self.your_label.setFont(font)
        self.your_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(195, 194, 193);\n"
"border-radius:10px")
        self.your_label.setMargin(11)

        self.gridLayout_8.addWidget(self.your_label, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widgetform, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 6, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.firma_str_line = QLineEdit(self.centralwidget)
        self.firma_str_line.setObjectName(u"firma_str_line")

        self.gridLayout_4.addWidget(self.firma_str_line, 4, 0, 1, 1)

        self.firma_address_line = QLineEdit(self.centralwidget)
        self.firma_address_line.setObjectName(u"firma_address_line")

        self.gridLayout_4.addWidget(self.firma_address_line, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rb_L_firma = QRadioButton(self.centralwidget)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.rb_L_firma)
        self.rb_L_firma.setObjectName(u"rb_L_firma")
        icon8 = QIcon()
        icon8.addFile(u":/images2/images/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rb_L_firma.setIcon(icon8)

        self.horizontalLayout_3.addWidget(self.rb_L_firma)

        self.rb_C_firma = QRadioButton(self.centralwidget)
        self.buttonGroup_2.addButton(self.rb_C_firma)
        self.rb_C_firma.setObjectName(u"rb_C_firma")
        icon9 = QIcon()
        icon9.addFile(u":/images2/images/center.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rb_C_firma.setIcon(icon9)

        self.horizontalLayout_3.addWidget(self.rb_C_firma)

        self.rb_R_firma = QRadioButton(self.centralwidget)
        self.buttonGroup_2.addButton(self.rb_R_firma)
        self.rb_R_firma.setObjectName(u"rb_R_firma")
        icon10 = QIcon()
        icon10.addFile(u":/images2/images/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rb_R_firma.setIcon(icon10)

        self.horizontalLayout_3.addWidget(self.rb_R_firma)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)

        self.f_colorBtn = QToolButton(self.centralwidget)
        self.f_colorBtn.setObjectName(u"f_colorBtn")
        self.f_colorBtn.setMinimumSize(QSize(70, 0))
        self.f_colorBtn.setMaximumSize(QSize(40, 16777215))
        icon11 = QIcon()
        icon11.addFile(u":/images2/images/color.png", QSize(), QIcon.Normal, QIcon.Off)
        self.f_colorBtn.setIcon(icon11)

        self.gridLayout_4.addWidget(self.f_colorBtn, 3, 1, 1, 1, Qt.AlignHCenter)

        self.styleComp_label = QLabel(self.centralwidget)
        self.styleComp_label.setObjectName(u"styleComp_label")
        font2 = QFont()
        font2.setFamily(u"Sitka Text")
        font2.setBold(True)
        font2.setWeight(75)
        self.styleComp_label.setFont(font2)

        self.gridLayout_4.addWidget(self.styleComp_label, 0, 1, 1, 1, Qt.AlignHCenter)

        self.firma_name_line = QLineEdit(self.centralwidget)
        self.firma_name_line.setObjectName(u"firma_name_line")

        self.gridLayout_4.addWidget(self.firma_name_line, 1, 0, 1, 1)

        self.f_fontBtn = QToolButton(self.centralwidget)
        self.f_fontBtn.setObjectName(u"f_fontBtn")
        self.f_fontBtn.setMinimumSize(QSize(70, 0))
        self.f_fontBtn.setMaximumSize(QSize(40, 16777215))
        icon12 = QIcon()
        icon12.addFile(u":/images2/images/font.png", QSize(), QIcon.Normal, QIcon.Off)
        self.f_fontBtn.setIcon(icon12)

        self.gridLayout_4.addWidget(self.f_fontBtn, 1, 1, 1, 1, Qt.AlignHCenter)

        self.comp_label = QLabel(self.centralwidget)
        self.comp_label.setObjectName(u"comp_label")
        self.comp_label.setMinimumSize(QSize(0, 0))
        self.comp_label.setMaximumSize(QSize(16777215, 16777215))
        self.comp_label.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setFamily(u"Sitka Text")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.comp_label.setFont(font3)
        self.comp_label.setLineWidth(1)
        self.comp_label.setMidLineWidth(0)
        self.comp_label.setScaledContents(False)
        self.comp_label.setAlignment(Qt.AlignCenter)
        self.comp_label.setWordWrap(False)
        self.comp_label.setMargin(-1)
        self.comp_label.setIndent(-1)
        self.comp_label.setOpenExternalLinks(False)

        self.gridLayout_4.addWidget(self.comp_label, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.gridLayout_4.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.your2_city_line = QLineEdit(self.centralwidget)
        self.your2_city_line.setObjectName(u"your2_city_line")

        self.gridLayout.addWidget(self.your2_city_line, 2, 1, 1, 1)

        self.styleInfo_label = QLabel(self.centralwidget)
        self.styleInfo_label.setObjectName(u"styleInfo_label")
        self.styleInfo_label.setFont(font2)

        self.gridLayout.addWidget(self.styleInfo_label, 0, 3, 1, 1, Qt.AlignHCenter)

        self.your_fontBtn = QToolButton(self.centralwidget)
        self.your_fontBtn.setObjectName(u"your_fontBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.your_fontBtn.sizePolicy().hasHeightForWidth())
        self.your_fontBtn.setSizePolicy(sizePolicy)
        self.your_fontBtn.setMinimumSize(QSize(70, 26))
        self.your_fontBtn.setMaximumSize(QSize(50, 50))
        self.your_fontBtn.setSizeIncrement(QSize(0, 0))
        self.your_fontBtn.setBaseSize(QSize(0, 0))
        self.your_fontBtn.setStyleSheet(u"")
        self.your_fontBtn.setIcon(icon12)
        self.your_fontBtn.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.your_fontBtn, 1, 3, 1, 1, Qt.AlignHCenter)

        self.info_label = QLabel(self.centralwidget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setMaximumSize(QSize(16777215, 17))
        self.info_label.setFont(font3)

        self.gridLayout.addWidget(self.info_label, 0, 1, 1, 2, Qt.AlignHCenter)

        self.your_colorBtn = QToolButton(self.centralwidget)
        self.your_colorBtn.setObjectName(u"your_colorBtn")
        self.your_colorBtn.setMinimumSize(QSize(70, 0))
        self.your_colorBtn.setMaximumSize(QSize(40, 16777215))
        self.your_colorBtn.setIcon(icon11)

        self.gridLayout.addWidget(self.your_colorBtn, 2, 3, 1, 1, Qt.AlignHCenter)

        self.your_zipcode_line = QLineEdit(self.centralwidget)
        self.your_zipcode_line.setObjectName(u"your_zipcode_line")
        self.your_zipcode_line.setMaximumSize(QSize(67, 16777215))

        self.gridLayout.addWidget(self.your_zipcode_line, 2, 0, 1, 1)

        self.your1_name_line = QLineEdit(self.centralwidget)
        self.your1_name_line.setObjectName(u"your1_name_line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.your1_name_line.sizePolicy().hasHeightForWidth())
        self.your1_name_line.setSizePolicy(sizePolicy1)
        self.your1_name_line.setMinimumSize(QSize(253, 20))
        self.your1_name_line.setMaximumSize(QSize(16777215, 16777215))
        self.your1_name_line.setSizeIncrement(QSize(0, 0))
        self.your1_name_line.setStyleSheet(u"")

        self.gridLayout.addWidget(self.your1_name_line, 1, 0, 1, 2)

        self.your3_street_line = QLineEdit(self.centralwidget)
        self.your3_street_line.setObjectName(u"your3_street_line")

        self.gridLayout.addWidget(self.your3_street_line, 3, 0, 1, 2)

        self.your4_email_line = QLineEdit(self.centralwidget)
        self.your4_email_line.setObjectName(u"your4_email_line")

        self.gridLayout.addWidget(self.your4_email_line, 4, 0, 1, 2)

        self.your5_tn_line = QLineEdit(self.centralwidget)
        self.your5_tn_line.setObjectName(u"your5_tn_line")

        self.gridLayout.addWidget(self.your5_tn_line, 5, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rb_L_your = QRadioButton(self.centralwidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.rb_L_your)
        self.rb_L_your.setObjectName(u"rb_L_your")
        self.rb_L_your.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.rb_L_your)

        self.rb_C_your = QRadioButton(self.centralwidget)
        self.buttonGroup.addButton(self.rb_C_your)
        self.rb_C_your.setObjectName(u"rb_C_your")
        self.rb_C_your.setIcon(icon9)

        self.horizontalLayout_2.addWidget(self.rb_C_your)

        self.rb_R_your = QRadioButton(self.centralwidget)
        self.buttonGroup.addButton(self.rb_R_your)
        self.rb_R_your.setObjectName(u"rb_R_your")
        self.rb_R_your.setIcon(icon10)

        self.horizontalLayout_2.addWidget(self.rb_R_your)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(7)
        self.gridLayout_3.setVerticalSpacing(4)
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.main_text = QTextEdit(self.centralwidget)
        self.main_text.setObjectName(u"main_text")
        self.main_text.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(195, 194, 193);\n"
"border-radius:10px")

        self.gridLayout_3.addWidget(self.main_text, 3, 0, 1, 5)

        self.send_label = QLabel(self.centralwidget)
        self.send_label.setObjectName(u"send_label")
        self.send_label.setMaximumSize(QSize(335, 16777215))
        font4 = QFont()
        font4.setFamily(u"Sitka Text")
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setWeight(75)
        self.send_label.setFont(font4)
        self.send_label.setMargin(0)

        self.gridLayout_3.addWidget(self.send_label, 0, 0, 1, 1)

        self.mr_rb = QRadioButton(self.centralwidget)
        self.buttonGroup_3 = QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.mr_rb)
        self.mr_rb.setObjectName(u"mr_rb")
        self.mr_rb.setMaximumSize(QSize(89, 16777215))
        font5 = QFont()
        font5.setFamily(u"Sitka Text")
        font5.setPointSize(7)
        font5.setBold(True)
        font5.setWeight(75)
        self.mr_rb.setFont(font5)

        self.gridLayout_3.addWidget(self.mr_rb, 0, 1, 1, 1)

        self.sendTo_line = QLineEdit(self.centralwidget)
        self.sendTo_line.setObjectName(u"sendTo_line")

        self.gridLayout_3.addWidget(self.sendTo_line, 2, 0, 1, 4)

        self.plural_rb = QRadioButton(self.centralwidget)
        self.buttonGroup_3.addButton(self.plural_rb)
        self.plural_rb.setObjectName(u"plural_rb")
        self.plural_rb.setFont(font5)

        self.gridLayout_3.addWidget(self.plural_rb, 0, 3, 1, 1)

        self.miss_rb = QRadioButton(self.centralwidget)
        self.buttonGroup_3.addButton(self.miss_rb)
        self.miss_rb.setObjectName(u"miss_rb")
        self.miss_rb.setFont(font5)

        self.gridLayout_3.addWidget(self.miss_rb, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 7, 0, 1, 1)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_8, 8, 1, 1, 1)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 3, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(7)
        self.gridLayout_6.setContentsMargins(-1, 0, 0, -1)
        self.sub_label = QLabel(self.centralwidget)
        self.sub_label.setObjectName(u"sub_label")
        self.sub_label.setFont(font3)
        self.sub_label.setMargin(-1)

        self.gridLayout_6.addWidget(self.sub_label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.subject_line = QLineEdit(self.centralwidget)
        self.subject_line.setObjectName(u"subject_line")
        self.subject_line.setMinimumSize(QSize(246, 0))

        self.gridLayout_6.addWidget(self.subject_line, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(47, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.s_colorBtn = QToolButton(self.centralwidget)
        self.s_colorBtn.setObjectName(u"s_colorBtn")
        self.s_colorBtn.setMinimumSize(QSize(70, 0))
        self.s_colorBtn.setMaximumSize(QSize(40, 16777215))
        self.s_colorBtn.setIcon(icon11)

        self.gridLayout_6.addWidget(self.s_colorBtn, 3, 2, 1, 1)

        self.styleSub_label = QLabel(self.centralwidget)
        self.styleSub_label.setObjectName(u"styleSub_label")
        self.styleSub_label.setFont(font2)

        self.gridLayout_6.addWidget(self.styleSub_label, 0, 2, 1, 1, Qt.AlignHCenter)

        self.s_fontBtn = QToolButton(self.centralwidget)
        self.s_fontBtn.setObjectName(u"s_fontBtn")
        self.s_fontBtn.setMinimumSize(QSize(70, 0))
        self.s_fontBtn.setIcon(icon12)

        self.gridLayout_6.addWidget(self.s_fontBtn, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(52, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 26))
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        font6.setWeight(75)
        self.dateEdit.setFont(font6)
        self.dateEdit.setStyleSheet(u"border-radius : 10px;\n"
"padding-left:15px")
        self.dateEdit.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))

        self.gridLayout_6.addWidget(self.dateEdit, 3, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_7, 4, 0, 1, 1)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_6, 1, 1, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1010, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menupdf_Tools = QMenu(self.menubar)
        self.menupdf_Tools.setObjectName(u"menupdf_Tools")
        self.menuExamples = QMenu(self.menubar)
        self.menuExamples.setObjectName(u"menuExamples")
        self.menuk_ndigung = QMenu(self.menuExamples)
        self.menuk_ndigung.setObjectName(u"menuk_ndigung")
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        self.menuLanguages = QMenu(self.menuSetting)
        self.menuLanguages.setObjectName(u"menuLanguages")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setEnabled(True)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(34, 30))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(True)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        QWidget.setTabOrder(self.your1_name_line, self.your_zipcode_line)
        QWidget.setTabOrder(self.your_zipcode_line, self.your2_city_line)
        QWidget.setTabOrder(self.your2_city_line, self.your3_street_line)
        QWidget.setTabOrder(self.your3_street_line, self.your4_email_line)
        QWidget.setTabOrder(self.your4_email_line, self.your5_tn_line)
        QWidget.setTabOrder(self.your5_tn_line, self.firma_name_line)
        QWidget.setTabOrder(self.firma_name_line, self.firma_address_line)
        QWidget.setTabOrder(self.firma_address_line, self.firma_str_line)
        QWidget.setTabOrder(self.firma_str_line, self.subject_line)
        QWidget.setTabOrder(self.subject_line, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.sendTo_line)
        QWidget.setTabOrder(self.sendTo_line, self.main_text)
        QWidget.setTabOrder(self.main_text, self.your_colorBtn)
        QWidget.setTabOrder(self.your_colorBtn, self.rb_L_your)
        QWidget.setTabOrder(self.rb_L_your, self.rb_C_your)
        QWidget.setTabOrder(self.rb_C_your, self.rb_R_your)
        QWidget.setTabOrder(self.rb_R_your, self.f_fontBtn)
        QWidget.setTabOrder(self.f_fontBtn, self.f_colorBtn)
        QWidget.setTabOrder(self.f_colorBtn, self.rb_L_firma)
        QWidget.setTabOrder(self.rb_L_firma, self.rb_C_firma)
        QWidget.setTabOrder(self.rb_C_firma, self.rb_R_firma)
        QWidget.setTabOrder(self.rb_R_firma, self.s_fontBtn)
        QWidget.setTabOrder(self.s_fontBtn, self.s_colorBtn)
        QWidget.setTabOrder(self.s_colorBtn, self.mr_rb)
        QWidget.setTabOrder(self.mr_rb, self.miss_rb)
        QWidget.setTabOrder(self.miss_rb, self.plural_rb)
        QWidget.setTabOrder(self.plural_rb, self.your_fontBtn)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menupdf_Tools.menuAction())
        self.menubar.addAction(self.menuExamples.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menuFile.addAction(self.actionSave_as_docx)
        self.menuFile.addAction(self.actionSave_as_pdf)
        self.menuFile.addAction(self.actionPrivew)
        self.menuFile.addAction(self.actionEars)
        self.menuFile.addAction(self.actionQuit)
        self.menupdf_Tools.addAction(self.actionMerge)
        self.menupdf_Tools.addAction(self.actionSplit)
        self.menuExamples.addAction(self.actionBewerbung)
        self.menuExamples.addAction(self.menuk_ndigung.menuAction())
        self.menuk_ndigung.addAction(self.actioninternt)
        self.menuk_ndigung.addAction(self.actionhandy)
        self.menuk_ndigung.addAction(self.actionwohnung)
        self.menuk_ndigung.addAction(self.actionarbeit)
        self.menuSetting.addAction(self.menuLanguages.menuAction())
        self.menuLanguages.addAction(self.actionEnglish)
        self.menuLanguages.addAction(self.actionGermany)
        self.toolBar.addAction(self.actionSave_as_docx)
        self.toolBar.addAction(self.actionSave_as_pdf)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMerge)
        self.toolBar.addAction(self.actionSplit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPrivew)
        self.toolBar.addAction(self.actionEars)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Templete", None))
        self.actionSave_as_docx.setText(QCoreApplication.translate("MainWindow", u"Save as .docx ", None))
#if QT_CONFIG(shortcut)
        self.actionSave_as_docx.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_as_pdf.setText(QCoreApplication.translate("MainWindow", u"Save as pdf", None))
#if QT_CONFIG(shortcut)
        self.actionSave_as_pdf.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionMerge.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
#if QT_CONFIG(shortcut)
        self.actionMerge.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionSplit.setText(QCoreApplication.translate("MainWindow", u"Split", None))
#if QT_CONFIG(shortcut)
        self.actionSplit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionpreview.setText(QCoreApplication.translate("MainWindow", u"preview", None))
        self.actionPrivew.setText(QCoreApplication.translate("MainWindow", u"Privew", None))
#if QT_CONFIG(shortcut)
        self.actionPrivew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionBewerbung.setText(QCoreApplication.translate("MainWindow", u"Bewerbung", None))
        self.actioninternt.setText(QCoreApplication.translate("MainWindow", u"Internet", None))
        self.actionhandy.setText(QCoreApplication.translate("MainWindow", u"Handy", None))
        self.actionwohnung.setText(QCoreApplication.translate("MainWindow", u"Wohnung", None))
        self.actionarbeit.setText(QCoreApplication.translate("MainWindow", u"Arbeit", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionGermany.setText(QCoreApplication.translate("MainWindow", u"Germany", None))
        self.actionEars.setText(QCoreApplication.translate("MainWindow", u"Earse", None))
#if QT_CONFIG(shortcut)
        self.actionEars.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.text_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\"> Main Letter</span></p></body></html>", None))
        self.s_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">City, Today Date</span></p><p><span style=\" font-weight:600;\">Subject </span></p></body></html>", None))
        self.firma_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Company Name</span></p><p><span style=\" font-weight:600;\">Company Address</span></p><p><span style=\" font-weight:600;\">Company Street</span></p></body></html>", None))
        self.your_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Your Name</span></p><p align=\"right\"><span style=\" font-weight:600;\">Your Street</span></p><p align=\"right\"><span style=\" font-weight:600;\">Your Email</span></p><p align=\"right\"><span style=\" font-weight:600;\">Your TN</span></p></body></html>", None))
        self.firma_str_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Street", None))
        self.firma_address_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.rb_L_firma.setText("")
        self.rb_C_firma.setText("")
        self.rb_R_firma.setText("")
        self.f_colorBtn.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.styleComp_label.setText(QCoreApplication.translate("MainWindow", u"Style", None))
        self.firma_name_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Company Name", None))
        self.f_fontBtn.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.comp_label.setText(QCoreApplication.translate("MainWindow", u"Company Information", None))
        self.your2_city_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"City", None))
        self.styleInfo_label.setText(QCoreApplication.translate("MainWindow", u"Style", None))
        self.your_fontBtn.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.info_label.setText(QCoreApplication.translate("MainWindow", u"Your Information", None))
        self.your_colorBtn.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.your_zipcode_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Zip Code", None))
        self.your1_name_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Name & Last Name", None))
        self.your3_street_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Street", None))
        self.your4_email_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.your5_tn_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telephone Number", None))
        self.rb_L_your.setText("")
        self.rb_C_your.setText("")
        self.rb_R_your.setText("")
        self.send_label.setText(QCoreApplication.translate("MainWindow", u"Send to :", None))
        self.mr_rb.setText(QCoreApplication.translate("MainWindow", u"Herr", None))
        self.sendTo_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The recipient's name", None))
        self.plural_rb.setText(QCoreApplication.translate("MainWindow", u"Plural", None))
        self.miss_rb.setText(QCoreApplication.translate("MainWindow", u"Frau", None))
        self.sub_label.setText(QCoreApplication.translate("MainWindow", u"Subject", None))
        self.s_colorBtn.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.styleSub_label.setText(QCoreApplication.translate("MainWindow", u"Style", None))
#if QT_CONFIG(tooltip)
        self.s_fontBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.s_fontBtn.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menupdf_Tools.setTitle(QCoreApplication.translate("MainWindow", u"pdf Tools", None))
        self.menuExamples.setTitle(QCoreApplication.translate("MainWindow", u"Examples", None))
        self.menuk_ndigung.setTitle(QCoreApplication.translate("MainWindow", u"K\u00fcndigung", None))
        self.menuSetting.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.menuLanguages.setTitle(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

