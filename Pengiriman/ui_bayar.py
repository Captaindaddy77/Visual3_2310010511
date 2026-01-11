# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bayar.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_FormBayar(object):
    def setupUi(self, FormBayar):
        if not FormBayar.objectName():
            FormBayar.setObjectName(u"FormBayar")
        FormBayar.resize(607, 477)
        self.lblJudul = QLabel(FormBayar)
        self.lblJudul.setObjectName(u"lblJudul")
        self.lblJudul.setGeometry(QRect(10, 10, 578, 24))
        self.lblJudul.setStyleSheet(u"font-size:18px; font-weight:bold; color:#2b5fab;")
        self.lblJudul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget = QWidget(FormBayar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 50, 581, 141))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblKode = QLabel(self.layoutWidget)
        self.lblKode.setObjectName(u"lblKode")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblKode)

        self.txtKode = QLineEdit(self.layoutWidget)
        self.txtKode.setObjectName(u"txtKode")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtKode)

        self.lblNamaBarang = QLabel(self.layoutWidget)
        self.lblNamaBarang.setObjectName(u"lblNamaBarang")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblNamaBarang)

        self.txtNamaBarang = QLineEdit(self.layoutWidget)
        self.txtNamaBarang.setObjectName(u"txtNamaBarang")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtNamaBarang)

        self.lblHarga = QLabel(self.layoutWidget)
        self.lblHarga.setObjectName(u"lblHarga")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblHarga)

        self.txtHarga = QLineEdit(self.layoutWidget)
        self.txtHarga.setObjectName(u"txtHarga")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtHarga)

        self.lblJumlah = QLabel(self.layoutWidget)
        self.lblJumlah.setObjectName(u"lblJumlah")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblJumlah)

        self.txtJumlah = QLineEdit(self.layoutWidget)
        self.txtJumlah.setObjectName(u"txtJumlah")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtJumlah)

        self.layoutWidget_2 = QWidget(FormBayar)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(120, 200, 343, 31))
        self.buttonLayout = QHBoxLayout(self.layoutWidget_2)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.btnSimpan = QPushButton(self.layoutWidget_2)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(self.layoutWidget_2)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnTampil = QPushButton(self.layoutWidget_2)
        self.btnTampil.setObjectName(u"btnTampil")

        self.buttonLayout.addWidget(self.btnTampil)


        self.retranslateUi(FormBayar)

        QMetaObject.connectSlotsByName(FormBayar)
    # setupUi

    def retranslateUi(self, FormBayar):
        FormBayar.setWindowTitle(QCoreApplication.translate("FormBayar", u"FormBayar", None))
        self.lblJudul.setText(QCoreApplication.translate("FormBayar", u"Form Pembayaran Barang", None))
        self.lblKode.setText(QCoreApplication.translate("FormBayar", u"Kode Barang", None))
        self.lblNamaBarang.setText(QCoreApplication.translate("FormBayar", u"Nama Barang", None))
        self.lblHarga.setText(QCoreApplication.translate("FormBayar", u"Harga", None))
        self.lblJumlah.setText(QCoreApplication.translate("FormBayar", u"Jumlah", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormBayar", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormBayar", u"Ubah", None))
        self.btnTampil.setText(QCoreApplication.translate("FormBayar", u"Tampil", None))
    # retranslateUi

