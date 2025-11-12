# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kurir.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_FormKurir(object):
    def setupUi(self, FormKurir):
        if not FormKurir.objectName():
            FormKurir.setObjectName(u"FormKurir")
        FormKurir.resize(600, 520)
        self.verticalLayout = QVBoxLayout(FormKurir)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblJudul = QLabel(FormKurir)
        self.lblJudul.setObjectName(u"lblJudul")
        self.lblJudul.setStyleSheet(u"font-size:18px; font-weight:bold; color:#2b5fab;")
        self.lblJudul.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblJudul)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblKurirID = QLabel(FormKurir)
        self.lblKurirID.setObjectName(u"lblKurirID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblKurirID)

        self.txtKurirID = QLineEdit(FormKurir)
        self.txtKurirID.setObjectName(u"txtKurirID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtKurirID)

        self.lblNamaKurir = QLabel(FormKurir)
        self.lblNamaKurir.setObjectName(u"lblNamaKurir")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblNamaKurir)

        self.txtNamaKurir = QLineEdit(FormKurir)
        self.txtNamaKurir.setObjectName(u"txtNamaKurir")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtNamaKurir)

        self.lblNoHP = QLabel(FormKurir)
        self.lblNoHP.setObjectName(u"lblNoHP")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblNoHP)

        self.txtNoHP = QLineEdit(FormKurir)
        self.txtNoHP.setObjectName(u"txtNoHP")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtNoHP)

        self.lblEmail = QLabel(FormKurir)
        self.lblEmail.setObjectName(u"lblEmail")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblEmail)

        self.txtEmail = QLineEdit(FormKurir)
        self.txtEmail.setObjectName(u"txtEmail")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtEmail)

        self.lblPlatNomor = QLabel(FormKurir)
        self.lblPlatNomor.setObjectName(u"lblPlatNomor")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblPlatNomor)

        self.txtPlatNomor = QLineEdit(FormKurir)
        self.txtPlatNomor.setObjectName(u"txtPlatNomor")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtPlatNomor)

        self.lblStatus = QLabel(FormKurir)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.cmbStatus = QComboBox(FormKurir)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cmbStatus)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(FormKurir)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(FormKurir)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(FormKurir)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(FormKurir)
        self.btnBersih.setObjectName(u"btnBersih")

        self.buttonLayout.addWidget(self.btnBersih)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.editCari = QLineEdit(FormKurir)
        self.editCari.setObjectName(u"editCari")

        self.verticalLayout.addWidget(self.editCari)

        self.tableKurir = QTableWidget(FormKurir)
        if (self.tableKurir.columnCount() < 6):
            self.tableKurir.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableKurir.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableKurir.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableKurir.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableKurir.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableKurir.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableKurir.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableKurir.setObjectName(u"tableKurir")
        self.tableKurir.setColumnCount(6)

        self.verticalLayout.addWidget(self.tableKurir)


        self.retranslateUi(FormKurir)

        QMetaObject.connectSlotsByName(FormKurir)
    # setupUi

    def retranslateUi(self, FormKurir):
        FormKurir.setWindowTitle(QCoreApplication.translate("FormKurir", u"Data Kurir", None))
        self.lblJudul.setText(QCoreApplication.translate("FormKurir", u"Form Input Kurir", None))
        self.lblKurirID.setText(QCoreApplication.translate("FormKurir", u"ID Kurir", None))
        self.lblNamaKurir.setText(QCoreApplication.translate("FormKurir", u"Nama Kurir", None))
        self.lblNoHP.setText(QCoreApplication.translate("FormKurir", u"No. HP", None))
        self.lblEmail.setText(QCoreApplication.translate("FormKurir", u"Email", None))
        self.lblPlatNomor.setText(QCoreApplication.translate("FormKurir", u"Plat Nomor", None))
        self.lblStatus.setText(QCoreApplication.translate("FormKurir", u"Status", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("FormKurir", u"aktif", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("FormKurir", u"nonaktif", None))

        self.btnSimpan.setText(QCoreApplication.translate("FormKurir", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormKurir", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormKurir", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("FormKurir", u"Bersih", None))
        ___qtablewidgetitem = self.tableKurir.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormKurir", u"ID Kurir", None));
        ___qtablewidgetitem1 = self.tableKurir.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormKurir", u"Nama Kurir", None));
        ___qtablewidgetitem2 = self.tableKurir.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormKurir", u"No. HP", None));
        ___qtablewidgetitem3 = self.tableKurir.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormKurir", u"Email", None));
        ___qtablewidgetitem4 = self.tableKurir.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormKurir", u"Plat Nomor", None));
        ___qtablewidgetitem5 = self.tableKurir.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormKurir", u"Status", None));
    # retranslateUi

