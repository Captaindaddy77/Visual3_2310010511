# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class pembayaran(QWidget):
    def __init__(self):
        super().__init__()
        fileform = QFile("pembayaran.ui")
        fileform.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(fileform, self)
        self.setLayout(self.form.layout())
        fileform.close()

        self.db = my_cruddb()

        # Tombol
        self.form.btnSimpan.clicked.connect(self.simpan)
        self.form.btnUbah.clicked.connect(self.ubah)
        self.form.btnHapus.clicked.connect(self.hapus)
        self.form.btnCari.clicked.connect(self.cari)
        self.form.btnBersih.clicked.connect(self.bersih)

        # Tampilkan data awal
        self.tampil_data()

    def tampil_data(self):
        data = self.db.tampilPembayaran()
        self.form.tablePembayaran.setRowCount(len(data))
        for i, row in enumerate(data):
            self.form.tablePembayaran.setItem(i, 0, QTableWidgetItem(str(row['pembayaran_id'])))
            self.form.tablePembayaran.setItem(i, 1, QTableWidgetItem(str(row['pengiriman_id'])))
            self.form.tablePembayaran.setItem(i, 2, QTableWidgetItem(row['metode']))
            self.form.tablePembayaran.setItem(i, 3, QTableWidgetItem(str(row['jumlah'])))
            self.form.tablePembayaran.setItem(i, 4, QTableWidgetItem(row['status_bayar']))
            self.form.tablePembayaran.setItem(i, 5, QTableWidgetItem(str(row['tanggal_bayar'])))

    def simpan(self):
        try:
            pembayaran_id = self.form.txtPembayaranID.text()
            pengiriman_id = self.form.txtPengirimanID.text()
            metode = self.form.comboMetode.currentText()
            jumlah = self.form.txtJumlah.text()
            status_bayar = self.form.comboStatus.currentText()
            tanggal_bayar = self.form.dateTanggalBayar.text()

            self.db.simpanPembayaran(pembayaran_id, pengiriman_id, metode, jumlah, status_bayar, tanggal_bayar)
            QMessageBox.information(self, "Sukses", "Data pembayaran berhasil disimpan!")
            self.tampil_data()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def ubah(self):
        try:
            pembayaran_id = self.form.txtPembayaranID.text()
            pengiriman_id = self.form.txtPengirimanID.text()
            metode = self.form.comboMetode.currentText()
            jumlah = self.form.txtJumlah.text()
            status_bayar = self.form.comboStatus.currentText()
            tanggal_bayar = self.form.dateTanggalBayar.text()

            self.db.ubahPembayaran(pembayaran_id, pengiriman_id, metode, jumlah, status_bayar, tanggal_bayar)
            QMessageBox.information(self, "Sukses", "Data pembayaran berhasil diubah!")
            self.tampil_data()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def hapus(self):
        try:
            pembayaran_id = self.form.txtPembayaranID.text()
            self.db.hapusPembayaran(pembayaran_id)
            QMessageBox.information(self, "Sukses", "Data pembayaran berhasil dihapus!")
            self.tampil_data()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def cari(self):
        try:
            pembayaran_id = self.form.txtPembayaranID.text()
            data = self.db.cariPembayaran(pembayaran_id)
            if data:
                self.form.txtPengirimanID.setText(str(data['pengiriman_id']))
                self.form.txtJumlah.setText(str(data['jumlah']))
                self.form.comboMetode.setCurrentText(data['metode'])
                self.form.comboStatus.setCurrentText(data['status_bayar'])
                self.form.dateTanggalBayar.setDate(data['tanggal_bayar'])
            else:
                QMessageBox.information(self, "Info", "Data tidak ditemukan.")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def bersih(self):
        self.form.txtPembayaranID.clear()
        self.form.txtPengirimanID.clear()
        self.form.txtJumlah.clear()
        self.form.comboMetode.setCurrentIndex(0)
        self.form.comboStatus.setCurrentIndex(0)
        self.tampil_data()
