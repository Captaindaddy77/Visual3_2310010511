# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pembayaran.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_FormPembayaran(object):
    def setupUi(self, FormPembayaran):
        if not FormPembayaran.objectName():
            FormPembayaran.setObjectName(u"FormPembayaran")
        FormPembayaran.resize(600, 520)
        self.verticalLayout = QVBoxLayout(FormPembayaran)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblJudul = QLabel(FormPembayaran)
        self.lblJudul.setObjectName(u"lblJudul")
        self.lblJudul.setStyleSheet(u"font-size:18px; font-weight:bold; color:#2b5fab;")
        self.lblJudul.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblJudul)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblPembayaranID = QLabel(FormPembayaran)
        self.lblPembayaranID.setObjectName(u"lblPembayaranID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblPembayaranID)

        self.txtPembayaranID = QLineEdit(FormPembayaran)
        self.txtPembayaranID.setObjectName(u"txtPembayaranID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtPembayaranID)

        self.lblPengirimanID = QLabel(FormPembayaran)
        self.lblPengirimanID.setObjectName(u"lblPengirimanID")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblPengirimanID)

        self.txtPengirimanID = QLineEdit(FormPembayaran)
        self.txtPengirimanID.setObjectName(u"txtPengirimanID")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtPengirimanID)

        self.lblMetode = QLabel(FormPembayaran)
        self.lblMetode.setObjectName(u"lblMetode")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblMetode)

        self.comboMetode = QComboBox(FormPembayaran)
        self.comboMetode.addItem("")
        self.comboMetode.addItem("")
        self.comboMetode.addItem("")
        self.comboMetode.setObjectName(u"comboMetode")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboMetode)

        self.lblJumlah = QLabel(FormPembayaran)
        self.lblJumlah.setObjectName(u"lblJumlah")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblJumlah)

        self.txtJumlah = QLineEdit(FormPembayaran)
        self.txtJumlah.setObjectName(u"txtJumlah")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtJumlah)

        self.lblStatus = QLabel(FormPembayaran)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.comboStatus = QComboBox(FormPembayaran)
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.setObjectName(u"comboStatus")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.comboStatus)

        self.lblTanggalBayar = QLabel(FormPembayaran)
        self.lblTanggalBayar.setObjectName(u"lblTanggalBayar")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblTanggalBayar)

        self.dateTanggalBayar = QDateEdit(FormPembayaran)
        self.dateTanggalBayar.setObjectName(u"dateTanggalBayar")
        self.dateTanggalBayar.setCalendarPopup(True)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.dateTanggalBayar)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(FormPembayaran)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(FormPembayaran)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(FormPembayaran)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(FormPembayaran)
        self.btnBersih.setObjectName(u"btnBersih")

        self.buttonLayout.addWidget(self.btnBersih)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.editCari = QLineEdit(FormPembayaran)
        self.editCari.setObjectName(u"editCari")

        self.verticalLayout.addWidget(self.editCari)

        self.tablePembayaran = QTableWidget(FormPembayaran)
        if (self.tablePembayaran.columnCount() < 6):
            self.tablePembayaran.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablePembayaran.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablePembayaran.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablePembayaran.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablePembayaran.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablePembayaran.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablePembayaran.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tablePembayaran.setObjectName(u"tablePembayaran")
        self.tablePembayaran.setColumnCount(6)

        self.verticalLayout.addWidget(self.tablePembayaran)


        self.retranslateUi(FormPembayaran)

        QMetaObject.connectSlotsByName(FormPembayaran)
    # setupUi

    def retranslateUi(self, FormPembayaran):
        FormPembayaran.setWindowTitle(QCoreApplication.translate("FormPembayaran", u"Data Pembayaran", None))
        self.lblJudul.setText(QCoreApplication.translate("FormPembayaran", u"Form Input Pembayaran", None))
        self.lblPembayaranID.setText(QCoreApplication.translate("FormPembayaran", u"ID Pembayaran", None))
        self.lblPengirimanID.setText(QCoreApplication.translate("FormPembayaran", u"ID Pengiriman", None))
        self.lblMetode.setText(QCoreApplication.translate("FormPembayaran", u"Metode Pembayaran", None))
        self.comboMetode.setItemText(0, QCoreApplication.translate("FormPembayaran", u"transfer", None))
        self.comboMetode.setItemText(1, QCoreApplication.translate("FormPembayaran", u"cod", None))
        self.comboMetode.setItemText(2, QCoreApplication.translate("FormPembayaran", u"ewallet", None))

        self.lblJumlah.setText(QCoreApplication.translate("FormPembayaran", u"Jumlah (Rp)", None))
        self.lblStatus.setText(QCoreApplication.translate("FormPembayaran", u"Status Pembayaran", None))
        self.comboStatus.setItemText(0, QCoreApplication.translate("FormPembayaran", u"belum", None))
        self.comboStatus.setItemText(1, QCoreApplication.translate("FormPembayaran", u"sudah", None))

        self.lblTanggalBayar.setText(QCoreApplication.translate("FormPembayaran", u"Tanggal Bayar", None))
        self.dateTanggalBayar.setDisplayFormat(QCoreApplication.translate("FormPembayaran", u"yyyy-MM-dd", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormPembayaran", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormPembayaran", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormPembayaran", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("FormPembayaran", u"Bersih", None))
        ___qtablewidgetitem = self.tablePembayaran.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormPembayaran", u"ID Pembayaran", None));
        ___qtablewidgetitem1 = self.tablePembayaran.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormPembayaran", u"ID Pengiriman", None));
        ___qtablewidgetitem2 = self.tablePembayaran.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormPembayaran", u"Metode", None));
        ___qtablewidgetitem3 = self.tablePembayaran.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormPembayaran", u"Jumlah", None));
        ___qtablewidgetitem4 = self.tablePembayaran.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormPembayaran", u"Status", None));
        ___qtablewidgetitem5 = self.tablePembayaran.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormPembayaran", u"Tanggal Bayar", None));
    # retranslateUi

