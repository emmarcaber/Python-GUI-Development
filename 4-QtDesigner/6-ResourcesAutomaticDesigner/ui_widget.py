# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(407, 60)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minus_button = QPushButton(Form)
        self.minus_button.setObjectName(u"minus_button")
        icon = QIcon()
        icon.addFile(u":/images/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minus_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.minus_button)

        self.spin_box = QSpinBox(Form)
        self.spin_box.setObjectName(u"spin_box")

        self.horizontalLayout.addWidget(self.spin_box)

        self.plus_button = QPushButton(Form)
        self.plus_button.setObjectName(u"plus_button")
        icon1 = QIcon()
        icon1.addFile(u":/images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.plus_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.plus_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.minus_button.setText(QCoreApplication.translate("Form", u"minus", None))
        self.plus_button.setText(QCoreApplication.translate("Form", u"plus", None))
    # retranslateUi

