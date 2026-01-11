# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crudDB import my_cruddb


class barang(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "barang.ui")

        file_ui = QFile(ui_path)
        if not file_ui.exists():
            QMessageBox.warning(None, "Peringatan", f"File UI tidak ditemukan:\n{ui_path}")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formBarang = loader.load(file_ui, self)
        file_ui.close()

        self.crud = my_cruddb()

        # Tombol CRUD
        self.formBarang.btnSimpan.clicked.connect(self.doSimpanBarang)
        self.formBarang.btnUbah.clicked.connect(self.doUbahBarang)
        self.formBarang.btnHapus.clicked.connect(self.doHapusBarang)
        self.formBarang.btnBersih.clicked.connect(self.doBersihBarang)
        self.formBarang.editCari.textChanged.connect(self.doCariBarang)

        # Isi tabel di awal
        self.tampilData()

    # -------------------- SIMPAN -------------------- #
    def doSimpanBarang(self):
        barang_id = self.formBarang.txtBarangID.text().strip()
        user_id = self.formBarang.txtUserID.text().strip()
        nama = self.formBarang.txtNamaBarang.text().strip()
        berat = self.formBarang.txtBerat.text().strip()
        desk = self.formBarang.txtDeskripsi.text().strip()
        tanggal = self.formBarang.dateTanggalInput.date().toString("yyyy-MM-dd")

        # Validasi form
        if not barang_id:
            QMessageBox.information(None, "Informasi", "ID Barang belum diisi")
            self.formBarang.txtBarangID.setFocus()
            return
        if not user_id:
            QMessageBox.information(None, "Informasi", "User ID belum diisi")
            self.formBarang.txtUserID.setFocus()
            return
        if not nama:
            QMessageBox.information(None, "Informasi", "Nama Barang belum diisi")
            self.formBarang.txtNamaBarang.setFocus()
            return

        pesan = QMessageBox.question(
            None,
            "Konfirmasi",
            "Apakah Anda yakin ingin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No
        )
        if pesan == QMessageBox.Yes:
            self.crud.simpanBarang(barang_id, user_id, nama, berat, desk, tanggal)
            self.tampilData()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    # -------------------- UBAH -------------------- #
    def doUbahBarang(self):
        barang_id = self.formBarang.txtBarangID.text().strip()
        user_id = self.formBarang.txtUserID.text().strip()
        nama = self.formBarang.txtNamaBarang.text().strip()
        berat = self.formBarang.txtBerat.text().strip()
        desk = self.formBarang.txtDeskripsi.text().strip()
        tanggal = self.formBarang.dateTanggalInput.date().toString("yyyy-MM-dd")

        self.crud.ubahBarang(barang_id, user_id, nama, berat, desk, tanggal)
        self.tampilData()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    # -------------------- HAPUS -------------------- #
    def doHapusBarang(self):
        barang_id = self.formBarang.txtBarangID.text().strip()
        if not barang_id:
            QMessageBox.information(None, "Informasi", "Pilih data yang ingin dihapus")
            return

        pesan = QMessageBox.question(
            None,
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )
        if pesan == QMessageBox.Yes:
            self.crud.hapusBarang(barang_id)
            self.tampilData()
            QMessageBox.information(None, "Informasi", "Data berhasil dihapus")

    # -------------------- BERSIH -------------------- #
    def doBersihBarang(self):
        self.formBarang.txtBarangID.clear()
        self.formBarang.txtUserID.clear()
        self.formBarang.txtNamaBarang.clear()
        self.formBarang.txtBerat.clear()
        self.formBarang.txtDeskripsi.clear()
        self.formBarang.editCari.clear()
        self.tampilData()

    # -------------------- CARI -------------------- #
    def doCariBarang(self):
        keyword = self.formBarang.editCari.text().strip()
        hasil = self.crud.cariBarang(keyword)

        self.formBarang.tableBarang.setRowCount(0)
        for r in hasil:
            i = self.formBarang.tableBarang.rowCount()
            self.formBarang.tableBarang.insertRow(i)
            self.formBarang.tableBarang.setItem(i, 0, QTableWidgetItem(str(r["barang_id"])))
            self.formBarang.tableBarang.setItem(i, 1, QTableWidgetItem(str(r["user_id"])))
            self.formBarang.tableBarang.setItem(i, 2, QTableWidgetItem(r["nama_barang"]))
            self.formBarang.tableBarang.setItem(i, 3, QTableWidgetItem(str(r["berat"])))
            self.formBarang.tableBarang.setItem(i, 4, QTableWidgetItem(r["deskripsi"]))
            self.formBarang.tableBarang.setItem(i, 5, QTableWidgetItem(str(r["tanggal_input"])))

    # -------------------- AUTO ISI FORM -------------------- #
        if len(hasil) > 0:
            data = hasil[0]   # AMBIL DATA PERTAMA

            self.formBarang.txtBarangID.setText(str(data["barang_id"]))
            self.formBarang.txtUserID.setText(str(data["user_id"]))
            self.formBarang.txtNamaBarang.setText(data["nama_barang"])
            self.formBarang.txtBerat.setText(str(data["berat"]))
            self.formBarang.txtDeskripsi.setText(data["deskripsi"])
            self.formBarang.dateTanggalInput.setDate(
            QDate.fromString(str(data["tanggal_input"]), "yyyy-MM-dd")
        )

    # -------------------- TAMPIL DATA -------------------- #
    def tampilData(self):
        baris = self.crud.dataBarang()
        self.formBarang.tableBarang.setRowCount(0)
        for r in baris:
            i = self.formBarang.tableBarang.rowCount()
            self.formBarang.tableBarang.insertRow(i)
            self.formBarang.tableBarang.setItem(i, 0, QTableWidgetItem(str(r["barang_id"])))
            self.formBarang.tableBarang.setItem(i, 1, QTableWidgetItem(str(r["user_id"])))
            self.formBarang.tableBarang.setItem(i, 2, QTableWidgetItem(r["nama_barang"]))
            self.formBarang.tableBarang.setItem(i, 3, QTableWidgetItem(str(r["berat"])))
            self.formBarang.tableBarang.setItem(i, 4, QTableWidgetItem(r["deskripsi"]))
            self.formBarang.tableBarang.setItem(i, 5, QTableWidgetItem(str(r["tanggal_input"])))
        self.formBarang.tableBarang.resizeColumnsToContents()



