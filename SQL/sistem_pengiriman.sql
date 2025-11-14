-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 14, 2025 at 06:22 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sistem_pengiriman`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `nama_admin` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `no_hp` varchar(20) DEFAULT NULL,
  `tanggal_daftar` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `nama_admin`, `email`, `username`, `password`, `no_hp`, `tanggal_daftar`) VALUES
(1, 'Administrator Utama', 'admin@sistem.com', 'admin', 'admin123', '08123456789', '2025-11-05 22:29:46');

-- --------------------------------------------------------

--
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `barang_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `nama_barang` varchar(100) NOT NULL,
  `berat` decimal(5,2) NOT NULL,
  `deskripsi` text DEFAULT NULL,
  `tanggal_input` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`barang_id`, `user_id`, `nama_barang`, `berat`, `deskripsi`, `tanggal_input`) VALUES
(12, 99, 'mouse', 0.53, 'vxe r1', '2024-07-02'),
(22, 54, 'handphone', 1.00, 'iPhone', '2025-12-23'),
(66, 789, 'laptop bekas', 2.00, 'laptop gaming', '2024-01-01');

-- --------------------------------------------------------

--
-- Table structure for table `kurir`
--

CREATE TABLE `kurir` (
  `kurir_id` int(11) NOT NULL,
  `nama_kurir` varchar(100) NOT NULL,
  `no_hp` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `plat_nomor` varchar(20) DEFAULT NULL,
  `status` enum('aktif','nonaktif') DEFAULT 'aktif'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kurir`
--

INSERT INTO `kurir` (`kurir_id`, `nama_kurir`, `no_hp`, `email`, `plat_nomor`, `status`) VALUES
(12, 'agus', '085210398774', 'agus123@gmail.com', 'da 1234 ku', 'aktif'),
(24, 'budi', '081352959546', 'budi321@gmail.com', 'kh 1945 jp', 'nonaktif');

-- --------------------------------------------------------

--
-- Table structure for table `pembayaran`
--

CREATE TABLE `pembayaran` (
  `pembayaran_id` int(11) NOT NULL,
  `pengiriman_id` int(11) NOT NULL,
  `metode` enum('transfer','cod','ewallet') DEFAULT 'transfer',
  `jumlah` decimal(10,2) NOT NULL,
  `status_bayar` enum('belum','sudah') DEFAULT 'belum',
  `tanggal_bayar` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pembayaran`
--

INSERT INTO `pembayaran` (`pembayaran_id`, `pengiriman_id`, `metode`, `jumlah`, `status_bayar`, `tanggal_bayar`) VALUES
(22, 33, 'transfer', 50000.00, 'sudah', '2024-07-02');

-- --------------------------------------------------------

--
-- Table structure for table `pengiriman`
--

CREATE TABLE `pengiriman` (
  `pengiriman_id` int(11) NOT NULL,
  `barang_id` int(11) NOT NULL,
  `asal` varchar(100) NOT NULL,
  `tujuan` varchar(100) NOT NULL,
  `jarak_km` decimal(6,2) DEFAULT NULL,
  `biaya_kirim` decimal(10,2) DEFAULT NULL,
  `status` enum('diproses','dikirim','diterima') DEFAULT 'diproses',
  `tanggal_kirim` date DEFAULT NULL,
  `tanggal_terima` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pengiriman`
--

INSERT INTO `pengiriman` (`pengiriman_id`, `barang_id`, `asal`, `tujuan`, `jarak_km`, `biaya_kirim`, `status`, `tanggal_kirim`, `tanggal_terima`) VALUES
(33, 12, 'Tangerang', 'Banjarmasin', 543.00, 25000.00, 'diterima', '2024-07-02', '2024-07-06');

-- --------------------------------------------------------

--
-- Table structure for table `tracking`
--

CREATE TABLE `tracking` (
  `tracking_id` int(11) NOT NULL,
  `pengiriman_id` int(11) NOT NULL,
  `kurir_id` int(11) DEFAULT NULL,
  `status` enum('dikemas','dikirim','selesai','gagal') NOT NULL DEFAULT 'dikemas',
  `lokasi` varchar(150) DEFAULT NULL,
  `waktu_update` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tracking`
--

INSERT INTO `tracking` (`tracking_id`, `pengiriman_id`, `kurir_id`, `status`, `lokasi`, `waktu_update`) VALUES
(45, 33, 12, 'dikemas', 'Surabaya', '2025-11-08');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`barang_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `kurir`
--
ALTER TABLE `kurir`
  ADD PRIMARY KEY (`kurir_id`);

--
-- Indexes for table `pembayaran`
--
ALTER TABLE `pembayaran`
  ADD PRIMARY KEY (`pembayaran_id`),
  ADD KEY `pengiriman_id` (`pengiriman_id`);

--
-- Indexes for table `pengiriman`
--
ALTER TABLE `pengiriman`
  ADD PRIMARY KEY (`pengiriman_id`),
  ADD KEY `barang_id` (`barang_id`);

--
-- Indexes for table `tracking`
--
ALTER TABLE `tracking`
  ADD PRIMARY KEY (`tracking_id`),
  ADD KEY `pengiriman_id` (`pengiriman_id`),
  ADD KEY `kurir_id` (`kurir_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `barang`
--
ALTER TABLE `barang`
  MODIFY `barang_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6666;

--
-- AUTO_INCREMENT for table `kurir`
--
ALTER TABLE `kurir`
  MODIFY `kurir_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `pembayaran`
--
ALTER TABLE `pembayaran`
  MODIFY `pembayaran_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `pengiriman`
--
ALTER TABLE `pengiriman`
  MODIFY `pengiriman_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `tracking`
--
ALTER TABLE `tracking`
  MODIFY `tracking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pembayaran`
--
ALTER TABLE `pembayaran`
  ADD CONSTRAINT `pembayaran_ibfk_1` FOREIGN KEY (`pengiriman_id`) REFERENCES `pengiriman` (`pengiriman_id`) ON DELETE CASCADE;

--
-- Constraints for table `pengiriman`
--
ALTER TABLE `pengiriman`
  ADD CONSTRAINT `pengiriman_ibfk_1` FOREIGN KEY (`barang_id`) REFERENCES `barang` (`barang_id`) ON DELETE CASCADE;

--
-- Constraints for table `tracking`
--
ALTER TABLE `tracking`
  ADD CONSTRAINT `tracking_ibfk_1` FOREIGN KEY (`pengiriman_id`) REFERENCES `pengiriman` (`pengiriman_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `tracking_ibfk_2` FOREIGN KEY (`kurir_id`) REFERENCES `kurir` (`kurir_id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
