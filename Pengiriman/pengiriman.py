# This Python file uses the following encoding: utf-8
import sys
from datetime import date, datetime
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crudDB import my_cruddb

class pengiriman(QWidget):
    def __init__(self):
        super().__init__()
        # Load UI
        loader = QUiLoader()
        file = QFile("pengiriman.ui")
        if not file.exists():
            QMessageBox.critical(self, "Error", "File pengiriman.ui tidak ditemukan!")
            sys.exit(-1)
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

        # Inisialisasi CRUD
        self.crud = my_cruddb()

        # Set combo status
        self.ui.cmbStatus.clear()
        self.ui.cmbStatus.addItems(["diproses", "dikirim", "diterima"])

        # Tombol
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnCari.clicked.connect(self.cari)
        self.ui.btnBersih.clicked.connect(self.bersih)

        # Tampilkan data awal
        self.tampilData()

    def tampilData(self):
        data = self.crud.tampilPengiriman()
        table = self.ui.tablePengiriman
        table.setRowCount(0)
        table.setColumnCount(9)
        table.setHorizontalHeaderLabels([
            "pengiriman_id", "barang_id", "asal", "tujuan",
            "jarak_km", "biaya_kirim", "status", "tanggal_kirim", "tanggal_terima"
        ])

        for row_index, row_data in enumerate(data):
            table.insertRow(row_index)
            for col_index, key in enumerate(row_data.keys()):
                value = row_data[key]
                if isinstance(value, datetime):
                    value = value.date()
                if isinstance(value, date):
                    value = value.strftime("%Y-%m-%d")
                table.setItem(row_index, col_index, QTableWidgetItem(str(value)))

    def simpan(self):
        try:
            data = (
                self.ui.txtPengirimanID.text(),
                self.ui.txtBarangID.text(),
                self.ui.txtAsal.text(),
                self.ui.txtTujuan.text(),
                self.ui.txtJarak.text(),
                self.ui.txtBiaya.text(),
                self.ui.cmbStatus.currentText(),
                self.ui.txtTanggalKirim.date().toString("yyyy-MM-dd"),
                self.ui.txtTanggalTerima.date().toString("yyyy-MM-dd")
            )
            self.crud.simpanPengiriman(*data)
            QMessageBox.information(self, "Sukses", "Data pengiriman berhasil disimpan!")
            self.tampilData()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def ubah(self):
        try:
            data = (
                self.ui.txtPengirimanID.text(),
                self.ui.txtBarangID.text(),
                self.ui.txtAsal.text(),
                self.ui.txtTujuan.text(),
                self.ui.txtJarak.text(),
                self.ui.txtBiaya.text(),
                self.ui.cmbStatus.currentText(),
                self.ui.txtTanggalKirim.date().toString("yyyy-MM-dd"),
                self.ui.txtTanggalTerima.date().toString("yyyy-MM-dd")
            )
            self.crud.ubahPengiriman(*data)
            QMessageBox.information(self, "Sukses", "Data pengiriman berhasil diubah!")
            self.tampilData()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def hapus(self):
        try:
            pengiriman_id = self.ui.txtPengirimanID.text()
            self.crud.hapusPengiriman(pengiriman_id)
            QMessageBox.information(self, "Sukses", "Data pengiriman berhasil dihapus!")
            self.tampilData()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def cari(self):
        pengiriman_id = self.ui.txtPengirimanID.text()
        data = self.crud.cariPengiriman(pengiriman_id)
        if data:
            self.ui.txtBarangID.setText(str(data["barang_id"]))
            self.ui.txtAsal.setText(str(data["asal"]))
            self.ui.txtTujuan.setText(str(data["tujuan"]))
            self.ui.txtJarak.setText(str(data["jarak_km"]))
            self.ui.txtBiaya.setText(str(data["biaya_kirim"]))
            self.ui.cmbStatus.setCurrentText(str(data["status"]))

            # Perbaikan QDateEdit agar tanggal sesuai data
            for key, widget in [("tanggal_kirim", self.ui.txtTanggalKirim),
                                ("tanggal_terima", self.ui.txtTanggalTerima)]:
                value = data[key]
                if isinstance(value, datetime):
                    value = value.date()
                if isinstance(value, date):
                    widget.setDate(QDate(value.year, value.month, value.day))
                else:
                    widget.setDate(QDate.currentDate())
        else:
            QMessageBox.information(self, "Info", "Data tidak ditemukan.")

    def bersih(self):
        """Reset semua field input"""
        self.ui.txtPengirimanID.clear()
        self.ui.txtBarangID.clear()
        self.ui.txtAsal.clear()
        self.ui.txtTujuan.clear()
        self.ui.txtJarak.clear()
        self.ui.txtBiaya.clear()
        self.ui.cmbStatus.setCurrentIndex(0)
        self.ui.txtTanggalKirim.setDate(QDate.currentDate())
        self.ui.txtTanggalTerima.setDate(QDate.currentDate())
        self.tampilData()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = pengiriman()
    window.show()
    sys.exit(app.exec())
