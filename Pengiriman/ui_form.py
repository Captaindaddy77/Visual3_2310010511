# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.actionAdmin = QAction(Main)
        self.actionAdmin.setObjectName(u"actionAdmin")
        self.actionBarang = QAction(Main)
        self.actionBarang.setObjectName(u"actionBarang")
        self.actionPembayaran = QAction(Main)
        self.actionPembayaran.setObjectName(u"actionPembayaran")
        self.actionPengiriman = QAction(Main)
        self.actionPengiriman.setObjectName(u"actionPengiriman")
        self.actionKurir = QAction(Main)
        self.actionKurir.setObjectName(u"actionKurir")
        self.actionTracking = QAction(Main)
        self.actionTracking.setObjectName(u"actionTracking")
        self.HalamanUtama = QWidget(Main)
        self.HalamanUtama.setObjectName(u"HalamanUtama")
        Main.setCentralWidget(self.HalamanUtama)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionBarang)
        self.menuMenu.addAction(self.actionPengiriman)
        self.menuMenu.addAction(self.actionPembayaran)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionKurir)
        self.menuMenu.addAction(self.actionTracking)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.actionAdmin.setText(QCoreApplication.translate("Main", u"Admin", None))
        self.actionBarang.setText(QCoreApplication.translate("Main", u"Barang", None))
        self.actionPembayaran.setText(QCoreApplication.translate("Main", u"Pembayaran", None))
        self.actionPengiriman.setText(QCoreApplication.translate("Main", u"Pengiriman", None))
        self.actionKurir.setText(QCoreApplication.translate("Main", u"Kurir", None))
        self.actionTracking.setText(QCoreApplication.translate("Main", u"Tracking", None))
        self.menuMenu.setTitle(QCoreApplication.translate("Main", u"Menu", None))
    # retranslateUi

