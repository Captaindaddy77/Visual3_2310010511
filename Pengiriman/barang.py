# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crudDB import my_cruddb


class barang(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Pastikan path file UI benar
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "barang.ui")

        file_ui = QFile(ui_path)
        if not file_ui.exists():
            print(f"File UI tidak ditemukan: {ui_path}")
        file_ui.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.formBarang = loader.load(file_ui, self)
        file_ui.close()

        # Inisialisasi koneksi ke database
        self.crud = my_cruddb()

        # Koneksi tombol ke fungsi
        self.formBarang.btnSimpan.clicked.connect(self.doSimpan)
        self.formBarang.btnUbah.clicked.connect(self.doUbah)
        self.formBarang.btnHapus.clicked.connect(self.doHapus)
        self.formBarang.btnCari.clicked.connect(self.doCari)
        self.formBarang.btnBersih.clicked.connect(self.doBersih)

        # Tampilkan data awal di tabel
        self.tampilData()

        # Klik baris tabel untuk isi form
        self.formBarang.tableBarang.cellClicked.connect(self.isiDariTabel)

    # -------------------- FUNGSI CRUD -------------------- #
    def doSimpan(self):
        barang_id = self.formBarang.txtBarangID.text()
        user_id = self.formBarang.txtUserID.text()
        nama_barang = self.formBarang.txtNamaBarang.text()
        berat = self.formBarang.txtBerat.text()
        deskripsi = self.formBarang.txtDeskripsi.text()
        tanggal_input = self.formBarang.dateTanggalInput.date().toString("yyyy-MM-dd")

        self.crud.simpanBarang(barang_id, user_id, nama_barang, berat, deskripsi, tanggal_input)
        self.tampilData()
        print("Data barang berhasil disimpan")

    def doUbah(self):
        barang_id = self.formBarang.txtBarangID.text()
        user_id = self.formBarang.txtUserID.text()
        nama_barang = self.formBarang.txtNamaBarang.text()
        berat = self.formBarang.txtBerat.text()
        deskripsi = self.formBarang.txtDeskripsi.text()
        tanggal_input = self.formBarang.dateTanggalInput.date().toString("yyyy-MM-dd")

        self.crud.ubahBarang(barang_id, user_id, nama_barang, berat, deskripsi, tanggal_input)
        self.tampilData()
        print("Data barang berhasil diubah")

    def doHapus(self):
        barang_id = self.formBarang.txtBarangID.text()
        self.crud.hapusBarang(barang_id)
        self.tampilData()
        print("Data barang berhasil dihapus")

    def doCari(self):
        barang_id = self.formBarang.txtBarangID.text()
        data = self.crud.cariBarang(barang_id)
        if data:
            self.formBarang.txtUserID.setText(str(data["user_id"]))
            self.formBarang.txtNamaBarang.setText(data["nama_barang"])
            self.formBarang.txtBerat.setText(str(data["berat"]))
            self.formBarang.txtDeskripsi.setText(data["deskripsi"])
            date = QDate.fromString(str(data["tanggal_input"]), "yyyy-MM-dd")
            self.formBarang.dateTanggalInput.setDate(date)
        else:
            print("Data tidak ditemukan")

    def doBersih(self):
        self.formBarang.txtBarangID.clear()
        self.formBarang.txtUserID.clear()
        self.formBarang.txtNamaBarang.clear()
        self.formBarang.txtBerat.clear()
        self.formBarang.txtDeskripsi.clear()
        self.tampilData()

    # -------------------- TAMPIL DATA -------------------- #
    def tampilData(self):
        cursor = self.crud.conn.cursor()
        cursor.execute("SELECT * FROM barang")
        hasil = cursor.fetchall()
        cursor.close()

        self.formBarang.tableBarang.setRowCount(len(hasil))
        self.formBarang.tableBarang.setColumnCount(6)
        self.formBarang.tableBarang.setHorizontalHeaderLabels([
            "ID Barang", "User ID", "Nama Barang", "Berat", "Deskripsi", "Tanggal Input"
        ])

        for i, row in enumerate(hasil):
            for j, val in enumerate(row):
                # Hilangkan waktu jika ada format datetime
                if j == 5 and isinstance(val, str) and " " in val:
                    val = val.split(" ")[0]
                self.formBarang.tableBarang.setItem(i, j, QTableWidgetItem(str(val)))

        self.formBarang.tableBarang.resizeColumnsToContents()

    # -------------------- ISI FORM DARI TABEL -------------------- #
    def isiDariTabel(self, row, column):
        self.formBarang.txtBarangID.setText(self.formBarang.tableBarang.item(row, 0).text())
        self.formBarang.txtUserID.setText(self.formBarang.tableBarang.item(row, 1).text())
        self.formBarang.txtNamaBarang.setText(self.formBarang.tableBarang.item(row, 2).text())
        self.formBarang.txtBerat.setText(self.formBarang.tableBarang.item(row, 3).text())
        self.formBarang.txtDeskripsi.setText(self.formBarang.tableBarang.item(row, 4).text())

        date_text = self.formBarang.tableBarang.item(row, 5).text()
        date = QDate.fromString(date_text, "yyyy-MM-dd")
        self.formBarang.dateTanggalInput.setDate(date)


# -------------------- MAIN PROGRAM -------------------- #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = barang()
    window.formBarang.show()
    sys.exit(app.exec())
