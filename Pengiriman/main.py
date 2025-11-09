# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from barang import barang
from pembayaran import pembayaran
from pengiriman import pengiriman
from kurir import kurir
from tracking import tracking

class HalamanUtama(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Load UI utama
        ui_file = QFile("form.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formutama = loader.load(ui_file, self)
        ui_file.close()
        self.setMenuBar(self.formutama.menuBar())
        self.resize(self.formutama.size())

        # Hubungkan menu
        self.formutama.actionBarang.triggered.connect(self.bukabarang)
        self.formutama.actionPembayaran.triggered.connect(self.bukapembayaran)
        self.formutama.actionPengiriman.triggered.connect(self.bukapengiriman)
        self.formutama.actionKurir.triggered.connect(self.bukakurir)
        self.formutama.actionTracking.triggered.connect(self.bukatracking)

    def bukabarang(self):
        self.formbarang = barang()
        self.formbarang.show()

    def bukapembayaran(self):
        self.formpembayaran = pembayaran()
        self.formpembayaran.show()

    def bukapengiriman(self):
        self.formpengiriman = pengiriman()
        self.formpengiriman.show()

    def bukakurir(self):
        self.formkurir = kurir()
        self.formkurir.show()

    def bukatracking(self):
        self.formtracking = tracking()
        self.formtracking.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HalamanUtama()
    window.show()
    sys.exit(app.exec())
