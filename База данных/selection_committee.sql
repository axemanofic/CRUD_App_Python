-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Июл 17 2020 г., 11:28
-- Версия сервера: 8.0.15
-- Версия PHP: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `selection_committee`
--
CREATE DATABASE IF NOT EXISTS `selection_committee` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `selection_committee`;

-- --------------------------------------------------------

--
-- Структура таблицы `direction_ist`
--

DROP TABLE IF EXISTS `direction_ist`;
CREATE TABLE IF NOT EXISTS `direction_ist` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FIO` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `POINTS` int(1) NOT NULL,
  `ORIGINAL` tinyint(1) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `direction_ist`
--

INSERT INTO `direction_ist` (`ID`, `FIO`, `POINTS`, `ORIGINAL`) VALUES
(1, 'AAA', 111, 1),
(2, 'BBB', 200, 0),
(3, 'CCC', 300, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `direction_ivt`
--

DROP TABLE IF EXISTS `direction_ivt`;
CREATE TABLE IF NOT EXISTS `direction_ivt` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FIO` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `POINTS` int(1) NOT NULL,
  `ORIGINAL` tinyint(1) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `direction_ivt`
--

INSERT INTO `direction_ivt` (`ID`, `FIO`, `POINTS`, `ORIGINAL`) VALUES
(1, 'AAA', 111, 1),
(3, 'BBB', 222, 1),
(4, 'CCC', 222, 0),
(5, 'Сотников Роман', 300, 1),
(53, 'Филичев Владимир', 111, 0),
(56, 'Третьякова Екатерина', 111, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
