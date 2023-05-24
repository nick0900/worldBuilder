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
-- Table structure for table `species`
--

DROP TABLE IF EXISTS `species`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `species` (
  `scientificname` varchar(200) NOT NULL,
  `speciesdescription` mediumtext,
  PRIMARY KEY (`scientificname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `species`
--

LOCK TABLES `species` WRITE;
/*!40000 ALTER TABLE `species` DISABLE KEYS */;
INSERT INTO `species` VALUES ('Homo Aviana','The masters of the skies the Avians have the ability to fly. With hollow bones, slender builds, massive chest muscles and wingspans that can reach up to 9m.\nMost of their bodymass is centered around their upper body and arms. The wings are strong enough to launch them up to 3 meters in the air, the highest jumps of any hominid.\nTheir legs are usually quite slim and hardly able to support their weight for far distances. Instead they walk with aid of the knuckles of their great wings, homogenous to a normal Sapien walking on their pinky knuckle.\nThe feet of the avians however are prehensile working like an extra pair of hands as their actual hands are somewhat hard to manouver with the large wings.\nBoasting a great ammount of strength and usually very imposing statures these hominids rank quite low in their capacity for learning and using magic.\n'),('Homo Daeocuprum','Name meaning dreadful copper, to most these nearly extinct hominids are known as copper devils.\nVery little actually known about them except for myths and legend.\nEquipped with razorsharp fins by their ears and wrists with dazzling colours. remains also confirm a large polymorphism between the males and females, of males often showcasing imposing instances of gigantism averaging around 2 meters tall.\nIn legends of ancient times Daeocuprum was said to bestow three times the physical strength of a hominid of similar stature, a fierce temperament that would lay waste in battle and the ability to transform into winged skeletal creatures adorned with a copper like armoured skin.\nFamously it\'s said the Homo Sapiens were once nearly wiped out by them before the discovery of magic which gave the Sapien an edge.\nThese stories and myths should not be considered probable as such physical traits as superhuman sthrength and such extreme transmutation pushes far beyond what is known to be possible in both the biological and magical world.\nIt is believed a small population of them still propogate, and individuals may pop up every once and again. They are however understandably hesitant to making themselves known as the devil hunting of many religious groups stand as partial cause to their near extinction.\n'),('Homo Polypoda','Given a name meaning \"Man With many Feet\" these hominids possess three tentacle appendages originating from their backs just under their rib cages. Throughout their lives these appendages will periodically branch into two as they grow often nearing close to a hundred ends if a polypod lives long enough.\nThese hominids have with quite a lot of leway generally the largest body masses of all hominids with their masses of appendages moving them across the floor.\nWith their imposing and immense bodies their magical capacity is also as expected the lowest of all hominids.\n'),('Homo Sapiens','This is widly considered to be the most physically basic of all hominids having no uniquely extingishing physical features compared to all others.\nHowever, as suggested by their name meaning \"Wise Man\" they make up for their physical weakness for craftyness, ingenuity and their inherit entunement with magic.\nTheir capacity for magic being among the greatest of all hominids.\n'),('Homo Spicaderma','Name meaning spiky skin, these hominids are all about defence.\nOn the fron side of their bodies they possess thick armoured hide, usually covering their stomach, chest, upper arms and upper thighs.\nTogether with this armoured skin they also posess large and sharp spines that splay out when they puff up their chest and torso.\nAdding to the impressive display is striking aposematic coloring and patterns to work as a warning. Most healthy individuals of this hominid has the threatening coloring despite only some sub species are actually venomous.\nWith rather average statures these hominids have good magical capabilities.\n');
/*!40000 ALTER TABLE `species` ENABLE KEYS */;
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
