# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crudDB import my_cruddb


class pengiriman(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "pengiriman.ui")

        file_ui = QFile(ui_path)
        if not file_ui.exists():
            QMessageBox.warning(None, "Peringatan", f"File UI tidak ditemukan:\n{ui_path}")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formPengiriman = loader.load(file_ui, self)
        file_ui.close()

        self.crud = my_cruddb()

        # Tombol CRUD
        self.formPengiriman.btnSimpan.clicked.connect(self.doSimpanPengiriman)
        self.formPengiriman.btnUbah.clicked.connect(self.doUbahPengiriman)
        self.formPengiriman.btnHapus.clicked.connect(self.doHapusPengiriman)
        self.formPengiriman.btnBersih.clicked.connect(self.doBersihPengiriman)
        self.formPengiriman.editCari.textChanged.connect(self.doCariPengiriman)

        # Tampilkan data di awal
        self.tampilData()

    # -------------------- SIMPAN -------------------- #
    def doSimpanPengiriman(self):
        pengiriman_id = self.formPengiriman.txtPengirimanID.text().strip()
        barang_id = self.formPengiriman.txtBarangID.text().strip()
        asal = self.formPengiriman.txtAsal.text().strip()
        tujuan = self.formPengiriman.txtTujuan.text().strip()
        jarak_km = self.formPengiriman.txtJarak.text().strip()
        biaya_kirim = self.formPengiriman.txtBiaya.text().strip()
        status = self.formPengiriman.cmbStatus.currentText()
        tanggal_kirim = self.formPengiriman.txtTanggalKirim.date().toString("yyyy-MM-dd")
        tanggal_terima = self.formPengiriman.txtTanggalTerima.date().toString("yyyy-MM-dd")

        # Validasi input
        if not pengiriman_id:
            QMessageBox.information(None, "Informasi", "ID Pengiriman belum diisi")
            self.formPengiriman.txtPengirimanID.setFocus()
            return
        if not barang_id:
            QMessageBox.information(None, "Informasi", "ID Barang belum diisi")
            self.formPengiriman.txtBarangID.setFocus()
            return
        if not asal or not tujuan:
            QMessageBox.information(None, "Informasi", "Asal dan Tujuan belum diisi")
            return

        pesan = QMessageBox.question(
            None,
            "Konfirmasi",
            "Apakah Anda yakin ingin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No
        )
        if pesan == QMessageBox.Yes:
            self.crud.simpanPengiriman(pengiriman_id, barang_id, asal, tujuan, jarak_km,
                                       biaya_kirim, status, tanggal_kirim, tanggal_terima)
            self.tampilData()
            QMessageBox.information(None, "Informasi", "Data pengiriman berhasil disimpan")

    # -------------------- UBAH -------------------- #
    def doUbahPengiriman(self):
        pengiriman_id = self.formPengiriman.txtPengirimanID.text().strip()
        barang_id = self.formPengiriman.txtBarangID.text().strip()
        asal = self.formPengiriman.txtAsal.text().strip()
        tujuan = self.formPengiriman.txtTujuan.text().strip()
        jarak_km = self.formPengiriman.txtJarak.text().strip()
        biaya_kirim = self.formPengiriman.txtBiaya.text().strip()
        status = self.formPengiriman.cmbStatus.currentText()
        tanggal_kirim = self.formPengiriman.txtTanggalKirim.date().toString("yyyy-MM-dd")
        tanggal_terima = self.formPengiriman.txtTanggalTerima.date().toString("yyyy-MM-dd")

        self.crud.ubahPengiriman(pengiriman_id, barang_id, asal, tujuan, jarak_km,
                                 biaya_kirim, status, tanggal_kirim, tanggal_terima)
        self.tampilData()
        QMessageBox.information(None, "Informasi", "Data pengiriman berhasil diubah")

    # -------------------- HAPUS -------------------- #
    def doHapusPengiriman(self):
        pengiriman_id = self.formPengiriman.txtPengirimanID.text().strip()
        if not pengiriman_id:
            QMessageBox.information(None, "Informasi", "Pilih data yang ingin dihapus")
            return

        pesan = QMessageBox.question(
            None,
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )
        if pesan == QMessageBox.Yes:
            self.crud.hapusPengiriman(pengiriman_id)
            self.tampilData()
            QMessageBox.information(None, "Informasi", "Data pengiriman berhasil dihapus")

    # -------------------- BERSIH -------------------- #
    def doBersihPengiriman(self):
        self.formPengiriman.txtPengirimanID.clear()
        self.formPengiriman.txtBarangID.clear()
        self.formPengiriman.txtAsal.clear()
        self.formPengiriman.txtTujuan.clear()
        self.formPengiriman.txtJarak.clear()
        self.formPengiriman.txtBiaya.clear()
        self.formPengiriman.cmbStatus.setCurrentIndex(0)
        self.formPengiriman.editCari.clear()
        self.tampilData()

    # -------------------- CARI -------------------- #
    def doCariPengiriman(self):
        keyword = self.formPengiriman.editCari.text().strip()
        hasil = self.crud.cariPengiriman(keyword)

        self.formPengiriman.tablePengiriman.setRowCount(0)
        for r in hasil:
            i = self.formPengiriman.tablePengiriman.rowCount()
            self.formPengiriman.tablePengiriman.insertRow(i)
            self.formPengiriman.tablePengiriman.setItem(i, 0, QTableWidgetItem(str(r["pengiriman_id"])))
            self.formPengiriman.tablePengiriman.setItem(i, 1, QTableWidgetItem(str(r["barang_id"])))
            self.formPengiriman.tablePengiriman.setItem(i, 2, QTableWidgetItem(r["asal"]))
            self.formPengiriman.tablePengiriman.setItem(i, 3, QTableWidgetItem(r["tujuan"]))
            self.formPengiriman.tablePengiriman.setItem(i, 4, QTableWidgetItem(str(r["jarak_km"])))
            self.formPengiriman.tablePengiriman.setItem(i, 5, QTableWidgetItem(str(r["biaya_kirim"])))
            self.formPengiriman.tablePengiriman.setItem(i, 6, QTableWidgetItem(r["status"]))
            self.formPengiriman.tablePengiriman.setItem(i, 7, QTableWidgetItem(str(r["tanggal_kirim"])))
            self.formPengiriman.tablePengiriman.setItem(i, 8, QTableWidgetItem(str(r["tanggal_terima"])))

    # -------------------- TAMPIL DATA -------------------- #
    def tampilData(self):
        baris = self.crud.tampilPengiriman()
        self.formPengiriman.tablePengiriman.setRowCount(0)
        for r in baris:
            i = self.formPengiriman.tablePengiriman.rowCount()
            self.formPengiriman.tablePengiriman.insertRow(i)
            self.formPengiriman.tablePengiriman.setItem(i, 0, QTableWidgetItem(str(r["pengiriman_id"])))
            self.formPengiriman.tablePengiriman.setItem(i, 1, QTableWidgetItem(str(r["barang_id"])))
            self.formPengiriman.tablePengiriman.setItem(i, 2, QTableWidgetItem(r["asal"]))
            self.formPengiriman.tablePengiriman.setItem(i, 3, QTableWidgetItem(r["tujuan"]))
            self.formPengiriman.tablePengiriman.setItem(i, 4, QTableWidgetItem(str(r["jarak_km"])))
            self.formPengiriman.tablePengiriman.setItem(i, 5, QTableWidgetItem(str(r["biaya_kirim"])))
            self.formPengiriman.tablePengiriman.setItem(i, 6, QTableWidgetItem(r["status"]))
            self.formPengiriman.tablePengiriman.setItem(i, 7, QTableWidgetItem(str(r["tanggal_kirim"])))
            self.formPengiriman.tablePengiriman.setItem(i, 8, QTableWidgetItem(str(r["tanggal_terima"])))
        self.formPengiriman.tablePengiriman.resizeColumnsToContents()
