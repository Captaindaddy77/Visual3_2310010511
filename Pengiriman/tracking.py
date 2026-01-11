# This Python file uses the following encoding: utf-8
import sys
import os
from datetime import date, datetime
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crudDB import my_cruddb


class tracking(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "tracking.ui")

        file_ui = QFile(ui_path)
        if not file_ui.exists():
            QMessageBox.warning(None, "Peringatan", f"File UI tidak ditemukan:\n{ui_path}")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formTracking = loader.load(file_ui, self)
        file_ui.close()

        # Inisialisasi CRUD
        self.crud = my_cruddb()

        # Isi combobox status
        self.formTracking.cmbStatus.clear()
        self.formTracking.cmbStatus.addItems(["dikemas", "dikirim", "selesai", "gagal"])

        # Tombol CRUD
        self.formTracking.btnSimpan.clicked.connect(self.doSimpanTracking)
        self.formTracking.btnUbah.clicked.connect(self.doUbahTracking)
        self.formTracking.btnHapus.clicked.connect(self.doHapusTracking)
        self.formTracking.btnBersih.clicked.connect(self.doBersihTracking)
        self.formTracking.editCari.textChanged.connect(self.doCariTracking)

        # Isi tabel di awal
        self.tampilData()

    # -------------------- SIMPAN -------------------- #
    def doSimpanTracking(self):
        tracking_id = self.formTracking.txtTrackingID.text().strip()
        pengiriman_id = self.formTracking.txtPengirimanID.text().strip()
        kurir_id = self.formTracking.txtKurirID.text().strip()
        status = self.formTracking.cmbStatus.currentText()
        lokasi = self.formTracking.txtLokasi.text().strip()
        tanggal = self.formTracking.dateTimeUpdate.date().toString("yyyy-MM-dd")

        if not tracking_id:
            QMessageBox.information(None, "Informasi", "Tracking ID belum diisi")
            self.formTracking.txtTrackingID.setFocus()
            return
        if not pengiriman_id:
            QMessageBox.information(None, "Informasi", "Pengiriman ID belum diisi")
            self.formTracking.txtPengirimanID.setFocus()
            return
        if not kurir_id:
            QMessageBox.information(None, "Informasi", "Kurir ID belum diisi")
            self.formTracking.txtKurirID.setFocus()
            return

        pesan = QMessageBox.question(
            None,
            "Konfirmasi",
            "Apakah Anda yakin ingin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No
        )
        if pesan == QMessageBox.Yes:
            self.crud.simpanTracking(tracking_id, pengiriman_id, kurir_id, status, lokasi, tanggal)
            self.tampilData()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    # -------------------- UBAH -------------------- #
    def doUbahTracking(self):
        tracking_id = self.formTracking.txtTrackingID.text().strip()
        pengiriman_id = self.formTracking.txtPengirimanID.text().strip()
        kurir_id = self.formTracking.txtKurirID.text().strip()
        status = self.formTracking.cmbStatus.currentText()
        lokasi = self.formTracking.txtLokasi.text().strip()
        tanggal = self.formTracking.dateTimeUpdate.date().toString("yyyy-MM-dd")

        self.crud.ubahTracking(tracking_id, pengiriman_id, kurir_id, status, lokasi, tanggal)
        self.tampilData()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    # -------------------- HAPUS -------------------- #
    def doHapusTracking(self):
        tracking_id = self.formTracking.txtTrackingID.text().strip()
        if not tracking_id:
            QMessageBox.information(None, "Informasi", "Pilih data yang ingin dihapus")
            return

        pesan = QMessageBox.question(
            None,
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )
        if pesan == QMessageBox.Yes:
            self.crud.hapusTracking(tracking_id)
            self.tampilData()
            QMessageBox.information(None, "Informasi", "Data berhasil dihapus")

    # -------------------- BERSIH -------------------- #
    def doBersihTracking(self):
        self.formTracking.txtTrackingID.clear()
        self.formTracking.txtPengirimanID.clear()
        self.formTracking.txtKurirID.clear()
        self.formTracking.txtLokasi.clear()
        self.formTracking.editCari.clear()
        self.formTracking.cmbStatus.setCurrentIndex(0)
        self.formTracking.dateTimeUpdate.setDate(QDate.currentDate())
        self.tampilData()

    # -------------------- CARI -------------------- #
    def doCariTracking(self):
        keyword = self.formTracking.editCari.text().strip()
        hasil = self.crud.cariTrackingMulti(keyword)

        self.formTracking.tableTracking.setRowCount(0)
        for r in hasil:
            i = self.formTracking.tableTracking.rowCount()
            self.formTracking.tableTracking.insertRow(i)
            self.formTracking.tableTracking.setItem(i, 0, QTableWidgetItem(str(r["tracking_id"])))
            self.formTracking.tableTracking.setItem(i, 1, QTableWidgetItem(str(r["pengiriman_id"])))
            self.formTracking.tableTracking.setItem(i, 2, QTableWidgetItem(str(r["kurir_id"])))
            self.formTracking.tableTracking.setItem(i, 3, QTableWidgetItem(r["status"]))
            self.formTracking.tableTracking.setItem(i, 4, QTableWidgetItem(r["lokasi"]))
            self.formTracking.tableTracking.setItem(i, 5, QTableWidgetItem(str(r["waktu_update"])))

    # -------------------- AUTO ISI FORM -------------------- #
        if len(hasil) > 0:
            data = hasil[0]

            self.formTracking.txtTrackingID.setText(str(data["tracking_id"]))
            self.formTracking.txtPengirimanID.setText(str(data["pengiriman_id"]))
            self.formTracking.txtKurirID.setText(str(data["kurir_id"]))
            self.formTracking.txtLokasi.setText(data["lokasi"])

            idx_status = self.formTracking.cmbStatus.findText(data["status"])
        if idx_status != -1:
            self.formTracking.cmbStatus.setCurrentIndex(idx_status)

            self.formTracking.dateTimeUpdate.setDate(
            QDate.fromString(str(data["waktu_update"]), "yyyy-MM-dd")
        )

    # -------------------- TAMPIL DATA -------------------- #
    def tampilData(self):
        baris = self.crud.tampilTracking()
        self.formTracking.tableTracking.setRowCount(0)
        for r in baris:
            i = self.formTracking.tableTracking.rowCount()
            self.formTracking.tableTracking.insertRow(i)
            self.formTracking.tableTracking.setItem(i, 0, QTableWidgetItem(str(r["tracking_id"])))
            self.formTracking.tableTracking.setItem(i, 1, QTableWidgetItem(str(r["pengiriman_id"])))
            self.formTracking.tableTracking.setItem(i, 2, QTableWidgetItem(str(r["kurir_id"])))
            self.formTracking.tableTracking.setItem(i, 3, QTableWidgetItem(r["status"]))
            self.formTracking.tableTracking.setItem(i, 4, QTableWidgetItem(r["lokasi"]))
            self.formTracking.tableTracking.setItem(i, 5, QTableWidgetItem(str(r["waktu_update"])))
        self.formTracking.tableTracking.resizeColumnsToContents()
