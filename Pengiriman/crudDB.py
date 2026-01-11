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
        cursor = self.conn.cursor()
        sql = """
            INSERT INTO barang
            (barang_id, user_id, nama_barang, berat, deskripsi, tanggal_input)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        val = (barang_id, user_id, nama_barang, berat, deskripsi, tanggal_input)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def ubahBarang(self, barang_id, user_id, nama_barang, berat, deskripsi, tanggal_input):
        cursor = self.conn.cursor()
        sql = """
            UPDATE barang
            SET user_id = %s,
                nama_barang = %s,
                berat = %s,
                deskripsi = %s,
                tanggal_input = %s
            WHERE barang_id = %s
        """
        val = (user_id, nama_barang, berat, deskripsi, tanggal_input, barang_id)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def hapusBarang(self, barang_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM barang WHERE barang_id = %s", (barang_id,))
        self.conn.commit()
        affected = cursor.rowcount
        cursor.close()
        return affected

    def dataBarang(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM barang ORDER BY barang_id ASC")
        record = cur.fetchall()
        cur.close()
        return record

    def cariBarang(self, param):
        sql = """
            SELECT * FROM barang
            WHERE barang_id LIKE %s
               OR user_id LIKE %s
               OR nama_barang LIKE %s
               OR berat LIKE %s
               OR deskripsi LIKE %s
               OR tanggal_input LIKE %s
        """
        cur = self.conn.cursor(dictionary=True)
        cur.execute(sql, [
            f"%{param}%", f"%{param}%", f"%{param}%",
            f"%{param}%", f"%{param}%", f"%{param}%"
        ])
        record = cur.fetchall()
        cur.close()
        return record
    # ====================== PENGIRIMAN =======================
    def simpanPengiriman(self, pengiriman_id, barang_id, asal, tujuan, jarak_km, biaya_kirim, status, tanggal_kirim, tanggal_terima):
        cursor = self.conn.cursor()
        sql = """
            INSERT INTO pengiriman
            (pengiriman_id, barang_id, asal, tujuan, jarak_km, biaya_kirim, status, tanggal_kirim, tanggal_terima)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = (pengiriman_id, barang_id, asal, tujuan, jarak_km, biaya_kirim, status, tanggal_kirim, tanggal_terima)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def ubahPengiriman(self, pengiriman_id, barang_id, asal, tujuan, jarak_km, biaya_kirim, status, tanggal_kirim, tanggal_terima):
        cursor = self.conn.cursor()
        sql = """
            UPDATE pengiriman
            SET barang_id = %s,
                asal = %s,
                tujuan = %s,
                jarak_km = %s,
                biaya_kirim = %s,
                status = %s,
                tanggal_kirim = %s,
                tanggal_terima = %s
            WHERE pengiriman_id = %s
        """
        val = (barang_id, asal, tujuan, jarak_km, biaya_kirim, status, tanggal_kirim, tanggal_terima, pengiriman_id)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def hapusPengiriman(self, pengiriman_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM pengiriman WHERE pengiriman_id = %s", (pengiriman_id,))
        self.conn.commit()
        affected = cursor.rowcount
        cursor.close()
        return affected

    def tampilPengiriman(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM pengiriman ORDER BY pengiriman_id ASC")
        record = cur.fetchall()
        cur.close()
        return record

    def cariPengiriman(self, param):
        sql = """
            SELECT * FROM pengiriman
            WHERE pengiriman_id LIKE %s
               OR barang_id LIKE %s
               OR asal LIKE %s
               OR tujuan LIKE %s
               OR jarak_km LIKE %s
               OR biaya_kirim LIKE %s
               OR status LIKE %s
               OR tanggal_kirim LIKE %s
               OR tanggal_terima LIKE %s
        """
        cur = self.conn.cursor(dictionary=True)
        cur.execute(sql, [
            f"%{param}%", f"%{param}%", f"%{param}%",
            f"%{param}%", f"%{param}%", f"%{param}%",
            f"%{param}%", f"%{param}%", f"%{param}%"
        ])
        record = cur.fetchall()
        cur.close()
        return record
    # ====================== PEMBAYARAN =======================
    def simpanPembayaran(self, pembayaran_id, pengiriman_id, metode, jumlah, status_bayar, tanggal_bayar):
        cursor = self.conn.cursor()
        sql = """
            INSERT INTO pembayaran
            (pembayaran_id, pengiriman_id, metode, jumlah, status_bayar, tanggal_bayar)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        val = (pembayaran_id, pengiriman_id, metode, jumlah, status_bayar, tanggal_bayar)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def ubahPembayaran(self, pembayaran_id, pengiriman_id, metode, jumlah, status_bayar, tanggal_bayar):
        cursor = self.conn.cursor()
        sql = """
            UPDATE pembayaran
            SET pengiriman_id = %s,
                metode = %s,
                jumlah = %s,
                status_bayar = %s,
                tanggal_bayar = %s
            WHERE pembayaran_id = %s
        """
        val = (pengiriman_id, metode, jumlah, status_bayar, tanggal_bayar, pembayaran_id)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def hapusPembayaran(self, pembayaran_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM pembayaran WHERE pembayaran_id = %s", (pembayaran_id,))
        self.conn.commit()
        cursor.close()

    def tampilPembayaran(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM pembayaran ORDER BY pembayaran_id ASC")
        record = cur.fetchall()
        cur.close()
        return record

    def cariPembayaranMulti(self, keyword):
        sql = """
            SELECT * FROM pembayaran
            WHERE pembayaran_id LIKE %s
               OR pengiriman_id LIKE %s
               OR metode LIKE %s
               OR jumlah LIKE %s
               OR status_bayar LIKE %s
               OR tanggal_bayar LIKE %s
        """
        cur = self.conn.cursor(dictionary=True)
        like = f"%{keyword}%"
        cur.execute(sql, [like, like, like, like, like, like])
        record = cur.fetchall()
        cur.close()
        return record

    # ====================== KURIR ===========================
    def simpanKurir(self, kurir_id, nama_kurir, no_hp, email, plat_nomor, status):
        cursor = self.conn.cursor()
        sql = """
            INSERT INTO kurir
            (kurir_id, nama_kurir, no_hp, email, plat_nomor, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        val = (kurir_id, nama_kurir, no_hp, email, plat_nomor, status)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def ubahKurir(self, kurir_id, nama_kurir, no_hp, email, plat_nomor, status):
        cursor = self.conn.cursor()
        sql = """
            UPDATE kurir
            SET nama_kurir = %s,
                no_hp = %s,
                email = %s,
                plat_nomor = %s,
                status = %s
            WHERE kurir_id = %s
        """
        val = (nama_kurir, no_hp, email, plat_nomor, status, kurir_id)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def hapusKurir(self, kurir_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM kurir WHERE kurir_id = %s", (kurir_id,))
        self.conn.commit()
        affected = cursor.rowcount
        cursor.close()
        return affected

    def dataKurir(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM kurir ORDER BY kurir_id ASC")
        record = cur.fetchall()
        cur.close()
        return record

    def cariKurir(self, param):
        sql = """
            SELECT * FROM kurir
            WHERE kurir_id LIKE %s
               OR nama_kurir LIKE %s
               OR no_hp LIKE %s
               OR email LIKE %s
               OR plat_nomor LIKE %s
               OR status LIKE %s
        """
        cur = self.conn.cursor(dictionary=True)
        cur.execute(sql, [
            f"%{param}%", f"%{param}%", f"%{param}%",
            f"%{param}%", f"%{param}%", f"%{param}%"
        ])
        record = cur.fetchall()
        cur.close()
        return record

    # ====================== TRACKING ========================
    def simpanTracking(self, tracking_id, pengiriman_id, kurir_id, status, lokasi, waktu_update):
        sql = """
            INSERT INTO tracking
            (tracking_id, pengiriman_id, kurir_id, status, lokasi, waktu_update)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.eksekusi(sql, (tracking_id, pengiriman_id, kurir_id, status, lokasi, waktu_update))

    def ubahTracking(self, tracking_id, pengiriman_id, kurir_id, status, lokasi, waktu_update):
        sql = """
            UPDATE tracking
            SET pengiriman_id=%s,
                kurir_id=%s,
                status=%s,
                lokasi=%s,
                waktu_update=%s
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
            WHERE tracking_id LIKE %s
               OR pengiriman_id LIKE %s
               OR kurir_id LIKE %s
               OR status LIKE %s
               OR lokasi LIKE %s
               OR waktu_update LIKE %s
        """
        params = [f"%{keyword}%"] * 6
        cursor.execute(sql, params)
        hasil = cursor.fetchall()
        cursor.close()
        return hasil

    # ====================== BAYAR ======================
    def simpanBayar(self, kode, nama_barang, harga, jumlah):
        sql = """
            INSERT INTO bayar
            (kode, nama_barang, harga, jumlah)
            VALUES (%s, %s, %s, %s)
        """
        self.eksekusi(sql, (kode, nama_barang, harga, jumlah))


    def ubahBayar(self, kode, nama_barang, harga, jumlah):
        sql = """
            UPDATE bayar
            SET nama_barang=%s,
                harga=%s,
                jumlah=%s
            WHERE kode=%s
        """
        self.eksekusi(sql, (nama_barang, harga, jumlah, kode))


    def cariBayar(self, kode):
        cursor = self.conn.cursor(dictionary=True)
        sql = "SELECT * FROM bayar WHERE kode=%s"
        cursor.execute(sql, (kode,))
        data = cursor.fetchone()
        cursor.close()
        return data


    def tampilBayar(self):
        return self.tampilData("bayar")

    # ====================== PENUTUP ==========================
    def __del__(self):
        try:
            if self.conn.is_connected():
                self.conn.close()
                print("Koneksi database ditutup.")
        except:
            pass
