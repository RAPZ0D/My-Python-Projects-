-- MySQL dump 10.13  Distrib 8.0.34, for macos13 (arm64)
--
-- Host: localhost    Database: lab10
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `EconomicIndicators`
--

DROP TABLE IF EXISTS `EconomicIndicators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EconomicIndicators` (
  `Year` int NOT NULL,
  `CountryID` int NOT NULL,
  `GDP` float DEFAULT NULL,
  `GDPGrowth` float DEFAULT NULL,
  `AdolFertRate` float DEFAULT NULL,
  `AgriValAddGDP` float DEFAULT NULL,
  `DomCreditGDP` float DEFAULT NULL,
  `ExportsGDP` float DEFAULT NULL,
  `FertRate` float DEFAULT NULL,
  `FDINetBoP` float DEFAULT NULL,
  `GNICapAtlas` float DEFAULT NULL,
  `GNIAtlas` float DEFAULT NULL,
  `GrossCapFormGDP` float DEFAULT NULL,
  `ImportsGDP` float DEFAULT NULL,
  `IndValAddGDP` float DEFAULT NULL,
  PRIMARY KEY (`Year`,`CountryID`),
  KEY `CountryID` (`CountryID`),
  CONSTRAINT `economicindicators_ibfk_1` FOREIGN KEY (`CountryID`) REFERENCES `CountryInfo` (`CountryID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EconomicIndicators`
--

LOCK TABLES `EconomicIndicators` WRITE;
/*!40000 ALTER TABLE `EconomicIndicators` DISABLE KEYS */;
/*!40000 ALTER TABLE `EconomicIndicators` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-25  0:43:13
