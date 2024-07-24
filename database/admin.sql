-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 19, 2024 at 02:37 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbo2`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(3, 'fid', '$2b$12$PKXoxThVpZAuhOVyM6dtvehGezc2jaUi9HVARZhUkFDaEsvBSemnS'),
(4, 'fid', '$2b$12$.aSFFAYQPY7QtFOipPlEHed4ieFgSUqs0XUBxwks7ZrFTF0rRQJq2'),
(5, 'fid', '$2b$12$spI2neVxNHfIgKWc/6m/detm8RMpx2GQnGCoonv9Pefp3DzcHPuo.'),
(6, 'fid', '$2b$12$bb1aKBCy.ZmuUkOnVkgL8et4AZrrLWrGR95HmKgQLBhrlbeKi6kNe'),
(7, 'fid', '$2b$12$qm77RxYOltONU679KXnODuFAl2aNyTMWShcgSNHU8G7p3zyTEZruS'),
(8, 'fid', '$2b$12$dUQPEqcqUlMNd5TJlR1VhOOnHCwm8mg4V3U9FaHJXihGaCKDZ/JMC'),
(9, 'fid', '$2b$12$NoyN.2oSO8aJXT5janw8HeJZ8U.aJ7FCW88b1EhJnAr1gqzb7fBRy'),
(10, 'fid', '$2b$12$K8mJjrLmFmEpct4vk1HnXueWZq2f1CWNh2yKYrk6ZAznUYLtC0/YK'),
(11, 'fid', '$2b$12$hDE7p5u2qx6nbj9AiCTsc.UhHL/I25Ad8p4wiINNYui0YFwQLG/du'),
(12, 'fid', '$2b$12$QRInnZ359Uo2pMDkKc1sie5jKvTfMBQ4NhaIUwvzkMP03m7eiB33a'),
(13, 'fid', '$2b$12$ZbFFzVcNq8WPz4c2pJ18SOXbfDAf3/NRFMmXKwkC0wglgR84oNEoe'),
(14, 'fid', '$2b$12$bVRKF8lEagCNNo1IGIEWD.Dedp.XmNFHCVccm5IUFOx1EYQD.UgEC'),
(15, 'fid', '$2b$12$WuwzYbkqkGeOMZ6umgU7IeK0xNTala9Lg9RhBLLnxLm07zD/V5lY.'),
(16, 'fid', '$2b$12$lI07YBbmW/H4ajidehQsW.7apZSET2TExcHFYB1MfxQtdQxPC/QMK');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
