-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 12, 2021 at 03:19 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Hotel Management`
--

-- --------------------------------------------------------

--
-- Table structure for table `AdminLogin`
--

CREATE TABLE `AdminLogin` (
  `Username` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `AdminLogin`
--

INSERT INTO `AdminLogin` (`Username`, `Password`) VALUES
('ELITE', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `Employee`
--

CREATE TABLE `Employee` (
  `NAME` varchar(30) NOT NULL,
  `AGE` varchar(10) NOT NULL,
  `DOB` varchar(10) NOT NULL,
  `GENDER` varchar(10) NOT NULL,
  `CONTACT` varchar(10) NOT NULL,
  `EMAIL` varchar(30) NOT NULL,
  `ADDRESS` varchar(50) NOT NULL,
  `CITY` varchar(20) NOT NULL,
  `STATE` varchar(20) NOT NULL,
  `DEPARTMENT` varchar(30) NOT NULL,
  `STATUS` varchar(10) NOT NULL,
  `IDPROOF` varchar(30) NOT NULL,
  `TYPE` varchar(20) NOT NULL,
  `SALARY` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Employee`
--

INSERT INTO `Employee` (`NAME`, `AGE`, `DOB`, `GENDER`, `CONTACT`, `EMAIL`, `ADDRESS`, `CITY`, `STATE`, `DEPARTMENT`, `STATUS`, `IDPROOF`, `TYPE`, `SALARY`) VALUES
('S Durga', '21', '14-12-2000', 'Female', '6369046512', 'durga@gmail.com', '16A,Akshaya Apartment', ' Chennai', ' Tamil Nadu', 'Receptionist', 'Active', 'Aadhaar/PAN/DL', 'Permanent', '60000'),
('Dinesh Kumar', '26', '02-12-1996', 'Male', '9873644633', 'dinesh12@gmail.com', '12,Anna Nagar,', ' Chennai', ' Tamil Nadu', 'Food Department', 'Active', 'PAN/Passport/DL', 'Permanent', '50000'),
('Rajesh Kannan', '20', '09-09-2001', 'Female', '7695949396', 'rajhacker@gmail.com', '12,West cross st.', ' Bangalore', ' Karnatakka', 'Receptionist', 'Active', 'Aadhaar/PAN/Passport', 'Temporary', '80000'),
('Shalini R', '22', '21-03-2000', 'Female', '8976654321', 'shalini21@gmail.com', 'Ub city,2nd street', ' Bangalore', ' Karnatakka', 'Food Department', 'Active', 'Aadhaar/PAN/Passport', 'Temporary', '40000'),
('durga', '20', '21-08-2001', 'Female', '9842160648', 'durga@gmail.com', '37', ' Trivandur', ' Kerala', 'Food', 'Inactive', 'Aadhaar/PAN/DL', 'Temporary', '30000');

-- --------------------------------------------------------

--
-- Table structure for table `Food`
--

CREATE TABLE `Food` (
  `STOCKNAME` varchar(30) NOT NULL,
  `QUANTITY` varchar(30) NOT NULL,
  `TOTALCOST` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Food`
--

INSERT INTO `Food` (`STOCKNAME`, `QUANTITY`, `TOTALCOST`) VALUES
('Apples and Pears', '12', 22),
('Bananas and Mangoes ', '21', 21),
('Berries and Melons', '11', 21),
('Leafy green and Root', '12', 20),
('Cruciferous and Marrow', '21', 12),
('Maida and Wheet Flour', '21', 22),
('Special Masala', '12', 22),
('Rice', '21', 222),
('Dessert', '21', 22),
('Diary Products', '21', 22),
('Meat', '11', 12),
('Chicken', '21', 12),
('Beef', '22', 21),
('Eggs', '22', 21),
('Fish', '22', 21);

-- --------------------------------------------------------

--
-- Table structure for table `Room`
--

CREATE TABLE `Room` (
  `NAME` varchar(20) NOT NULL,
  `PHONENO` varchar(10) NOT NULL,
  `ROOMNO` varchar(10) NOT NULL,
  `MEALS` varchar(20) NOT NULL,
  `ROOMTYPE` varchar(20) NOT NULL,
  `CHECKIN` varchar(20) NOT NULL,
  `CHECKOUT` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Room`
--

INSERT INTO `Room` (`NAME`, `PHONENO`, `ROOMNO`, `MEALS`, `ROOMTYPE`, `CHECKIN`, `CHECKOUT`) VALUES
('R Manoj Kumar', '8940132022', '102', 'Taken', 'Single Room', '7/19/21', '7/21/21'),
('S Durga Sri', '6369048512', '106', 'Taken', 'Double Room', '7/22/21', '7/27/21'),
('N Hari Karthik', '1234567890', '104', 'Not Taken', 'Single Room', '7/27/21', '7/29/21'),
('N Shruthi', '6457382976', '101', 'Taken', 'Deluxe', '7/30/21', '8/1/21'),
('R Susmi', '9842652203', '108', 'Taken', 'Single Room', '7/30/21', '7/31/21'),
('Dinesh S', '9004500231', '105', 'Taken', 'Double Room', '7/28/21', '7/31/21');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
