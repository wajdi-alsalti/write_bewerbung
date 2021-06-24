# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'merge.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


import res2

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(435, 234)
        Form.setMinimumSize(QSize(435, 234))
        Form.setMaximumSize(QSize(435,234))
        icon = QIcon()
        icon.addFile(u":/images2/images/merge.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.add_btn = QPushButton(Form)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(10, 20, 93, 28))
        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(230, 180, 193, 28))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.remove_btn = QPushButton(Form)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setGeometry(QRect(10, 60, 93, 28))
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(111, 17, 311, 151))
        self.up_btn = QToolButton(Form)
        self.up_btn.setObjectName(u"up_btn")
        self.up_btn.setGeometry(QRect(70, 100, 27, 26))
        icon1 = QIcon()
        icon1.addFile(u":/images2/images/up arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.up_btn.setIcon(icon1)
        self.down_btn = QToolButton(Form)
        self.down_btn.setObjectName(u"down_btn")
        self.down_btn.setGeometry(QRect(70, 140, 27, 26))
        icon2 = QIcon()
        icon2.addFile(u":/images2/images/down arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.down_btn.setIcon(icon2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Merge Files", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"Add", None))
        self.remove_btn.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.up_btn.setText("")
        self.down_btn.setText("")
    # retranslateUi

