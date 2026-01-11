from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class bayar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("bayar.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formBayar = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        # tombol
        self.formBayar.btnSimpan.clicked.connect(self.doSimpanbayar)
        self.formBayar.btnUbah.clicked.connect(self.doUbahBayar)
        self.formBayar.btnTampil.clicked.connect(self.doTampilBayar)

    # ================= SIMPAN =================
    def doSimpanbayar(self):
        kode = self.formBayar.txtKode.text().strip()
        nama = self.formBayar.txtNamaBarang.text().strip()
        harga = self.formBayar.txtHarga.text().strip()
        jumlah = self.formBayar.txtJumlah.text().strip()

        if not kode or not harga:
            QMessageBox.information(None, "Info", "Kode dan harga wajib diisi")
            return

        harga = float(harga)
        harga_diskon = harga - (harga * 0.007)   # diskon 0,7%

        self.crud.simpanBayar(
            kode,
            nama,
            harga_diskon,
            jumlah
        )

        QMessageBox.information(
            None,
            "Info",
            f"Data tersimpan\nHarga setelah diskon: {harga_diskon:.2f}"
        )

    # ================= UBAH =================
    def doUbahBayar(self):
        kode = self.formBayar.txtKode.text().strip()
        nama = self.formBayar.txtNamaBarang.text().strip()
        harga = self.formBayar.txtHarga.text().strip()
        jumlah = self.formBayar.txtJumlah.text().strip()

        harga = float(harga)
        harga_diskon = harga - (harga * 0.007)   # diskon 0,7%

        self.crud.ubahBayar(
            kode,
            nama,
            harga_diskon,
            jumlah
        )

        QMessageBox.information(
            None,
            "Info",
            f"Data diubah\nHarga setelah diskon: {harga_diskon:.2f}"
        )

    # ================= TAMPIL =================
    def tampilData(self):
        hasil = self.crud.tampilBayar()

        if len(hasil) == 0:
            QMessageBox.information(None, "Info", "Data pembayaran kosong")
            return

        data = hasil[0]   # ambil data pertama

        # isi ke line edit
        self.formBayar.txtKode.setText(
            str(data["kode"])
        )
        self.formBayar.txtNamaBarang.setText(
            data["nama_barang"]
        )

        # harga + diskon 0.7%
        harga_asli = float(data["harga"])
        harga_diskon = harga_asli - (harga_asli * 0.007)

        self.formBayar.txtHarga.setText(
            str(int(harga_diskon))
        )

        self.formBayar.txtJumlah.setText(
            str(data["jumlah"])
        )

