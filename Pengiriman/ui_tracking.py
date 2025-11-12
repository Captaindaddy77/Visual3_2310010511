# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tracking.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_FormTracking(object):
    def setupUi(self, FormTracking):
        if not FormTracking.objectName():
            FormTracking.setObjectName(u"FormTracking")
        FormTracking.resize(700, 500)
        self.verticalLayout = QVBoxLayout(FormTracking)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblJudul = QLabel(FormTracking)
        self.lblJudul.setObjectName(u"lblJudul")
        self.lblJudul.setStyleSheet(u"font-size:18px; font-weight:bold; color:#2b5fab;")
        self.lblJudul.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblJudul)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblTrackingID = QLabel(FormTracking)
        self.lblTrackingID.setObjectName(u"lblTrackingID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblTrackingID)

        self.txtTrackingID = QLineEdit(FormTracking)
        self.txtTrackingID.setObjectName(u"txtTrackingID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtTrackingID)

        self.lblPengirimanID = QLabel(FormTracking)
        self.lblPengirimanID.setObjectName(u"lblPengirimanID")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblPengirimanID)

        self.txtPengirimanID = QLineEdit(FormTracking)
        self.txtPengirimanID.setObjectName(u"txtPengirimanID")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtPengirimanID)

        self.lblKurirID = QLabel(FormTracking)
        self.lblKurirID.setObjectName(u"lblKurirID")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblKurirID)

        self.txtKurirID = QLineEdit(FormTracking)
        self.txtKurirID.setObjectName(u"txtKurirID")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtKurirID)

        self.lblStatus = QLabel(FormTracking)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.cmbStatus = QComboBox(FormTracking)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbStatus)

        self.lblLokasi = QLabel(FormTracking)
        self.lblLokasi.setObjectName(u"lblLokasi")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblLokasi)

        self.txtLokasi = QLineEdit(FormTracking)
        self.txtLokasi.setObjectName(u"txtLokasi")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtLokasi)

        self.lblWaktuUpdate = QLabel(FormTracking)
        self.lblWaktuUpdate.setObjectName(u"lblWaktuUpdate")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblWaktuUpdate)

        self.dateTimeUpdate = QDateTimeEdit(FormTracking)
        self.dateTimeUpdate.setObjectName(u"dateTimeUpdate")
        self.dateTimeUpdate.setCalendarPopup(True)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.dateTimeUpdate)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(FormTracking)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(FormTracking)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(FormTracking)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(FormTracking)
        self.btnBersih.setObjectName(u"btnBersih")

        self.buttonLayout.addWidget(self.btnBersih)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.editCari = QLineEdit(FormTracking)
        self.editCari.setObjectName(u"editCari")

        self.verticalLayout.addWidget(self.editCari)

        self.tableTracking = QTableWidget(FormTracking)
        if (self.tableTracking.columnCount() < 6):
            self.tableTracking.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableTracking.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableTracking.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableTracking.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableTracking.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableTracking.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableTracking.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableTracking.setObjectName(u"tableTracking")
        self.tableTracking.setColumnCount(6)

        self.verticalLayout.addWidget(self.tableTracking)


        self.retranslateUi(FormTracking)

        QMetaObject.connectSlotsByName(FormTracking)
    # setupUi

    def retranslateUi(self, FormTracking):
        FormTracking.setWindowTitle(QCoreApplication.translate("FormTracking", u"Form Tracking", None))
        self.lblJudul.setText(QCoreApplication.translate("FormTracking", u"Form Input Tracking", None))
        self.lblTrackingID.setText(QCoreApplication.translate("FormTracking", u"ID Tracking", None))
        self.lblPengirimanID.setText(QCoreApplication.translate("FormTracking", u"ID Pengiriman", None))
        self.lblKurirID.setText(QCoreApplication.translate("FormTracking", u"ID Kurir", None))
        self.lblStatus.setText(QCoreApplication.translate("FormTracking", u"Status", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("FormTracking", u"dikemas", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("FormTracking", u"dikirim", None))
        self.cmbStatus.setItemText(2, QCoreApplication.translate("FormTracking", u"selesai", None))
        self.cmbStatus.setItemText(3, QCoreApplication.translate("FormTracking", u"gagal", None))

        self.lblLokasi.setText(QCoreApplication.translate("FormTracking", u"Lokasi", None))
        self.lblWaktuUpdate.setText(QCoreApplication.translate("FormTracking", u"Waktu Update", None))
        self.dateTimeUpdate.setDisplayFormat(QCoreApplication.translate("FormTracking", u"yyyy-MM-dd HH:mm:ss", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormTracking", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormTracking", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormTracking", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("FormTracking", u"Bersih", None))
        ___qtablewidgetitem = self.tableTracking.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormTracking", u"ID Tracking", None));
        ___qtablewidgetitem1 = self.tableTracking.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormTracking", u"ID Pengiriman", None));
        ___qtablewidgetitem2 = self.tableTracking.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormTracking", u"ID Kurir", None));
        ___qtablewidgetitem3 = self.tableTracking.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormTracking", u"Status", None));
        ___qtablewidgetitem4 = self.tableTracking.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormTracking", u"Lokasi", None));
        ___qtablewidgetitem5 = self.tableTracking.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormTracking", u"Waktu Update", None));
    # retranslateUi

