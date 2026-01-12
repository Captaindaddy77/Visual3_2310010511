# This Python file uses the following encoding: utf-8
import os
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb


class bayar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "bayar.ui")

        file_ui = QFile(ui_path)
        if not file_ui.exists():
            QMessageBox.warning(self, "Peringatan", f"File UI tidak ditemukan:\n{ui_path}")
            return

        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formBayar = loader.load(file_ui, self)
        file_ui.close()

        self.crud = my_cruddb()

        # ===== TOMBOL =====
        self.formBayar.btnSimpan.clicked.connect(self.doSimpanBayar)
        self.formBayar.btnUbah.clicked.connect(self.doUbahBayar)

        # ===== TAMPIL DATA =====
        self.tampilData()

    # ---------------- SIMPAN ----------------
    def doSimpanBayar(self):
        kode = self.formBayar.txtKode.text().strip()
        nama = self.formBayar.txtNamaBarang.text().strip()
        harga = self.formBayar.txtHarga.text().strip()
        jumlah = self.formBayar.txtJumlah.text().strip()

        if not kode or not harga or not jumlah:
            QMessageBox.information(self, "Info", "Data belum lengkap")
            return

        try:
            harga = float(harga)
            jumlah = int(jumlah)
        except ValueError:
            QMessageBox.warning(self, "Error", "Harga / jumlah tidak valid")
            return

        harga_diskon = harga - (harga * 0.007)

        self.crud.simpanBayar(kode, nama, harga_diskon, jumlah)
        self.tampilData()

        QMessageBox.information(
            self,
            "Info",
            f"Data berhasil disimpan\nHarga setelah diskon: {harga_diskon:.2f}"
        )

    # ---------------- UBAH ----------------
    def doUbahBayar(self):
        kode = self.formBayar.txtKode.text().strip()
        if not kode:
            QMessageBox.information(self, "Info", "Masukkan kode barang")
            return

        try:
            harga = float(self.formBayar.txtHarga.text())
            jumlah = int(self.formBayar.txtJumlah.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Harga / jumlah tidak valid")
            return

        harga_diskon = harga - (harga * 0.007)

        self.crud.ubahBayar(
            kode,
            self.formBayar.txtNamaBarang.text(),
            harga_diskon,
            jumlah
        )

        self.tampilData()
        QMessageBox.information(self, "Info", "Data berhasil diubah")

    # ---------------- TAMPIL DATA ----------------
    def tampilData(self):
        data = self.crud.dataBayar()   # ⬅️ HARUS ADA DI CRUD
        table = self.formBayar.tableBarang
        table.setRowCount(0)

        for r in data:
            row = table.rowCount()
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(str(r["kode"])))
            table.setItem(row, 1, QTableWidgetItem(r["nama_barang"]))
            table.setItem(row, 2, QTableWidgetItem(str(r["harga"])))
            table.setItem(row, 3, QTableWidgetItem(str(r["jumlah"])))

        table.resizeColumnsToContents()
