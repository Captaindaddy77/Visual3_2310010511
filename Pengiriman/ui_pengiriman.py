# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pengiriman.ui'
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

class Ui_FormPengiriman(object):
    def setupUi(self, FormPengiriman):
        if not FormPengiriman.objectName():
            FormPengiriman.setObjectName(u"FormPengiriman")
        FormPengiriman.resize(700, 550)
        self.verticalLayout = QVBoxLayout(FormPengiriman)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblJudul = QLabel(FormPengiriman)
        self.lblJudul.setObjectName(u"lblJudul")
        self.lblJudul.setStyleSheet(u"font-size:18px; font-weight:bold; color:#2b5fab;")
        self.lblJudul.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblJudul)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblPengirimanID = QLabel(FormPengiriman)
        self.lblPengirimanID.setObjectName(u"lblPengirimanID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblPengirimanID)

        self.txtPengirimanID = QLineEdit(FormPengiriman)
        self.txtPengirimanID.setObjectName(u"txtPengirimanID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtPengirimanID)

        self.lblBarangID = QLabel(FormPengiriman)
        self.lblBarangID.setObjectName(u"lblBarangID")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblBarangID)

        self.txtBarangID = QLineEdit(FormPengiriman)
        self.txtBarangID.setObjectName(u"txtBarangID")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtBarangID)

        self.lblAsal = QLabel(FormPengiriman)
        self.lblAsal.setObjectName(u"lblAsal")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblAsal)

        self.txtAsal = QLineEdit(FormPengiriman)
        self.txtAsal.setObjectName(u"txtAsal")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtAsal)

        self.lblTujuan = QLabel(FormPengiriman)
        self.lblTujuan.setObjectName(u"lblTujuan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblTujuan)

        self.txtTujuan = QLineEdit(FormPengiriman)
        self.txtTujuan.setObjectName(u"txtTujuan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtTujuan)

        self.lblJarak = QLabel(FormPengiriman)
        self.lblJarak.setObjectName(u"lblJarak")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblJarak)

        self.txtJarak = QLineEdit(FormPengiriman)
        self.txtJarak.setObjectName(u"txtJarak")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtJarak)

        self.lblBiaya = QLabel(FormPengiriman)
        self.lblBiaya.setObjectName(u"lblBiaya")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblBiaya)

        self.txtBiaya = QLineEdit(FormPengiriman)
        self.txtBiaya.setObjectName(u"txtBiaya")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.txtBiaya)

        self.lblStatus = QLabel(FormPengiriman)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.cmbStatus = QComboBox(FormPengiriman)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.cmbStatus)

        self.lblTanggalKirim = QLabel(FormPengiriman)
        self.lblTanggalKirim.setObjectName(u"lblTanggalKirim")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lblTanggalKirim)

        self.txtTanggalKirim = QDateEdit(FormPengiriman)
        self.txtTanggalKirim.setObjectName(u"txtTanggalKirim")
        self.txtTanggalKirim.setCalendarPopup(True)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.txtTanggalKirim)

        self.lblTanggalTerima = QLabel(FormPengiriman)
        self.lblTanggalTerima.setObjectName(u"lblTanggalTerima")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.lblTanggalTerima)

        self.txtTanggalTerima = QDateEdit(FormPengiriman)
        self.txtTanggalTerima.setObjectName(u"txtTanggalTerima")
        self.txtTanggalTerima.setCalendarPopup(True)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.txtTanggalTerima)


        self.verticalLayout.addLayout(self.formLayout)

        self.editCari = QLineEdit(FormPengiriman)
        self.editCari.setObjectName(u"editCari")

        self.verticalLayout.addWidget(self.editCari)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(FormPengiriman)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(FormPengiriman)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(FormPengiriman)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(FormPengiriman)
        self.btnBersih.setObjectName(u"btnBersih")

        self.buttonLayout.addWidget(self.btnBersih)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.tablePengiriman = QTableWidget(FormPengiriman)
        if (self.tablePengiriman.columnCount() < 9):
            self.tablePengiriman.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablePengiriman.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablePengiriman.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablePengiriman.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablePengiriman.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablePengiriman.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablePengiriman.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablePengiriman.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablePengiriman.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablePengiriman.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tablePengiriman.setObjectName(u"tablePengiriman")
        self.tablePengiriman.setColumnCount(9)

        self.verticalLayout.addWidget(self.tablePengiriman)


        self.retranslateUi(FormPengiriman)

        QMetaObject.connectSlotsByName(FormPengiriman)
    # setupUi

    def retranslateUi(self, FormPengiriman):
        FormPengiriman.setWindowTitle(QCoreApplication.translate("FormPengiriman", u"Data Pengiriman", None))
        self.lblJudul.setText(QCoreApplication.translate("FormPengiriman", u"Form Input Pengiriman", None))
        self.lblPengirimanID.setText(QCoreApplication.translate("FormPengiriman", u"ID Pengiriman", None))
        self.lblBarangID.setText(QCoreApplication.translate("FormPengiriman", u"ID Barang", None))
        self.lblAsal.setText(QCoreApplication.translate("FormPengiriman", u"Asal", None))
        self.lblTujuan.setText(QCoreApplication.translate("FormPengiriman", u"Tujuan", None))
        self.lblJarak.setText(QCoreApplication.translate("FormPengiriman", u"Jarak (km)", None))
        self.lblBiaya.setText(QCoreApplication.translate("FormPengiriman", u"Biaya Kirim (Rp)", None))
        self.lblStatus.setText(QCoreApplication.translate("FormPengiriman", u"Status", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("FormPengiriman", u"diproses", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("FormPengiriman", u"dikirim", None))
        self.cmbStatus.setItemText(2, QCoreApplication.translate("FormPengiriman", u"diterima", None))

#if QT_CONFIG(tooltip)
        self.cmbStatus.setToolTip(QCoreApplication.translate("FormPengiriman", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lblTanggalKirim.setText(QCoreApplication.translate("FormPengiriman", u"Tanggal Kirim", None))
        self.txtTanggalKirim.setDisplayFormat(QCoreApplication.translate("FormPengiriman", u"yyyy-MM-dd", None))
        self.lblTanggalTerima.setText(QCoreApplication.translate("FormPengiriman", u"Tanggal Terima", None))
        self.txtTanggalTerima.setDisplayFormat(QCoreApplication.translate("FormPengiriman", u"yyyy-MM-dd", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormPengiriman", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormPengiriman", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormPengiriman", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("FormPengiriman", u"Bersih", None))
        ___qtablewidgetitem = self.tablePengiriman.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormPengiriman", u"ID Pengiriman", None));
        ___qtablewidgetitem1 = self.tablePengiriman.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormPengiriman", u"ID Barang", None));
        ___qtablewidgetitem2 = self.tablePengiriman.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormPengiriman", u"Asal", None));
        ___qtablewidgetitem3 = self.tablePengiriman.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormPengiriman", u"Tujuan", None));
        ___qtablewidgetitem4 = self.tablePengiriman.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormPengiriman", u"Jarak (km)", None));
        ___qtablewidgetitem5 = self.tablePengiriman.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormPengiriman", u"Biaya (Rp)", None));
        ___qtablewidgetitem6 = self.tablePengiriman.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("FormPengiriman", u"Status", None));
        ___qtablewidgetitem7 = self.tablePengiriman.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("FormPengiriman", u"Tanggal Kirim", None));
        ___qtablewidgetitem8 = self.tablePengiriman.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("FormPengiriman", u"Tanggal Terima", None));
    # retranslateUi

