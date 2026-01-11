# This Python file uses the following encoding: utf-8
import os
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crudDB import my_cruddb


class pembayaran(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "pembayaran.ui")

        file_ui = QFile(ui_path)
        if not file_ui.exists():
            QMessageBox.warning(None, "Peringatan", f"File UI tidak ditemukan:\n{ui_path}")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formPembayaran = loader.load(file_ui, self)
        file_ui.close()

        self.crud = my_cruddb()

        # Tombol CRUD
        self.formPembayaran.btnSimpan.clicked.connect(self.doSimpanPembayaran)
        self.formPembayaran.btnUbah.clicked.connect(self.doUbahPembayaran)
        self.formPembayaran.btnHapus.clicked.connect(self.doHapusPembayaran)
        self.formPembayaran.btnBersih.clicked.connect(self.doBersihPembayaran)
        self.formPembayaran.editCari.textChanged.connect(self.doCariPembayaran)

        # Isi combo box
        self.formPembayaran.comboMetode.clear()
        self.formPembayaran.comboMetode.addItems(["Transfer Bank", "COD", "E-Wallet"])
        self.formPembayaran.comboStatus.clear()
        self.formPembayaran.comboStatus.addItems(["Belum Bayar", "Sudah Bayar"])

        # Isi tabel di awal
        self.tampilData()

    # -------------------- SIMPAN -------------------- #
    def doSimpanPembayaran(self):
        pembayaran_id = self.formPembayaran.txtPembayaranID.text().strip()
        pengiriman_id = self.formPembayaran.txtPengirimanID.text().strip()
        metode = self.formPembayaran.comboMetode.currentText().strip()
        jumlah = self.formPembayaran.txtJumlah.text().strip()
        status = self.formPembayaran.comboStatus.currentText().strip()
        tanggal = self.formPembayaran.dateTanggalBayar.date().toString("yyyy-MM-dd")

        if not pembayaran_id:
            QMessageBox.information(None, "Informasi", "ID Pembayaran belum diisi")
            self.formPembayaran.txtPembayaranID.setFocus()
            return
        if not pengiriman_id:
            QMessageBox.information(None, "Informasi", "Pengiriman ID belum diisi")
            self.formPembayaran.txtPengirimanID.setFocus()
            return
        if not jumlah:
            QMessageBox.information(None, "Informasi", "Jumlah pembayaran belum diisi")
            self.formPembayaran.txtJumlah.setFocus()
            return

        pesan = QMessageBox.question(
            None,
            "Konfirmasi",
            "Apakah Anda yakin ingin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No
        )
        if pesan == QMessageBox.Yes:
            self.crud.simpanPembayaran(
                pembayaran_id, pengiriman_id, metode, jumlah, status, tanggal
            )
            self.tampilData()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    # -------------------- UBAH -------------------- #
    def doUbahPembayaran(self):
        pembayaran_id = self.formPembayaran.txtPembayaranID.text().strip()
        pengiriman_id = self.formPembayaran.txtPengirimanID.text().strip()
        metode = self.formPembayaran.comboMetode.currentText().strip()
        jumlah = self.formPembayaran.txtJumlah.text().strip()
        status = self.formPembayaran.comboStatus.currentText().strip()
        tanggal = self.formPembayaran.dateTanggalBayar.date().toString("yyyy-MM-dd")

        if not pembayaran_id:
            QMessageBox.information(None, "Informasi", "Masukkan ID Pembayaran yang akan diubah")
            return

        self.crud.ubahPembayaran(
            pembayaran_id, pengiriman_id, metode, jumlah, status, tanggal
        )
        self.tampilData()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    # -------------------- HAPUS -------------------- #
    def doHapusPembayaran(self):
        pembayaran_id = self.formPembayaran.txtPembayaranID.text().strip()
        if not pembayaran_id:
            QMessageBox.information(None, "Informasi", "Pilih data yang ingin dihapus")
            return

        pesan = QMessageBox.question(
            None,
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )
        if pesan == QMessageBox.Yes:
            self.crud.hapusPembayaran(pembayaran_id)
            self.tampilData()
            QMessageBox.information(None, "Informasi", "Data berhasil dihapus")

    # -------------------- BERSIH -------------------- #
    def doBersihPembayaran(self):
        self.formPembayaran.txtPembayaranID.clear()
        self.formPembayaran.txtPengirimanID.clear()
        self.formPembayaran.txtJumlah.clear()
        self.formPembayaran.comboMetode.setCurrentIndex(0)
        self.formPembayaran.comboStatus.setCurrentIndex(0)
        self.formPembayaran.editCari.clear()
        self.tampilData()

    # -------------------- CARI -------------------- #
    def doCariPembayaran(self):
        keyword = self.formPembayaran.editCari.text().strip()
        hasil = self.crud.cariPembayaranMulti(keyword)

        self.formPembayaran.tablePembayaran.setRowCount(0)
        for r in hasil:
            i = self.formPembayaran.tablePembayaran.rowCount()
            self.formPembayaran.tablePembayaran.insertRow(i)
            self.formPembayaran.tablePembayaran.setItem(i, 0, QTableWidgetItem(str(r["pembayaran_id"])))
            self.formPembayaran.tablePembayaran.setItem(i, 1, QTableWidgetItem(str(r["pengiriman_id"])))
            self.formPembayaran.tablePembayaran.setItem(i, 2, QTableWidgetItem(r["metode"]))
            self.formPembayaran.tablePembayaran.setItem(i, 3, QTableWidgetItem(str(r["jumlah"])))
            self.formPembayaran.tablePembayaran.setItem(i, 4, QTableWidgetItem(r["status_bayar"]))
            self.formPembayaran.tablePembayaran.setItem(i, 5, QTableWidgetItem(str(r["tanggal_bayar"])))

    # -------------------- AUTO ISI FORM -------------------- #
            if len(hasil) > 0:
                data = hasil[0]   # ambil data pertama

                self.formPembayaran.txtPembayaranID.setText(
                    str(data["pembayaran_id"])
                )
                self.formPembayaran.txtPengirimanID.setText(
                    str(data["pengiriman_id"])
                )
                self.formPembayaran.txtJumlah.setText(
                    str(data["jumlah"])
                )

                # combo metode
                idx_metode = self.formPembayaran.comboMetode.findText(
                    data["metode"]
                )
                if idx_metode != -1:
                    self.formPembayaran.comboMetode.setCurrentIndex(idx_metode)

                # combo status
                idx_status = self.formPembayaran.comboStatus.findText(
                    data["status_bayar"]
                )
                if idx_status != -1:
                    self.formPembayaran.comboStatus.setCurrentIndex(idx_status)

                # tanggal bayar
                self.formPembayaran.dateTanggalBayar.setDate(
                    QDate.fromString(str(data["tanggal_bayar"]), "yyyy-MM-dd")
                )


    # -------------------- TAMPIL DATA -------------------- #
    def tampilData(self):
        baris = self.crud.tampilPembayaran()
        self.formPembayaran.tablePembayaran.setRowCount(0)
        for r in baris:
            i = self.formPembayaran.tablePembayaran.rowCount()
            self.formPembayaran.tablePembayaran.insertRow(i)
            self.formPembayaran.tablePembayaran.setItem(i, 0, QTableWidgetItem(str(r["pembayaran_id"])))
            self.formPembayaran.tablePembayaran.setItem(i, 1, QTableWidgetItem(str(r["pengiriman_id"])))
            self.formPembayaran.tablePembayaran.setItem(i, 2, QTableWidgetItem(r["metode"]))
            self.formPembayaran.tablePembayaran.setItem(i, 3, QTableWidgetItem(str(r["jumlah"])))
            self.formPembayaran.tablePembayaran.setItem(i, 4, QTableWidgetItem(r["status_bayar"]))
            self.formPembayaran.tablePembayaran.setItem(i, 5, QTableWidgetItem(str(r["tanggal_bayar"])))
        self.formPembayaran.tablePembayaran.resizeColumnsToContents()
