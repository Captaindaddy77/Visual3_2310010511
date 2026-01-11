# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import mysql.connector
from mysql.connector import Error


class kurir(QWidget):
    def __init__(self):
        super().__init__()

        # ------------------ LOAD UI ------------------ #
        ui_file = QFile("kurir.ui")
        if not ui_file.exists():
            QMessageBox.critical(None, "Kesalahan", "File kurir.ui tidak ditemukan!")
            sys.exit(-1)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formKurir = loader.load(ui_file, self)
        ui_file.close()

        # ------------------ INISIALISASI DB ------------------ #
        try:
            self.koneksi = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="sistem_pengiriman"
            )
            self.cursor = self.koneksi.cursor(dictionary=True)
            print("Koneksi database berhasil.")
        except Error as e:
            QMessageBox.critical(None, "Kesalahan", f"Gagal koneksi database:\n{e}")
            sys.exit(-1)

        # ------------------ ISI COMBOBOX STATUS ------------------ #
        self.formKurir.cmbStatus.clear()
        self.formKurir.cmbStatus.addItems(["aktif", "nonaktif"])

        # ------------------ KONEKSI TOMBOL ------------------ #
        self.formKurir.btnSimpan.clicked.connect(self.doSimpanKurir)
        self.formKurir.btnUbah.clicked.connect(self.doUbahKurir)
        self.formKurir.btnHapus.clicked.connect(self.doHapusKurir)
        self.formKurir.btnBersih.clicked.connect(self.doBersihKurir)
        self.formKurir.editCari.textChanged.connect(self.doCariKurir)

        # ------------------ TAMPIL DATA AWAL ------------------ #
        self.tampilData()

    # =======================================================
    # SIMPAN DATA
    # =======================================================
    def doSimpanKurir(self):
        id_kurir = self.formKurir.txtKurirID.text().strip()
        nama = self.formKurir.txtNamaKurir.text().strip()
        no_hp = self.formKurir.txtNoHP.text().strip()
        email = self.formKurir.txtEmail.text().strip()
        plat = self.formKurir.txtPlatNomor.text().strip()
        status = self.formKurir.cmbStatus.currentText()

        # Validasi input
        if not id_kurir:
            QMessageBox.information(None, "Informasi", "ID Kurir belum diisi.")
            self.formKurir.txtKurirID.setFocus()
            return
        if not nama:
            QMessageBox.information(None, "Informasi", "Nama Kurir belum diisi.")
            self.formKurir.txtNamaKurir.setFocus()
            return

        # Konfirmasi simpan
        pesan = QMessageBox.question(
            None,
            "Konfirmasi",
            "Apakah Anda yakin ingin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No
        )
        if pesan == QMessageBox.Yes:
            try:
                sql = """
                    INSERT INTO kurir (kurir_id, nama_kurir, no_hp, email, plat_nomor, status)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                val = (id_kurir, nama, no_hp, email, plat, status)
                self.cursor.execute(sql, val)
                self.koneksi.commit()
                QMessageBox.information(None, "Informasi", "Data berhasil disimpan.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(None, "Kesalahan", f"Gagal menyimpan data:\n{e}")

    # =======================================================
    # UBAH DATA
    # =======================================================
    def doUbahKurir(self):
        id_kurir = self.formKurir.txtKurirID.text().strip()
        nama = self.formKurir.txtNamaKurir.text().strip()
        no_hp = self.formKurir.txtNoHP.text().strip()
        email = self.formKurir.txtEmail.text().strip()
        plat = self.formKurir.txtPlatNomor.text().strip()
        status = self.formKurir.cmbStatus.currentText()

        if not id_kurir:
            QMessageBox.information(None, "Informasi", "Pilih data yang akan diubah.")
            return

        try:
            sql = """
                UPDATE kurir
                SET nama_kurir=%s, no_hp=%s, email=%s, plat_nomor=%s, status=%s
                WHERE kurir_id=%s
            """
            val = (nama, no_hp, email, plat, status, id_kurir)
            self.cursor.execute(sql, val)
            self.koneksi.commit()
            QMessageBox.information(None, "Informasi", "Data berhasil diubah.")
            self.tampilData()
        except Exception as e:
            QMessageBox.critical(None, "Kesalahan", f"Gagal mengubah data:\n{e}")

    # =======================================================
    # HAPUS DATA
    # =======================================================
    def doHapusKurir(self):
        id_kurir = self.formKurir.txtKurirID.text().strip()

        if not id_kurir:
            QMessageBox.information(None, "Informasi", "Masukkan ID Kurir yang akan dihapus.")
            return

        pesan = QMessageBox.question(
            None,
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )
        if pesan == QMessageBox.Yes:
            try:
                sql = "DELETE FROM kurir WHERE kurir_id = %s"
                self.cursor.execute(sql, (id_kurir,))
                self.koneksi.commit()
                QMessageBox.information(None, "Informasi", "Data berhasil dihapus.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(None, "Kesalahan", f"Gagal menghapus data:\n{e}")

    # =======================================================
    # CARI DATA
    # =======================================================
    def doCariKurir(self):
        keyword = self.formKurir.editCari.text().strip()
        self.formKurir.tableKurir.setRowCount(0)

        try:
            sql = """
                SELECT * FROM kurir
                WHERE kurir_id LIKE %s
                   OR nama_kurir LIKE %s
                   OR no_hp LIKE %s
                   OR email LIKE %s
                   OR plat_nomor LIKE %s
                   OR status LIKE %s
            """
            val = [f"%{keyword}%"] * 6
            self.cursor.execute(sql, val)
            hasil = self.cursor.fetchall()

            for row_data in hasil:
                i = self.formKurir.tableKurir.rowCount()
                self.formKurir.tableKurir.insertRow(i)
                self.formKurir.tableKurir.setItem(i, 0, QTableWidgetItem(str(row_data["kurir_id"])))
                self.formKurir.tableKurir.setItem(i, 1, QTableWidgetItem(row_data["nama_kurir"]))
                self.formKurir.tableKurir.setItem(i, 2, QTableWidgetItem(row_data["no_hp"]))
                self.formKurir.tableKurir.setItem(i, 3, QTableWidgetItem(row_data["email"]))
                self.formKurir.tableKurir.setItem(i, 4, QTableWidgetItem(row_data["plat_nomor"]))
                self.formKurir.tableKurir.setItem(i, 5, QTableWidgetItem(row_data["status"]))
        except Exception as e:
            QMessageBox.critical(None, "Kesalahan", f"Gagal mencari data:\n{e}")

    # =======================================================
    # AUTO ISI FORM
    # =======================================================
        if len(hasil) > 0:
            data = hasil[0]

            self.formKurir.txtKurirID.setText(str(data["kurir_id"]))
            self.formKurir.txtNamaKurir.setText(data["nama_kurir"])
            self.formKurir.txtNoHP.setText(data["no_hp"])
            self.formKurir.txtEmail.setText(data["email"])
            self.formKurir.txtPlatNomor.setText(data["plat_nomor"])

        idx_status = self.formKurir.cmbStatus.findText(data["status"])
        if idx_status != -1:
            self.formKurir.cmbStatus.setCurrentIndex(idx_status)

    # =======================================================
    # BERSIHKAN FORM
    # =======================================================
    def doBersihKurir(self):
        self.formKurir.txtKurirID.clear()
        self.formKurir.txtNamaKurir.clear()
        self.formKurir.txtNoHP.clear()
        self.formKurir.txtEmail.clear()
        self.formKurir.txtPlatNomor.clear()
        self.formKurir.cmbStatus.setCurrentIndex(0)
        self.formKurir.editCari.clear()
        self.tampilData()

    # =======================================================
    # TAMPIL DATA
    # =======================================================
    def tampilData(self):
        try:
            self.formKurir.tableKurir.setRowCount(0)
            self.cursor.execute("SELECT * FROM kurir ORDER BY kurir_id ASC")
            hasil = self.cursor.fetchall()

            for row_data in hasil:
                i = self.formKurir.tableKurir.rowCount()
                self.formKurir.tableKurir.insertRow(i)
                self.formKurir.tableKurir.setItem(i, 0, QTableWidgetItem(str(row_data["kurir_id"])))
                self.formKurir.tableKurir.setItem(i, 1, QTableWidgetItem(row_data["nama_kurir"]))
                self.formKurir.tableKurir.setItem(i, 2, QTableWidgetItem(row_data["no_hp"]))
                self.formKurir.tableKurir.setItem(i, 3, QTableWidgetItem(row_data["email"]))
                self.formKurir.tableKurir.setItem(i, 4, QTableWidgetItem(row_data["plat_nomor"]))
                self.formKurir.tableKurir.setItem(i, 5, QTableWidgetItem(row_data["status"]))

            self.formKurir.tableKurir.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.critical(None, "Kesalahan", f"Gagal menampilkan data:\n{e}")



