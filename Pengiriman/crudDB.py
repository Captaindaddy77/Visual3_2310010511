# This Python file uses the following encoding: utf-8
import mysql.connector
from mysql.connector import Error

class my_cruddb:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='sistem_pengiriman'
            )
            print("Koneksi database berhasil.")
        except Error as e:
            print(f"Gagal koneksi ke database: {e}")

    # ====================== GENERIK ==========================
    def tampilData(self, nama_tabel):
        cursor = self.conn.cursor(dictionary=True)
        sql = f"SELECT * FROM {nama_tabel}"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data

    def eksekusi(self, query, data=None):
        cursor = self.conn.cursor()
        cursor.execute(query, data)
        self.conn.commit()
        cursor.close()

    # ====================== BARANG ===========================
    def simpanBarang(self, barang_id, user_id, nama_barang, berat, deskripsi, tanggal_input):
        sql = """
            INSERT INTO barang (barang_id, user_id, nama_barang, berat, deskripsi, tanggal_input)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.eksekusi(sql, (barang_id, user_id, nama_barang, berat, deskripsi, tanggal_input))

    def ubahBarang(self, barang_id, user_id, nama_barang, berat, deskripsi, tanggal_input):
        sql = """
            UPDATE barang
            SET user_id=%s, nama_barang=%s, berat=%s, deskripsi=%s, tanggal_input=%s
            WHERE barang_id=%s
        """
        self.eksekusi(sql, (user_id, nama_barang, berat, deskripsi, tanggal_input, barang_id))

    def hapusBarang(self, barang_id):
        sql = "DELETE FROM barang WHERE barang_id=%s"
        self.eksekusi(sql, (barang_id,))

    def cariBarang(self, barang_id):
        cursor = self.conn.cursor(dictionary=True)
        sql = "SELECT * FROM barang WHERE barang_id=%s"
        cursor.execute(sql, (barang_id,))
        data = cursor.fetchone()
        cursor.close()
        return data

    def tampilBarang(self):
        return self.tampilData("barang")

    def cariBarangMulti(self, barang_id="", user_id="", nama_barang="", berat="", deskripsi="", tanggal_input=""):
        cursor = self.conn.cursor(dictionary=True)
        sql = """
            SELECT * FROM barang
            WHERE barang_id LIKE %s OR user_id LIKE %s OR nama_barang LIKE %s
            OR berat LIKE %s OR deskripsi LIKE %s OR tanggal_input LIKE %s
        """
        params = [f"%{barang_id}%", f"%{user_id}%", f"%{nama_barang}%", f"%{berat}%", f"%{deskripsi}%", f"%{tanggal_input}%"]
        cursor.execute(sql, params)
        hasil = cursor.fetchall()
        cursor.close()
        return hasil

    # ====================== PENGIRIMAN =======================
    def simpanPengiriman(self, pengiriman_id, barang_id, asal, tujuan, jarak_km, biaya_kirim, status, tanggal_kirim, tanggal_terima):
        sql = """
            INSERT INTO pengiriman (pengiriman_id, barang_id, asal, tujuan, jarak_km, biaya_kirim, status, tanggal_kirim, tanggal_terima)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.eksekusi(sql, (pengiriman_id, barang_id, asal, tujuan, jarak_km, biaya_kirim, status, tanggal_kirim, tanggal_terima))

    def ubahPengiriman(self, pengiriman_id, barang_id, asal, tujuan, jarak_km, biaya_kirim, status, tanggal_kirim, tanggal_terima):
        sql = """
            UPDATE pengiriman
            SET barang_id=%s, asal=%s, tujuan=%s, jarak_km=%s, biaya_kirim=%s, status=%s, tanggal_kirim=%s, tanggal_terima=%s
            WHERE pengiriman_id=%s
        """
        self.eksekusi(sql, (barang_id, asal, tujuan, jarak_km, biaya_kirim, status, tanggal_kirim, tanggal_terima, pengiriman_id))

    def hapusPengiriman(self, pengiriman_id):
        sql = "DELETE FROM pengiriman WHERE pengiriman_id=%s"
        self.eksekusi(sql, (pengiriman_id,))

    def cariPengiriman(self, pengiriman_id):
        cursor = self.conn.cursor(dictionary=True)
        sql = "SELECT * FROM pengiriman WHERE pengiriman_id=%s"
        cursor.execute(sql, (pengiriman_id,))
        data = cursor.fetchone()
        cursor.close()
        return data

    def tampilPengiriman(self):
        return self.tampilData("pengiriman")

    def cariPengirimanMulti(self, keyword):
        cursor = self.conn.cursor(dictionary=True)
        sql = """
            SELECT * FROM pengiriman
            WHERE pengiriman_id LIKE %s OR barang_id LIKE %s OR asal LIKE %s OR tujuan LIKE %s OR status LIKE %s
        """
        params = [f"%{keyword}%"] * 5
        cursor.execute(sql, params)
        hasil = cursor.fetchall()
        cursor.close()
        return hasil

    # ====================== PEMBAYARAN =======================
    def simpanPembayaran(self, pembayaran_id, pengiriman_id, metode, jumlah, status_bayar, tanggal_bayar):
        sql = """
            INSERT INTO pembayaran (pembayaran_id, pengiriman_id, metode, jumlah, status_bayar, tanggal_bayar)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.eksekusi(sql, (pembayaran_id, pengiriman_id, metode, jumlah, status_bayar, tanggal_bayar))

    def ubahPembayaran(self, pembayaran_id, pengiriman_id, metode, jumlah, status_bayar, tanggal_bayar):
        sql = """
            UPDATE pembayaran
            SET pengiriman_id=%s, metode=%s, jumlah=%s, status_bayar=%s, tanggal_bayar=%s
            WHERE pembayaran_id=%s
        """
        self.eksekusi(sql, (pengiriman_id, metode, jumlah, status_bayar, tanggal_bayar, pembayaran_id))

    def hapusPembayaran(self, pembayaran_id):
        sql = "DELETE FROM pembayaran WHERE pembayaran_id=%s"
        self.eksekusi(sql, (pembayaran_id,))

    def cariPembayaran(self, pembayaran_id):
        cursor = self.conn.cursor(dictionary=True)
        sql = "SELECT * FROM pembayaran WHERE pembayaran_id=%s"
        cursor.execute(sql, (pembayaran_id,))
        data = cursor.fetchone()
        cursor.close()
        return data

    def tampilPembayaran(self):
        return self.tampilData("pembayaran")

    def cariPembayaranMulti(self, keyword):
        cursor = self.conn.cursor(dictionary=True)
        sql = """
            SELECT * FROM pembayaran
            WHERE pembayaran_id LIKE %s OR pengiriman_id LIKE %s OR metode LIKE %s
            OR jumlah LIKE %s OR status_bayar LIKE %s OR tanggal_bayar LIKE %s
        """
        params = [f"%{keyword}%"] * 6
        cursor.execute(sql, params)
        hasil = cursor.fetchall()
        cursor.close()
        return hasil

    # ====================== KURIR ===========================
    def simpanKurir(self, kurir_id, nama_kurir, no_hp, email, plat_nomor, status):
        sql = """
            INSERT INTO kurir (kurir_id, nama_kurir, no_hp, email, plat_nomor, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.eksekusi(sql, (kurir_id, nama_kurir, no_hp, email, plat_nomor, status))

    def ubahKurir(self, kurir_id, nama_kurir, no_hp, email, plat_nomor, status):
        sql = """
            UPDATE kurir
            SET nama_kurir=%s, no_hp=%s, email=%s, plat_nomor=%s, status=%s
            WHERE kurir_id=%s
        """
        self.eksekusi(sql, (nama_kurir, no_hp, email, plat_nomor, status, kurir_id))

    def hapusKurir(self, kurir_id):
        sql = "DELETE FROM kurir WHERE kurir_id=%s"
        self.eksekusi(sql, (kurir_id,))

    def cariKurir(self, kurir_id):
        cursor = self.conn.cursor(dictionary=True)
        sql = "SELECT * FROM kurir WHERE kurir_id=%s"
        cursor.execute(sql, (kurir_id,))
        data = cursor.fetchone()
        cursor.close()
        return data

    def tampilKurir(self):
        return self.tampilData("kurir")

    def cariKurirMulti(self, keyword=""):
        cursor = self.conn.cursor(dictionary=True)
        sql = """
            SELECT * FROM kurir
            WHERE kurir_id LIKE %s OR nama_kurir LIKE %s OR no_hp LIKE %s
            OR email LIKE %s OR plat_nomor LIKE %s OR status LIKE %s
        """
        params = [f"%{keyword}%"] * 6
        cursor.execute(sql, params)
        hasil = cursor.fetchall()
        cursor.close()
        return hasil

    # ====================== TRACKING ========================
    def simpanTracking(self, tracking_id, pengiriman_id, kurir_id, status, lokasi, waktu_update):
        sql = """
            INSERT INTO tracking (tracking_id, pengiriman_id, kurir_id, status, lokasi, waktu_update)
            VALUES (%s,%s,%s,%s,%s,%s)
        """
        self.eksekusi(sql, (tracking_id, pengiriman_id, kurir_id, status, lokasi, waktu_update))

    def ubahTracking(self, tracking_id, pengiriman_id, kurir_id, status, lokasi, waktu_update):
        sql = """
            UPDATE tracking
            SET pengiriman_id=%s, kurir_id=%s, status=%s, lokasi=%s, waktu_update=%s
            WHERE tracking_id=%s
        """
        self.eksekusi(sql, (pengiriman_id, kurir_id, status, lokasi, waktu_update, tracking_id))

    def hapusTracking(self, tracking_id):
        sql = "DELETE FROM tracking WHERE tracking_id=%s"
        self.eksekusi(sql, (tracking_id,))

    def cariTracking(self, tracking_id):
        cursor = self.conn.cursor(dictionary=True)
        sql = "SELECT * FROM tracking WHERE tracking_id=%s"
        cursor.execute(sql, (tracking_id,))
        data = cursor.fetchone()
        cursor.close()
        return data

    def tampilTracking(self):
        return self.tampilData("tracking")

    def cariTrackingMulti(self, keyword=""):
        cursor = self.conn.cursor(dictionary=True)
        sql = """
            SELECT * FROM tracking
            WHERE tracking_id LIKE %s OR pengiriman_id LIKE %s OR kurir_id LIKE %s
            OR status LIKE %s OR lokasi LIKE %s OR waktu_update LIKE %s
        """
        params = [f"%{keyword}%"] * 6
        cursor.execute(sql, params)
        hasil = cursor.fetchall()
        cursor.close()
        return hasil

    # ====================== PENUTUP ==========================
    def __del__(self):
        try:
            if self.conn.is_connected():
                self.conn.close()
                print("Koneksi database ditutup.")
        except:
            pass
