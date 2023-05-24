CREATE DATABASE  IF NOT EXISTS `worldbuilding` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `worldbuilding`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: worldbuilding
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `significantcharacters`
--

DROP TABLE IF EXISTS `significantcharacters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `significantcharacters` (
  `characterid` int NOT NULL,
  `firstname` varchar(200) DEFAULT NULL,
  `familyname` varchar(200) DEFAULT NULL,
  `alias` varchar(200) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `occupation` varchar(200) DEFAULT NULL,
  `characterdescription` mediumtext,
  PRIMARY KEY (`characterid`),
  CONSTRAINT `significantcharacters_ibfk_1` FOREIGN KEY (`characterid`) REFERENCES `characters` (`characterid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `significantcharacters`
--

LOCK TABLES `significantcharacters` WRITE;
/*!40000 ALTER TABLE `significantcharacters` DISABLE KEYS */;
INSERT INTO `significantcharacters` VALUES (2,'Alotta','Datta','The Clever',32,'Void Developer','I forgor...\n'),(8,'Anne','Ri','The Dependable',22,'Hunter','Placeholder\n\n\n\nhello world\n'),(2444,'Nicolas','Ångnell','The Awesome',23,'Student',NULL),(2447,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `significantcharacters` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-24 11:12:09
