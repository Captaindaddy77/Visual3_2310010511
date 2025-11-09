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
        # Load UI
        ui_file = QFile("kurir.ui")
        if not ui_file.exists():
            print("File kurir.ui tidak ditemukan!")
            sys.exit(-1)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # Set combo status sesuai enum
        self.ui.cmbStatus.clear()
        self.ui.cmbStatus.addItems(["aktif", "nonaktif"])

        # Connect buttons
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnCari.clicked.connect(self.cari)
        self.ui.btnBersih.clicked.connect(self.bersih)

        # Initialize database dengan pengecekan koneksi
        try:
            self.koneksi = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="sistem_pengiriman"
            )
            self.cursor = self.koneksi.cursor()
            print("Koneksi database berhasil")  # <-- tampil di terminal
        except Error as e:
            print(f"Gagal koneksi ke database: {e}")
            sys.exit(-1)

        # Load data awal
        self.load_data()

    def load_data(self):
        self.ui.tableKurir.setRowCount(0)
        self.cursor.execute("SELECT * FROM kurir")
        for row_data in self.cursor.fetchall():
            row = self.ui.tableKurir.rowCount()
            self.ui.tableKurir.insertRow(row)
            for column, data in enumerate(row_data):
                self.ui.tableKurir.setItem(row, column, QTableWidgetItem(str(data)))

    def simpan(self):
        try:
            sql = "INSERT INTO kurir (kurir_id, nama_kurir, no_hp, email, plat_nomor, status) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (
                self.ui.txtKurirID.text(),
                self.ui.txtNamaKurir.text(),
                self.ui.txtNoHP.text(),
                self.ui.txtEmail.text(),
                self.ui.txtPlatNomor.text(),
                self.ui.cmbStatus.currentText()
            )
            self.cursor.execute(sql, val)
            self.koneksi.commit()
            print("Data berhasil disimpan")  # tampil di terminal
            self.load_data()
        except Exception as e:
            print(f"Error simpan: {e}")

    def ubah(self):
        try:
            sql = """UPDATE kurir SET
                     nama_kurir=%s, no_hp=%s, email=%s, plat_nomor=%s, status=%s
                     WHERE kurir_id=%s"""
            val = (
                self.ui.txtNamaKurir.text(),
                self.ui.txtNoHP.text(),
                self.ui.txtEmail.text(),
                self.ui.txtPlatNomor.text(),
                self.ui.cmbStatus.currentText(),
                self.ui.txtKurirID.text()
            )
            self.cursor.execute(sql, val)
            self.koneksi.commit()
            print("Data berhasil diubah")  # tampil di terminal
            self.load_data()
        except Exception as e:
            print(f"Error ubah: {e}")

    def hapus(self):
        try:
            sql = "DELETE FROM kurir WHERE kurir_id=%s"
            val = (self.ui.txtKurirID.text(),)
            self.cursor.execute(sql, val)
            self.koneksi.commit()
            print("Data berhasil dihapus")  # tampil di terminal
            self.load_data()
        except Exception as e:
            print(f"Error hapus: {e}")

    def cari(self):
        keyword = self.ui.txtKurirID.text()
        self.ui.tableKurir.setRowCount(0)
        self.cursor.execute(
            "SELECT * FROM kurir WHERE kurir_id LIKE %s OR nama_kurir LIKE %s",
            (f"%{keyword}%", f"%{keyword}%")
        )
        for row_data in self.cursor.fetchall():
            row = self.ui.tableKurir.rowCount()
            self.ui.tableKurir.insertRow(row)
            for column, data in enumerate(row_data):
                self.ui.tableKurir.setItem(row, column, QTableWidgetItem(str(data)))

    def bersih(self):
        self.ui.txtKurirID.clear()
        self.ui.txtNamaKurir.clear()
        self.ui.txtNoHP.clear()
        self.ui.txtEmail.clear()
        self.ui.txtPlatNomor.clear()
        self.ui.cmbStatus.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = kurir()
    window.show()
    sys.exit(app.exec())
