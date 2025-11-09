# This Python file uses the following encoding: utf-8
import sys
from datetime import date, datetime
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crudDB import my_cruddb

class tracking(QWidget):
    def __init__(self):
        super().__init__()
        # Load UI
        loader = QUiLoader()
        file = QFile("tracking.ui")
        if not file.exists():
            QMessageBox.critical(self, "Error", "File tracking.ui tidak ditemukan!")
            sys.exit(-1)
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

        # Set combo status
        self.ui.cmbStatus.clear()
        self.ui.cmbStatus.addItems(["dikemas", "dikirim", "selesai", "gagal"])

        # Tombol
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnCari.clicked.connect(self.cari)
        self.ui.btnBersih.clicked.connect(self.bersih)

        # Inisialisasi CRUD
        self.crud = my_cruddb()

        # Tampilkan data awal
        self.load_data()

    def load_data(self):
        data = self.crud.tampilTracking()
        table = self.ui.tableTracking
        table.setRowCount(0)
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels([
            "tracking_id", "pengiriman_id", "kurir_id", "status", "lokasi", "waktu_update"
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
            tanggal = self.ui.dateTimeUpdate.date().toString("yyyy-MM-dd")
            self.crud.simpanTracking(
                self.ui.txtTrackingID.text(),
                self.ui.txtPengirimanID.text(),
                self.ui.txtKurirID.text(),
                self.ui.cmbStatus.currentText(),
                self.ui.txtLokasi.text(),
                tanggal
            )
            QMessageBox.information(self, "Sukses", "Data berhasil disimpan")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def ubah(self):
        try:
            tanggal = self.ui.dateTimeUpdate.date().toString("yyyy-MM-dd")
            self.crud.ubahTracking(
                self.ui.txtTrackingID.text(),
                self.ui.txtPengirimanID.text(),
                self.ui.txtKurirID.text(),
                self.ui.cmbStatus.currentText(),
                self.ui.txtLokasi.text(),
                tanggal
            )
            QMessageBox.information(self, "Sukses", "Data berhasil diubah")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def hapus(self):
        try:
            self.crud.hapusTracking(self.ui.txtTrackingID.text())
            QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def cari(self):
        keyword = self.ui.txtTrackingID.text()
        if not keyword:
            self.load_data()
            return

        data = self.crud.cariTrackingMulti(keyword)
        table = self.ui.tableTracking
        table.setRowCount(0)

        if not data:
            QMessageBox.information(self, "Info", "Data tidak ditemukan.")
            return

        # Update table
        for row_index, row_data in enumerate(data):
            table.insertRow(row_index)
            for col_index, key in enumerate(row_data.keys()):
                value = row_data[key]
                if isinstance(value, datetime):
                    value = value.date()
                if isinstance(value, date):
                    value = value.strftime("%Y-%m-%d")
                table.setItem(row_index, col_index, QTableWidgetItem(str(value)))

        # Update field input dengan data pertama hasil pencarian
        first = data[0]
        self.ui.txtTrackingID.setText(str(first["tracking_id"]))
        self.ui.txtPengirimanID.setText(str(first["pengiriman_id"]))
        self.ui.txtKurirID.setText(str(first["kurir_id"]))
        self.ui.txtLokasi.setText(str(first["lokasi"]))
        self.ui.cmbStatus.setCurrentText(str(first["status"]))

        # Set tanggal
        tanggal = first["waktu_update"]
        if isinstance(tanggal, datetime):
            tanggal = tanggal.date()
        if isinstance(tanggal, date):
            self.ui.dateTimeUpdate.setDate(QDate(tanggal.year, tanggal.month, tanggal.day))
        else:
            self.ui.dateTimeUpdate.setDate(QDate.currentDate())

    def bersih(self):
        self.ui.txtTrackingID.clear()
        self.ui.txtPengirimanID.clear()
        self.ui.txtKurirID.clear()
        self.ui.txtLokasi.clear()
        self.ui.cmbStatus.setCurrentIndex(0)
        self.ui.dateTimeUpdate.setDate(QDate.currentDate())
        self.load_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = tracking()
    window.show()
    sys.exit(app.exec())
