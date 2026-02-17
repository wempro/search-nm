-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 07, 2026 at 04:37 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `searchdb_bluewhite`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add products', 8, 'add_products'),
(30, 'Can change products', 8, 'change_products'),
(31, 'Can delete products', 8, 'delete_products'),
(32, 'Can view products', 8, 'view_products');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$L1RXfGbA8tlY3054Q4bVLE$fYCYODKUfaqwWIZwBiqQsdsZ9Dw2z6x7McZGnGYc+DE=', '2026-02-02 05:25:54.733890', 1, 'wempro', '', '', 'nur.mohammad@wempro.com', 1, 1, '2023-10-21 03:17:51.169126'),
(2, 'pbkdf2_sha256$600000$9InT0DPrAvH4sseoUY6Vgz$+TDsXLcr2PjHsvYKk1+TraZVp6h8ahoo4h7pA9Nj+Z8=', '2025-12-29 03:14:01.000000', 1, 'rpi.nur@gmail.com', 'Nur', 'Mohammad', 'rpi.nur@gmail.com', 1, 1, '2025-12-29 03:08:29.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
CREATE TABLE IF NOT EXISTS `brand` (
  `id` int NOT NULL AUTO_INCREMENT,
  `textId` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `shortDescription` longtext,
  `details` longtext,
  `status` char(1) NOT NULL DEFAULT 'y',
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `img` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `textId` (`textId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `textId` varchar(50) NOT NULL,
  `categoryTitle` varchar(50) NOT NULL,
  `parrentCategory` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `categoryImage` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `breadcrumbTitle` varchar(100) NOT NULL,
  `categoryUrl` varchar(100) NOT NULL,
  `productCsv` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci,
  `rank` int NOT NULL,
  `status` varchar(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `textId` (`textId`),
  UNIQUE KEY `categoryTitle` (`categoryTitle`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `textId`, `categoryTitle`, `parrentCategory`, `description`, `categoryImage`, `breadcrumbTitle`, `categoryUrl`, `productCsv`, `rank`, `status`, `created`, `updated`) VALUES
(4, 'GAH-series', 'GAH Series', 'root', '', 'category/micropump-l18964-03b-940x724px-1639522903cftXw.png', '', 'GAH-series', '', 0, 'Y', '2026-01-03 06:06:00.355842', '2026-01-03 06:05:59.000000'),
(5, 'GB-Series', 'GB Series', 'root', '', 'category/Micropump-GB-220001_1kRGB.png', '', 'GB-Series', 'PD10P-APS-PTM', 0, 'Y', '2026-01-03 06:08:30.897992', '2026-01-03 06:08:29.000000'),
(6, 'GC-Series', 'GC Series', 'root', '', 'category/images.jfif', '', 'GC-Series', 'PD10P-APS-PTM', 0, 'Y', '2026-01-03 06:13:04.420823', '2026-01-03 06:11:22.000000'),
(3, 'ga-series', 'GA Series', 'root', '', 'category/WEB_Micropump_GA-Series_Image.jpg', '', 'ga-series', '', 0, 'Y', '2026-01-03 05:52:37.161116', '2026-01-03 05:52:13.000000');

-- --------------------------------------------------------

--
-- Table structure for table `categoryitem`
--

DROP TABLE IF EXISTS `categoryitem`;
CREATE TABLE IF NOT EXISTS `categoryitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `textId` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `sub_title` text,
  `url` varchar(100) NOT NULL,
  `sourceUrl` varchar(250) NOT NULL,
  `parrent` varchar(100) DEFAULT 'root',
  `type` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'category',
  `details` text,
  `img` text,
  `status` varchar(5) NOT NULL,
  `rank` int NOT NULL,
  `product_csv` text,
  `series_csv` text,
  `totalPageCount` int DEFAULT NULL,
  `totalListPage` int DEFAULT NULL,
  `queryString` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `textId` (`textId`),
  UNIQUE KEY `sourceUrl` (`sourceUrl`) USING BTREE,
  UNIQUE KEY `url` (`url`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=142 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-12-28 10:21:13.298250', '1', 'Summer Sale (1)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 10, 1),
(2, '2025-12-28 10:21:39.713631', '2', 'New Arrivals (2)', 2, '[]', 10, 1),
(3, '2025-12-28 10:21:47.312221', '1', 'Summer Sale (1)', 2, '[]', 10, 1),
(4, '2025-12-28 10:22:04.436783', '2', 'New Arrivals (2)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 10, 1),
(5, '2025-12-28 10:22:16.494964', '3', 'Best Deals (3)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 10, 1),
(6, '2025-12-28 10:22:53.670939', '4', 'Limited Offer (4)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 10, 1),
(7, '2025-12-28 10:43:47.093000', 'about_us', 'About Us', 2, '[{\"changed\": {\"fields\": [\"Status\", \"Updated\"]}}]', 9, 1),
(8, '2025-12-28 10:44:04.975371', 'featured_products', 'Featured Products', 2, '[{\"changed\": {\"fields\": [\"Status\", \"Updated\"]}}]', 9, 1),
(9, '2025-12-28 10:48:25.962721', 'hero_section', 'Hero Section', 2, '[{\"changed\": {\"fields\": [\"BodyContent\", \"Css\", \"Js\", \"Updated\"]}}]', 9, 1),
(10, '2025-12-28 10:49:04.933427', 'hero_section', 'Hero Section', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 9, 1),
(11, '2025-12-28 11:43:40.944578', '1', 'carousel (1)', 3, '', 11, 1),
(12, '2025-12-28 11:43:40.945593', '7', 'category (2)', 3, '', 11, 1),
(13, '2025-12-28 11:43:40.946583', '8', 'product (3)', 3, '', 11, 1),
(14, '2025-12-28 11:43:40.946583', '9', 'css (4)', 3, '', 11, 1),
(15, '2025-12-28 11:43:40.947592', '5', 'js (5)', 3, '', 11, 1),
(16, '2025-12-28 11:46:10.720427', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\", \"Updated\"]}}]', 11, 1),
(17, '2025-12-28 11:46:58.032220', '3', 'product (3)', 2, '[{\"changed\": {\"fields\": [\"Content\", \"Updated\"]}}]', 11, 1),
(18, '2025-12-28 12:00:54.035835', '2', 'ARO Piston Pumps & Complete Pump Packages (PD05P-ARS-PTT-B, 66605J-344, PD05P-ARS-PTT-Z,666053-0D3)', 1, '[{\"added\": {}}]', 7, 1),
(19, '2025-12-28 12:02:15.285233', '2', 'category (2)', 2, '[]', 11, 1),
(20, '2025-12-28 12:11:24.073105', '4', 'css (4)', 2, '[{\"changed\": {\"fields\": [\"Content\", \"Updated\"]}}]', 11, 1),
(21, '2025-12-28 12:24:35.062051', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(22, '2025-12-28 12:31:16.744817', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(23, '2025-12-28 12:43:37.354547', 'hero_section', 'Hero Section', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 9, 1),
(24, '2025-12-29 03:08:30.002393', '2', 'rpi.nur@gmail.com', 1, '[{\"added\": {}}]', 4, 1),
(25, '2025-12-29 03:11:24.579566', '2', 'rpi.nur@gmail.com', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"User permissions\"]}}]', 4, 1),
(26, '2025-12-29 03:13:50.422003', '2', 'rpi.nur@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\", \"Last login\"]}}]', 4, 1),
(27, '2025-12-29 03:14:18.907391', '2', 'rpi.nur@gmail.com', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 4, 1),
(28, '2026-01-03 05:32:14.651045', '1', 'Summer Sale (1)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 10, 1),
(29, '2026-01-03 05:32:22.374655', '2', 'New Arrivals (2)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 10, 1),
(30, '2026-01-03 05:32:29.929904', '3', 'Best Deals (3)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 10, 1),
(31, '2026-01-03 05:32:44.664658', '4', 'Limited Offer (4)', 3, '', 10, 1),
(32, '2026-01-03 05:32:49.258599', '5', 'Holiday Special (5)', 3, '', 10, 1),
(33, '2026-01-03 05:42:07.336420', '11', 'topContent (6)', 3, '', 11, 1),
(34, '2026-01-03 05:47:10.331593', '13', 'topContent (1)', 1, '[{\"added\": {}}]', 11, 1),
(35, '2026-01-03 05:52:37.162119', '3', 'GA Series ()', 1, '[{\"added\": {}}]', 7, 1),
(36, '2026-01-03 05:57:51.914833', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(37, '2026-01-03 06:01:38.004726', '3', 'GA Series ()', 2, '[{\"changed\": {\"fields\": [\"CategoryImage\"]}}]', 7, 1),
(38, '2026-01-03 06:03:28.029845', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(39, '2026-01-03 06:04:17.295137', '2', 'ARO Piston Pumps & Complete Pump Packages (PD05P-ARS-PTT-B, 66605J-344, PD05P-ARS-PTT-Z,666053-0D3)', 3, '', 7, 1),
(40, '2026-01-03 06:04:22.691073', '1', 'Electronics (PD05P-ARS-PTT-B, 66605J-344, PD05P-ARS-PTT-Z,666053-0D3)', 3, '', 7, 1),
(41, '2026-01-03 06:06:00.355842', '4', 'GAH Series ()', 1, '[{\"added\": {}}]', 7, 1),
(42, '2026-01-03 06:06:34.717822', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(43, '2026-01-03 06:08:10.661442', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(44, '2026-01-03 06:08:30.898993', '5', 'GB Series ()', 1, '[{\"added\": {}}]', 7, 1),
(45, '2026-01-03 06:13:04.420823', '6', 'GC Series ()', 1, '[{\"added\": {}}]', 7, 1),
(46, '2026-01-03 06:13:31.024420', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(47, '2026-01-03 06:13:54.609122', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(48, '2026-01-03 06:23:38.693751', 'hero_section', 'Hero Section', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 12, 1),
(49, '2026-01-03 06:35:34.588357', '1', 'Summer Sale (1)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 10, 1),
(50, '2026-01-03 06:35:44.508181', '2', 'New Arrivals (2)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 10, 1),
(51, '2026-01-03 06:41:15.264280', '3', 'Best Deals (3)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 10, 1),
(52, '2026-01-03 07:05:09.285752', '6', 'GC Series ()', 2, '[{\"changed\": {\"fields\": [\"CategoryUrl\"]}}]', 7, 1),
(53, '2026-01-03 07:05:45.708137', '3', 'GA Series ()', 2, '[{\"changed\": {\"fields\": [\"CategoryUrl\"]}}]', 7, 1),
(54, '2026-01-03 07:06:25.930546', '4', 'GAH Series ()', 2, '[{\"changed\": {\"fields\": [\"CategoryUrl\"]}}]', 7, 1),
(55, '2026-01-03 07:13:45.193558', '6', 'GC Series (PD10P-APS-PTM)', 2, '[{\"changed\": {\"fields\": [\"ProductCsv\"]}}]', 7, 1),
(56, '2026-01-03 07:14:07.539231', '5', 'GB Series (PD10P-APS-PTM)', 2, '[{\"changed\": {\"fields\": [\"ProductCsv\"]}}]', 7, 1),
(57, '2026-01-03 07:14:24.455589', '5', 'GB Series (PD10P-APS-PTM)', 2, '[]', 7, 1),
(58, '2026-01-03 07:17:11.338073', '5', 'GB Series (PD10P-APS-PTM)', 2, '[{\"changed\": {\"fields\": [\"CategoryUrl\"]}}]', 7, 1),
(59, '2026-01-03 08:05:28.617928', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(60, '2026-01-03 08:06:00.138741', '3', 'product (3)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(61, '2026-01-03 09:59:16.640594', '3', 'product (3)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(62, '2026-01-04 06:43:03.394174', '1', 'First Slide (1)', 1, '[{\"added\": {}}]', 10, 1),
(63, '2026-01-04 06:43:44.501288', '2', 'Second Slide (2)', 1, '[{\"added\": {}}]', 10, 1),
(64, '2026-01-04 06:44:29.926210', '3', 'Third Slide (1)', 1, '[{\"added\": {}}]', 10, 1),
(65, '2026-01-04 06:45:12.213244', '4', 'ARO Slide (4)', 1, '[{\"added\": {}}]', 10, 1),
(66, '2026-01-08 07:57:13.747933', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 11, 1),
(67, '2026-01-08 08:15:01.996421', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(68, '2026-01-08 08:15:46.981792', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(69, '2026-01-08 08:21:50.305853', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\", \"Status\"]}}]', 11, 1),
(70, '2026-01-08 08:22:58.197441', '12', 'additional (7)', 2, '[{\"changed\": {\"fields\": [\"Content\", \"Status\", \"Updated\"]}}]', 11, 1),
(71, '2026-01-08 08:23:35.215328', '12', 'additional (7)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(72, '2026-01-08 08:23:46.657759', '4', 'css (4)', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 11, 1),
(73, '2026-01-08 08:28:26.147889', '4', 'css (4)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(74, '2026-01-08 08:28:51.242501', '4', 'css (4)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(75, '2026-01-08 08:30:13.299984', '4', 'css (4)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(76, '2026-01-08 08:32:13.946682', '4', 'css (4)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(77, '2026-01-08 08:32:47.417279', '4', 'css (4)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(78, '2026-01-27 04:48:49.027940', '12', 'additional (7)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(79, '2026-01-27 09:00:03.418863', '13', 'topContent (1)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(80, '2026-01-27 09:01:43.515400', '13', 'topContent (1)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(81, '2026-01-27 09:08:09.860860', '14', 'series (3)', 1, '[{\"added\": {}}]', 11, 1),
(82, '2026-01-27 09:15:16.468817', '2', 'category (2)', 2, '[]', 11, 1),
(83, '2026-01-27 09:15:24.729888', '14', 'series (3)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(84, '2026-01-27 09:30:14.663447', '13', 'topContent (1)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(85, '2026-01-27 09:30:27.239406', '2', 'category (2)', 2, '[]', 11, 1),
(86, '2026-01-27 09:42:05.515746', '14', 'series (3)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(87, '2026-01-27 09:44:45.639056', '14', 'series (3)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(88, '2026-01-27 09:46:22.456686', '3', 'GAH Series', 2, '[{\"changed\": {\"fields\": [\"Type\", \"Details\", \"Img\"]}}]', 13, 1),
(89, '2026-01-27 10:03:54.043920', '4', 'GB Series', 2, '[{\"changed\": {\"fields\": [\"Type\", \"Details\", \"Img\"]}}]', 13, 1),
(90, '2026-01-27 10:04:13.067006', '3', 'GAH Series', 2, '[]', 13, 1),
(91, '2026-01-27 10:05:12.400442', '5', 'GC Series', 2, '[{\"changed\": {\"fields\": [\"Type\", \"Details\", \"Img\"]}}]', 13, 1),
(92, '2026-01-27 10:07:52.970728', '49', 'Magnetic Drive Pumps', 2, '[{\"changed\": {\"fields\": [\"Img\"]}}]', 13, 1),
(93, '2026-01-27 10:12:18.867629', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(94, '2026-01-27 10:15:32.513386', '47', 'Centrifugal Pumps', 2, '[{\"changed\": {\"fields\": [\"Img\"]}}]', 13, 1),
(95, '2026-01-27 10:16:55.922794', '45', 'Gear Pumps', 2, '[{\"changed\": {\"fields\": [\"Img\"]}}]', 13, 1),
(96, '2026-01-27 10:20:26.783272', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(97, '2026-01-27 10:24:48.732443', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(98, '2026-01-27 10:26:06.291034', '13', 'Drives', 2, '[{\"changed\": {\"fields\": [\"Img\"]}}]', 13, 1),
(99, '2026-01-27 10:27:19.082297', '1', 'Pumps', 2, '[{\"changed\": {\"fields\": [\"Img\"]}}]', 13, 1),
(100, '2026-01-27 10:30:04.242140', '2', 'category (2)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(101, '2026-01-27 10:33:06.805888', '45', 'Gear Pumps', 2, '[{\"changed\": {\"fields\": [\"Sub title\"]}}]', 13, 1),
(102, '2026-01-27 10:33:48.371537', '45', 'Gear Pumps', 2, '[{\"changed\": {\"fields\": [\"Details\"]}}]', 13, 1),
(103, '2026-01-27 10:37:24.954270', '1', 'Pumps', 2, '[{\"changed\": {\"fields\": [\"Sub title\"]}}]', 13, 1),
(104, '2026-01-27 10:39:25.288745', '49', 'Magnetic Drive Pumps', 2, '[{\"changed\": {\"fields\": [\"Sub title\"]}}]', 13, 1),
(105, '2026-01-27 10:40:24.614494', '49', 'Magnetic Drive Pumps', 2, '[{\"changed\": {\"fields\": [\"Sub title\", \"Details\"]}}]', 13, 1),
(106, '2026-01-27 10:40:44.277597', '1', 'Pumps', 2, '[{\"changed\": {\"fields\": [\"Sub title\", \"Details\"]}}]', 13, 1),
(107, '2026-01-27 10:43:53.066093', '47', 'Centrifugal Pumps', 2, '[{\"changed\": {\"fields\": [\"Sub title\", \"Details\", \"Product csv\"]}}]', 13, 1),
(108, '2026-01-27 10:46:04.302680', '13', 'Drives', 2, '[{\"changed\": {\"fields\": [\"Sub title\", \"Details\"]}}]', 13, 1),
(109, '2026-01-27 10:48:42.965387', '13', 'topContent (1)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(110, '2026-01-27 10:50:13.824139', '13', 'topContent (1)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(111, '2026-01-27 12:22:10.053876', '12', 'additional (7)', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 11, 1),
(112, '2026-01-27 12:29:42.402979', '14', 'series (3)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(113, '2026-01-27 12:31:05.148232', '14', 'series (3)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(114, '2026-01-27 13:03:32.389210', '14', 'series (3)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(115, '2026-01-27 13:04:30.611596', '8', 'GAF Series', 2, '[{\"changed\": {\"fields\": [\"Type\", \"Details\", \"Product csv\"]}}]', 13, 1),
(116, '2026-01-27 13:06:44.461379', '20', 'DB-380.A', 2, '[{\"changed\": {\"fields\": [\"Type\", \"Details\", \"Product csv\"]}}]', 13, 1),
(117, '2026-01-27 13:10:33.692896', '6', 'GD Series', 2, '[{\"changed\": {\"fields\": [\"Type\", \"Details\", \"Product csv\"]}}]', 13, 1),
(118, '2026-01-27 13:11:18.241878', '14', 'series (3)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(119, '2026-01-27 13:14:24.060002', '14', 'series (3)', 2, '[{\"changed\": {\"fields\": [\"Content\"]}}]', 11, 1),
(120, '2026-01-27 13:15:16.167666', '18', 'DP-415A.A', 2, '[{\"changed\": {\"fields\": [\"Type\", \"Details\", \"Product csv\"]}}]', 13, 1),
(121, '2026-01-27 13:41:49.226844', '49', 'Magnetic Drive Pumps', 2, '[{\"changed\": {\"fields\": [\"Product csv\"]}}]', 13, 1),
(122, '2026-01-28 08:22:21.374679', '3', 'GAH Series', 2, '[{\"changed\": {\"fields\": [\"Product csv\"]}}]', 13, 1),
(123, '2026-01-29 07:43:23.045023', '1', 'Pumps', 2, '[{\"changed\": {\"fields\": [\"Url\"]}}]', 13, 1),
(124, '2026-01-29 07:46:47.045352', '1', 'Pumps', 2, '[{\"changed\": {\"fields\": [\"Url\"]}}]', 13, 1),
(125, '2026-01-29 08:29:21.326968', '1', 'Pumps', 2, '[{\"changed\": {\"fields\": [\"Url\"]}}]', 13, 1),
(126, '2026-02-01 05:17:50.705994', '12', 'All Categories (category)', 2, '[{\"changed\": {\"fields\": [\"BreadcrumbTree\"]}}]', 14, 1),
(127, '2026-02-01 05:24:42.771519', '13', 'All Products list views (all-products)', 2, '[{\"changed\": {\"fields\": [\"SeoTitle\", \"MetaDescription\"]}}]', 14, 1),
(128, '2026-02-01 05:25:08.212630', '13', 'All Products list views (all-products)', 2, '[{\"changed\": {\"fields\": [\"CanonicalUrl\"]}}]', 14, 1),
(129, '2026-02-01 05:27:52.070612', '12', 'All Categories (category)', 2, '[{\"changed\": {\"fields\": [\"CanonicalUrl\"]}}]', 14, 1),
(130, '2026-02-01 05:31:29.653239', '12', 'All Categories (category)', 2, '[{\"changed\": {\"fields\": [\"BreadcrumbTree\"]}}]', 14, 1),
(131, '2026-02-01 05:46:15.266840', '49', 'Magnetic Drive Pumps', 2, '[{\"changed\": {\"fields\": [\"Product csv\"]}}]', 13, 1),
(132, '2026-02-01 05:46:46.785281', '49', 'Magnetic Drive Pumps', 2, '[{\"changed\": {\"fields\": [\"Product csv\"]}}]', 13, 1),
(133, '2026-02-01 06:06:30.244152', '2', 'Micropump Gear Pumps | Small Magnetically-Driven Fluid Systems (home)', 2, '[{\"changed\": {\"fields\": [\"SeoTitle\", \"MetaDescription\"]}}]', 14, 1),
(134, '2026-02-01 07:13:29.747705', '7', 'Micropump 20061, Drive | Micropump (20061)', 3, '', 14, 1),
(135, '2026-02-02 03:47:56.215652', '18', 'DP-415A.A', 2, '[{\"changed\": {\"fields\": [\"Product csv\"]}}]', 13, 1),
(136, '2026-02-02 04:31:18.585163', '10', 'All Products list view (all-products)', 3, '', 14, 1),
(137, '2026-02-02 04:31:52.835557', '12', 'All Products list view (all-products)', 2, '[{\"changed\": {\"fields\": [\"BreadcrumbTree\"]}}]', 14, 1),
(138, '2026-02-02 04:32:47.527261', '12', 'All Products list view (all-products)', 2, '[{\"changed\": {\"fields\": [\"BreadcrumbTree\"]}}]', 14, 1),
(139, '2026-02-02 04:35:10.015299', '11', 'All Categories (category)', 3, '', 14, 1),
(140, '2026-02-03 19:52:27.215932', '11', 'Expert Series', 2, '[{\"changed\": {\"fields\": [\"Url\"]}}]', 13, 1),
(141, '2026-02-03 21:50:43.079310', '2', 'Pneumatic Logic Controls (pneumatic-logic-controls)', 3, '', 15, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'category', 'category'),
(8, 'searchApp', 'products'),
(9, 'homeScreen', 'homepagecontent'),
(10, 'homeScreen', 'slide'),
(11, 'homeScreen', 'homeconfig'),
(12, 'homeScreen', 'sectioncontent'),
(13, 'searchApp', 'categoryitem'),
(14, 'searchApp', 'metadata'),
(15, 'searchApp', 'productitem');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-10-20 19:46:45.972035'),
(2, 'auth', '0001_initial', '2023-10-20 19:46:46.728243'),
(3, 'admin', '0001_initial', '2023-10-20 19:46:47.051161'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-10-20 19:46:47.064661'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-10-20 19:46:47.080285'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-10-20 19:46:47.245428'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-10-20 19:46:47.319667'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-10-20 19:46:47.389469'),
(9, 'auth', '0004_alter_user_username_opts', '2023-10-20 19:46:47.407423'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-10-20 19:46:47.477768'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-10-20 19:46:47.480760'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-10-20 19:46:47.494761'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-10-20 19:46:47.604511'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-10-20 19:46:47.709903'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-10-20 19:46:47.829634'),
(16, 'auth', '0011_update_proxy_permissions', '2023-10-20 19:46:47.859252'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-10-20 19:46:47.942369'),
(18, 'category', '0001_initial', '2023-10-20 19:46:47.962589'),
(19, 'sessions', '0001_initial', '2023-10-21 02:57:36.793088'),
(20, 'searchApp', '0001_initial', '2023-10-21 02:57:52.274333'),
(21, 'searchApp', '0002_products_producttitle_products_seriesid', '2023-10-21 03:00:32.634519'),
(22, 'searchApp', '0003_remove_products_producttitle_and_more', '2023-10-21 03:00:32.697399'),
(23, 'searchApp', '0004_products_producttitle_products_seriesid', '2023-10-21 03:01:19.915679'),
(24, 'searchApp', '0005_products_description_products_price_and_more', '2023-10-21 03:02:58.023617'),
(25, 'searchApp', '0006_products_additional1_products_additional2_and_more', '2023-10-21 03:03:41.646017'),
(26, 'searchApp', '0007_file_alter_products_additional1_and_more', '2023-10-24 07:23:34.803611');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('o2i9vkw4351irs4incuuo89v8x3etroo', 'e30:1qu3Fc:0I4p4GmBpz6RWaWz9xXG9zYUU6QDqUbKK2IYp2y520M', '2023-11-04 04:06:12.355986'),
('5itxt2vj1cvb72mkce0qxsq730rw2aki', 'e30:1r3VuC:ptqvvpaOyoe3uACiGkoiDIfekztIPQoL2pxq-BZRRnU', '2023-11-30 06:31:12.867179'),
('5r41kjqo9vusrj8u0r9kim4qopi72fzk', 'e30:1r3Vuo:uA8ZkTl4n8XVPL7vN2NDJ8UuwH6bCyG3TEpnZ4A1Rxk', '2023-11-30 06:31:50.283660'),
('xb3hru1av72exbsy7zbdrjj21et2cy1q', '.eJxVjEEOwiAQRe_C2pCBAqJL9z0DGRhGqgaS0q6Md7dNutDte-__twi4LiWsPc9hInEVSpx-WcT0zHUX9MB6bzK1usxTlHsiD9vl2Ci_bkf7d1Cwl20NyAmUJaWsJ7YWM2hmi1Y7f4l-gGjYJTIIwJGQkmeFxmkeznGDLD5f9Hg4pA:1qubUX:0-Uz1wrY8GKj6eWz4TwZbBjrjf35mP74O4d1KvHrz-M', '2023-11-05 16:39:53.630087'),
('esz1c0excypsgdiq1r00dyxzd5aq0cdv', '.eJxVjEEOwiAQRe_C2pCBAqJL9z0DGRhGqgaS0q6Md7dNutDte-__twi4LiWsPc9hInEVSpx-WcT0zHUX9MB6bzK1usxTlHsiD9vl2Ci_bkf7d1Cwl20NyAmUJaWsJ7YWM2hmi1Y7f4l-gGjYJTIIwJGQkmeFxmkeznGDLD5f9Hg4pA:1qur30:g5HpwE_v_yr7IEouaPIYtpdKJ7tZyaKtywXWaKwvp7g', '2023-11-06 09:16:30.858061'),
('5owbnqe1xeyjz4hl7qm6nsjqcqqtwab0', 'e30:1r3hC9:dm_wfhIju1NBFbIc-2cskH2Xfa_l7oExTPiVpS-1AYs', '2023-11-30 18:34:29.295664'),
('whc3q5ay6xucluu4h4ev8c0uettv39vg', 'e30:1r3hDQ:jO6SwtWD8Eb1tGtMd_rxsBsaiDIbUthqdVbRhs6gMqI', '2023-11-30 18:35:48.389777'),
('kql23hdsgmzl5yqu2d7kkt9xvgk8jv9o', 'e30:1r3hIM:e_Cwr3rSTjvF6-AcPA2veLQmmSYJ07QlrWmkPTkLdXs', '2023-11-30 18:40:54.257818'),
('lzromo1la1wgpo2ksi55p196mrxlz38i', 'e30:1r3hJ1:_BmLiSzCbW4nMI798_0ohP0r3tf1SKd9x0oMaCINaDs', '2023-11-30 18:41:35.570269'),
('4rbmi6v444qerjdrflqi0msc21zrgqa5', '.eJxVjEEOwiAQRe_C2pCBAqJL9z0DGRhGqgaS0q6Md7dNutDte-__twi4LiWsPc9hInEVSpx-WcT0zHUX9MB6bzK1usxTlHsiD9vl2Ci_bkf7d1Cwl20NyAmUJaWsJ7YWM2hmi1Y7f4l-gGjYJTIIwJGQkmeFxmkeznGDLD5f9Hg4pA:1r3pd6:4b-lGOcQ_J1Bk6LZeDXlQrRvuioV21C6HaPY5RxlfLQ', '2023-12-01 03:34:52.933234'),
('mk3zcf808olxxjw63l8lklyr0c3tstzy', '.eJxVjDsOwjAQBe_iGll27E0iSnrOEO3HiwPIluKkQtwdIqWA9s3Me5kJtzVPW0vLNIs5G29OvxshP1LZgdyx3KrlWtZlJrsr9qDNXquk5-Vw_w4ytvytowNSUuUgEMbIFEcWJd8zuI47EBx4kBEjQuAhsToQ11GIPXgUVfP-AA70OQ4:1vZmu9:MIZOFFvQY6CmV3dmaqm3EExrbccEr9Z_M_fnCId68lY', '2026-01-11 09:17:37.844572'),
('mla12v9a7jsyzg2n9koprtpv0zww9gbr', '.eJxVjDsOwjAQBe_iGll27E0iSnrOEO3HiwPIluKkQtwdIqWA9s3Me5kJtzVPW0vLNIs5G29OvxshP1LZgdyx3KrlWtZlJrsr9qDNXquk5-Vw_w4ytvytowNSUuUgEMbIFEcWJd8zuI47EBx4kBEjQuAhsToQ11GIPXgUVfP-AA70OQ4:1vc4R3:Hlexz9j8HcTTqvATOvtSLOmlaL6X4cJLXWlwE913M1I', '2026-01-17 16:25:01.175126'),
('ezkmjsbp5j5vn1i7x4rrwtk014jek1np', '.eJxVjDsOwjAQBe_iGll27E0iSnrOEO3HiwPIluKkQtwdIqWA9s3Me5kJtzVPW0vLNIs5G29OvxshP1LZgdyx3KrlWtZlJrsr9qDNXquk5-Vw_w4ytvytowNSUuUgEMbIFEcWJd8zuI47EBx4kBEjQuAhsToQ11GIPXgUVfP-AA70OQ4:1vkazg:8f0JbcvVoi7Q3HNgeu_chCJYh6Kfw-sL4mJuk_xCsSA', '2026-02-10 04:48:00.686896'),
('c6k0r8kkp44lxst1lmyta1wtgviw433e', '.eJxVjDsOwjAQBe_iGll27E0iSnrOEO3HiwPIluKkQtwdIqWA9s3Me5kJtzVPW0vLNIs5G29OvxshP1LZgdyx3KrlWtZlJrsr9qDNXquk5-Vw_w4ytvytowNSUuUgEMbIFEcWJd8zuI47EBx4kBEjQuAhsToQ11GIPXgUVfP-AA70OQ4:1vmmRe:2Y4yylOZ7Sn9_U7LOGpSRrNFVJmIhEaK4ZoJN_k8TdE', '2026-02-16 05:25:54.736917');

-- --------------------------------------------------------

--
-- Table structure for table `homeconfig`
--

DROP TABLE IF EXISTS `homeconfig`;
CREATE TABLE IF NOT EXISTS `homeconfig` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `sectionType` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `rank` int UNSIGNED NOT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `status` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_homeconfig_rank` (`rank`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `homeconfig`
--

INSERT INTO `homeconfig` (`id`, `sectionType`, `rank`, `content`, `status`, `created`, `updated`) VALUES
(2, 'category', 2, '<p>drives, pumps, gear-pumps, magnetic-drive-pumps, centrifugal-pumps</p>', 'active', '2025-12-28 11:42:22.209414', '2025-12-28 11:46:09.000000'),
(3, 'product', 3, '<p><a href=\"http://127.0.0.1:8000/admin/searchApp/products/4/change/\">L20477</a>,&nbsp;<a href=\"http://127.0.0.1:8000/admin/searchApp/products/3/change/\">L23918</a>,<a href=\"http://127.0.0.1:8000/admin/searchApp/products/26/change/\">85465</a>,<a href=\"http://127.0.0.1:8000/admin/searchApp/products/25/change/\">L28068</a></p>', 'active', '2025-12-28 11:42:22.209414', '2025-12-28 11:46:57.000000'),
(4, 'css', 4, '<p>.nur { color: red;}</p>\r\n\r\n<p>.nur strong{</p>\r\n\r\n<p>font-size: 36px;}</p>', 'active', '2025-12-28 11:42:22.209414', '2025-12-28 12:11:23.000000'),
(6, 'carousel', 1, '<p>Homepage carousel section</p>', 'active', '2025-12-28 15:27:15.000000', NULL),
(10, 'js', 5, '// Custom JavaScript', 'inactive', '2025-12-28 15:27:15.000000', NULL),
(12, 'additional', 7, '<p><strong>this is Additional content section ----</strong></p>', 'inactive', '2025-12-28 15:27:15.000000', '2026-01-08 08:22:56.000000'),
(13, 'topContent', 1, '<h1 class=\"page-title\">Industrial Pumps, Magnetic Drive &amp; Centrifugal Pumps | Reliable Solutions</h1>\r\n\r\n<p>Micropump, an industry leader in small, positive-displacement, magnetically-driven gear pumps, provide pump, motor and controller technologies for fluid handling system assemblies. Micropump uses magnetic drives in standard and custom designs or the EagleDrive electromagnetic drive technology to make both dynamic pump and positive displacement products. Micropump pumps are used in the following applications: aerospace &amp; aircraft, environmental, food &amp; beverage, biotech, automotive, chemical processing, medical equipment &amp; devices, paint &amp; inks, pharmaceutical &amp; cosmetics, energy/fuel, electronics, clinical &amp; analytical lab.</p>', 'active', '2026-01-03 05:47:10.329195', '2026-01-03 05:47:06.000000'),
(14, 'series', 3, '<p>GC-Series,&nbsp;GB-Series,&nbsp;GAH-series,glh-series, gj-series, ga-series,&nbsp;db-380a,&nbsp;DC-306.A,&nbsp;gj-series,&nbsp;gaf-series,&nbsp;gd-series,&nbsp;dp-415aa</p>', 'active', '2026-01-27 09:08:09.857259', '2026-01-27 09:07:07.000000');

-- --------------------------------------------------------

--
-- Table structure for table `metadata`
--

DROP TABLE IF EXISTS `metadata`;
CREATE TABLE IF NOT EXISTS `metadata` (
  `id` int NOT NULL AUTO_INCREMENT,
  `textId` varchar(100) NOT NULL,
  `seoTitle` varchar(100) NOT NULL,
  `metaDescription` text NOT NULL,
  `canonicalUrl` varchar(100) DEFAULT NULL,
  `breadcrumbTree` varchar(250) NOT NULL,
  `status` varchar(5) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `textId` (`textId`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `metadata`
--

INSERT INTO `metadata` (`id`, `textId`, `seoTitle`, `metaDescription`, `canonicalUrl`, `breadcrumbTree`, `status`, `created_at`) VALUES
(1, 'home', 'Home Page', 'Welcome to our home page.', '/', '[]', 'y', '2026-02-02 05:24:59'),
(2, 'pro-series', 'Pro Series | aro', 'Pro Series', 'pro-series', '[{\"name\": \"root\", \"link\": \"/category/root\"}, {\"name\": \"aro-diaphragm-pumps\", \"link\": \"/category/root/aro-diaphragm-pumps\"}, {\"name\": \"pro-series\", \"link\": null}]', 'y', '2026-02-05 06:54:54'),
(3, 'piston-pumps-packages', 'Piston Pumps & Packages | aro', 'Piston Pumps & Packages', 'piston-pumps-packages', '[{\"name\": \"root\", \"link\": \"/category/root\"}, {\"name\": \"piston-pumps-packages\", \"link\": null}]', 'y', '2026-02-05 06:55:01'),
(4, 'piston-pump-parts-accessories', 'Piston Pump Parts & Accessories | aro', 'Piston Pump Parts & Accessories', 'piston-pump-parts-accessories', '[{\"name\": \"root\", \"link\": \"/category/root\"}, {\"name\": \"piston-pumps-packages\", \"link\": \"/category/root/piston-pumps-packages\"}, {\"name\": \"piston-pump-parts-accessories\", \"link\": null}]', 'y', '2026-02-05 06:55:08'),
(5, 'evo-electric-pumps', 'EVO-Electric Pumps | aro', 'EVO-Electric Pumps', 'evo-electric-pumps', '[{\"name\": \"root\", \"link\": \"/category/root\"}, {\"name\": \"evo-electric-pumps\", \"link\": null}]', 'y', '2026-02-05 06:55:19'),
(6, '2-series-non-metallic', '2\" Series Non-Metallic | aro', '2\" Series Non-Metallic', '2-series-non-metallic', '[{\"name\": \"root\", \"link\": \"/category/root\"}, {\"name\": \"evo-electric-pumps\", \"link\": \"/category/root/evo-electric-pumps\"}, {\"name\": \"2-series-non-metallic\", \"link\": null}]', 'y', '2026-02-05 06:55:27'),
(7, 'all-products', 'All Products list view', 'Browse all products available on our platform.', 'all-products', '[{\"name\": \"Show all products\", \"link\": null}]', 'y', '2026-02-05 15:25:27');

-- --------------------------------------------------------

--
-- Table structure for table `productitem`
--

DROP TABLE IF EXISTS `productitem`;
CREATE TABLE IF NOT EXISTS `productitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `textId` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `url` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sourceUrl` varchar(250) NOT NULL,
  `brand` varchar(100) DEFAULT NULL,
  `series` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `img` text,
  `stock` text,
  `category_title` text,
  `status` varchar(5) NOT NULL,
  `rank` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id` (`textId`),
  UNIQUE KEY `url` (`url`),
  UNIQUE KEY `sourceUrl` (`sourceUrl`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
CREATE TABLE IF NOT EXISTS `products` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `productID` varchar(50) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `productTitle` varchar(100) NOT NULL,
  `seriesID` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `price` varchar(100) NOT NULL,
  `productImage` longtext NOT NULL,
  `searchUrl` varchar(100) NOT NULL,
  `shortDescription` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `additional1` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci,
  `additional2` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci,
  `additional3` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci,
  `esUrl` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `pniUrl` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `tabData` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci,
  `rank` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `productID` (`productID`),
  UNIQUE KEY `productTitle` (`productTitle`),
  UNIQUE KEY `searchUrl` (`searchUrl`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `products2`
--

DROP TABLE IF EXISTS `products2`;
CREATE TABLE IF NOT EXISTS `products2` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `productID` varchar(50) NOT NULL,
  `productTitle` varchar(100) NOT NULL,
  `seriesID` varchar(50) NOT NULL,
  `description` varchar(250) NOT NULL,
  `price` varchar(100) NOT NULL,
  `productImage` varchar(250) NOT NULL,
  `searchUrl` varchar(100) NOT NULL,
  `shortDescription` varchar(255) NOT NULL,
  `additional1` varchar(250) NOT NULL,
  `additional2` varchar(250) NOT NULL,
  `additional3` varchar(250) NOT NULL,
  `esUrl` varchar(100) NOT NULL,
  `pniUrl` varchar(100) NOT NULL,
  `tabData` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `productID` (`productID`),
  UNIQUE KEY `productTitle` (`productTitle`),
  UNIQUE KEY `seriesID` (`seriesID`),
  UNIQUE KEY `searchUrl` (`searchUrl`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `searchapp_file`
--

DROP TABLE IF EXISTS `searchapp_file`;
CREATE TABLE IF NOT EXISTS `searchapp_file` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `sectioncontent`
--

DROP TABLE IF EXISTS `sectioncontent`;
CREATE TABLE IF NOT EXISTS `sectioncontent` (
  `textId` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `sectionTitle` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `bodyContent` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `css` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `js` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `status` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `rank` int NOT NULL DEFAULT '0',
  `created` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`textId`),
  KEY `idx_homepagecontent_rank` (`rank`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `sectioncontent`
--

INSERT INTO `sectioncontent` (`textId`, `sectionTitle`, `bodyContent`, `css`, `js`, `status`, `rank`, `created`, `updated`) VALUES
('about_us', 'About Us', '<p>Learn more about our company</p>', '', '', 'inactive', 4, '2025-12-28 15:30:37.000000', '2025-12-28 10:43:45.000000'),
('featured_products', 'Featured Products', '<p>Check out our top products</p>', '', '', 'inactive', 2, '2025-12-28 15:30:37.000000', '2025-12-28 10:44:03.000000'),
('hero_section', 'Hero Section', '<h1>At ARO, We Make Success Flow!</h1>\r\n\r\n<p>For more than 95 years ARO has been a leading global manufacturer of fluid handling products, expertly engineered to deliver performance and reliability</p>', '<p>/* Custom CSS */</p>', '<p>// Custom JS</p>', 'inactive', 1, '2025-12-28 15:30:37.000000', '2025-12-28 10:48:25.000000'),
('newsletter', 'Newsletter Signup', '<p>Subscribe to our newsletter</p>', '', '', 'inactive', 3, '2025-12-28 15:30:37.000000', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `seriesitem`
--

DROP TABLE IF EXISTS `seriesitem`;
CREATE TABLE IF NOT EXISTS `seriesitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `textId` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `brand` varchar(100) DEFAULT NULL,
  `sub_title` text,
  `url` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `type` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'series',
  `details` text,
  `img` text,
  `status` varchar(5) NOT NULL,
  `rank` int NOT NULL,
  `product_csv` text,
  `category` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `textId` (`textId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `slide`
--

DROP TABLE IF EXISTS `slide`;
CREATE TABLE IF NOT EXISTS `slide` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` longtext,
  `image` varchar(255) DEFAULT NULL,
  `rank` int DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `slide`
--

INSERT INTO `slide` (`id`, `title`, `description`, `image`, `rank`, `status`, `created`) VALUES
(1, 'First Slide', '', 'slides/slide1_WpGEW88.png', 1, 'active', '2026-01-04 06:43:03'),
(2, 'Second Slide', '', 'slides/slide2_8FhRJls.png', 2, 'active', '2026-01-04 06:43:45'),
(3, 'Third Slide', '', 'slides/slide3_Nj1ufg3.png', 1, 'active', '2026-01-04 06:44:30'),
(4, 'ARO Slide', '', 'slides/aro_9P1WY9p.jpg', 4, 'inactive', '2026-01-04 06:45:12');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
