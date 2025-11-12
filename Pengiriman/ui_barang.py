# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barang.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_FormBarang(object):
    def setupUi(self, FormBarang):
        if not FormBarang.objectName():
            FormBarang.setObjectName(u"FormBarang")
        FormBarang.resize(600, 520)
        self.verticalLayout = QVBoxLayout(FormBarang)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblJudul = QLabel(FormBarang)
        self.lblJudul.setObjectName(u"lblJudul")
        self.lblJudul.setStyleSheet(u"font-size:18px; font-weight:bold; color:#2b5fab;")
        self.lblJudul.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblJudul)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblBarangID = QLabel(FormBarang)
        self.lblBarangID.setObjectName(u"lblBarangID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblBarangID)

        self.txtBarangID = QLineEdit(FormBarang)
        self.txtBarangID.setObjectName(u"txtBarangID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtBarangID)

        self.lblUserID = QLabel(FormBarang)
        self.lblUserID.setObjectName(u"lblUserID")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblUserID)

        self.txtUserID = QLineEdit(FormBarang)
        self.txtUserID.setObjectName(u"txtUserID")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtUserID)

        self.lblNamaBarang = QLabel(FormBarang)
        self.lblNamaBarang.setObjectName(u"lblNamaBarang")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblNamaBarang)

        self.txtNamaBarang = QLineEdit(FormBarang)
        self.txtNamaBarang.setObjectName(u"txtNamaBarang")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtNamaBarang)

        self.lblBerat = QLabel(FormBarang)
        self.lblBerat.setObjectName(u"lblBerat")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblBerat)

        self.txtBerat = QLineEdit(FormBarang)
        self.txtBerat.setObjectName(u"txtBerat")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtBerat)

        self.lblDeskripsi = QLabel(FormBarang)
        self.lblDeskripsi.setObjectName(u"lblDeskripsi")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblDeskripsi)

        self.txtDeskripsi = QLineEdit(FormBarang)
        self.txtDeskripsi.setObjectName(u"txtDeskripsi")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtDeskripsi)

        self.lblTanggal = QLabel(FormBarang)
        self.lblTanggal.setObjectName(u"lblTanggal")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblTanggal)

        self.dateTanggalInput = QDateEdit(FormBarang)
        self.dateTanggalInput.setObjectName(u"dateTanggalInput")
        self.dateTanggalInput.setCalendarPopup(True)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.dateTanggalInput)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(FormBarang)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(FormBarang)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(FormBarang)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(FormBarang)
        self.btnBersih.setObjectName(u"btnBersih")

        self.buttonLayout.addWidget(self.btnBersih)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.editCari = QLineEdit(FormBarang)
        self.editCari.setObjectName(u"editCari")

        self.verticalLayout.addWidget(self.editCari)

        self.tableBarang = QTableWidget(FormBarang)
        if (self.tableBarang.columnCount() < 6):
            self.tableBarang.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableBarang.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableBarang.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableBarang.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableBarang.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableBarang.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableBarang.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableBarang.setObjectName(u"tableBarang")
        self.tableBarang.setColumnCount(6)

        self.verticalLayout.addWidget(self.tableBarang)


        self.retranslateUi(FormBarang)

        QMetaObject.connectSlotsByName(FormBarang)
    # setupUi

    def retranslateUi(self, FormBarang):
        FormBarang.setWindowTitle(QCoreApplication.translate("FormBarang", u"Data Barang", None))
        self.lblJudul.setText(QCoreApplication.translate("FormBarang", u"Form Input Barang", None))
        self.lblBarangID.setText(QCoreApplication.translate("FormBarang", u"ID Barang", None))
        self.lblUserID.setText(QCoreApplication.translate("FormBarang", u"User ID", None))
        self.lblNamaBarang.setText(QCoreApplication.translate("FormBarang", u"Nama Barang", None))
        self.lblBerat.setText(QCoreApplication.translate("FormBarang", u"Berat (gram/kg)", None))
        self.lblDeskripsi.setText(QCoreApplication.translate("FormBarang", u"Deskripsi", None))
        self.lblTanggal.setText(QCoreApplication.translate("FormBarang", u"Tanggal Input", None))
        self.dateTanggalInput.setDisplayFormat(QCoreApplication.translate("FormBarang", u"yyyy-MM-dd", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormBarang", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormBarang", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormBarang", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("FormBarang", u"Bersih", None))
        ___qtablewidgetitem = self.tableBarang.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormBarang", u"ID Barang", None));
        ___qtablewidgetitem1 = self.tableBarang.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormBarang", u"User ID", None));
        ___qtablewidgetitem2 = self.tableBarang.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormBarang", u"Nama Barang", None));
        ___qtablewidgetitem3 = self.tableBarang.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormBarang", u"Berat", None));
        ___qtablewidgetitem4 = self.tableBarang.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormBarang", u"Deskripsi", None));
        ___qtablewidgetitem5 = self.tableBarang.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormBarang", u"Tanggal Input", None));
    # retranslateUi

