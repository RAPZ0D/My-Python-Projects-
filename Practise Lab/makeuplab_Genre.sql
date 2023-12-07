-- MySQL dump 10.13  Distrib 8.0.34, for macos13 (arm64)
--
-- Host: localhost    Database: makeuplab
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
-- Table structure for table `Genre`
--

DROP TABLE IF EXISTS `Genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Genre` (
  `genre_id` int NOT NULL AUTO_INCREMENT,
  `playlist_genre` text,
  PRIMARY KEY (`genre_id`)
) ENGINE=InnoDB AUTO_INCREMENT=658 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Genre`
--

LOCK TABLES `Genre` WRITE;
/*!40000 ALTER TABLE `Genre` DISABLE KEYS */;
INSERT INTO `Genre` VALUES (1,'edm'),(2,'latin'),(3,'edm'),(4,'rock'),(5,'r&b'),(6,'edm'),(7,'latin'),(8,'edm'),(9,'edm'),(10,'pop'),(11,'rap'),(12,'r&b'),(13,'rap'),(14,'latin'),(15,'edm'),(16,'rock'),(17,'r&b'),(18,'edm'),(19,'rap'),(20,'edm'),(21,'rock'),(22,'r&b'),(23,'pop'),(24,'r&b'),(25,'rock'),(26,'edm'),(27,'r&b'),(28,'pop'),(29,'rap'),(30,'rap'),(31,'pop'),(32,'edm'),(33,'r&b'),(34,'edm'),(35,'r&b'),(36,'edm'),(37,'rock'),(38,'r&b'),(39,'rap'),(40,'rap'),(41,'latin'),(42,'rock'),(43,'pop'),(44,'pop'),(45,'pop'),(46,'pop'),(47,'edm'),(48,'latin'),(49,'latin'),(50,'rap'),(51,'rock'),(52,'rap'),(53,'rock'),(54,'rap'),(55,'pop'),(56,'pop'),(57,'edm'),(58,'pop'),(59,'edm'),(60,'rock'),(61,'edm'),(62,'rock'),(63,'pop'),(64,'latin'),(65,'edm'),(66,'rap'),(67,'pop'),(68,'rock'),(69,'edm'),(70,'edm'),(71,'rap'),(72,'edm'),(73,'pop'),(74,'rock'),(75,'rap'),(76,'r&b'),(77,'rap'),(78,'pop'),(79,'latin'),(80,'rap'),(81,'edm'),(82,'latin'),(83,'rap'),(84,'r&b'),(85,'rap'),(86,'latin'),(87,'edm'),(88,'pop'),(89,'rock'),(90,'r&b'),(91,'latin'),(92,'pop'),(93,'rap'),(94,'latin'),(95,'edm'),(96,'latin'),(97,'latin'),(98,'rap'),(99,'rap'),(100,'pop'),(101,'edm'),(102,'pop'),(103,'latin'),(104,'rap'),(105,'r&b'),(106,'edm'),(107,'r&b'),(108,'rock'),(109,'rap'),(110,'rock'),(111,'edm'),(112,'r&b'),(113,'edm'),(114,'edm'),(115,'rock'),(116,'latin'),(117,'pop'),(118,'edm'),(119,'latin'),(120,'pop'),(121,'rap'),(122,'r&b'),(123,'rock'),(124,'rap'),(125,'r&b'),(126,'latin'),(127,'edm'),(128,'r&b'),(129,'edm'),(130,'edm'),(131,'rap'),(132,'rap'),(133,'r&b'),(134,'pop'),(135,'rock'),(136,'rap'),(137,'rap'),(138,'rap'),(139,'rock'),(140,'latin'),(141,'latin'),(142,'r&b'),(143,'edm'),(144,'edm'),(145,'latin'),(146,'rock'),(147,'rap'),(148,'pop'),(149,'edm'),(150,'pop'),(151,'latin'),(152,'rap'),(153,'latin'),(154,'edm'),(155,'rock'),(156,'r&b'),(157,'rock'),(158,'pop'),(159,'latin'),(160,'edm'),(161,'latin'),(162,'r&b'),(163,'rap'),(164,'rap'),(165,'latin'),(166,'edm'),(167,'edm'),(168,'rock'),(169,'latin'),(170,'r&b'),(171,'rap'),(172,'r&b'),(173,'pop'),(174,'pop'),(175,'edm'),(176,'pop'),(177,'edm'),(178,'rock'),(179,'edm'),(180,'rock'),(181,'pop'),(182,'rap'),(183,'r&b'),(184,'latin'),(185,'latin'),(186,'pop'),(187,'rock'),(188,'edm'),(189,'rock'),(190,'rock'),(191,'pop'),(192,'latin'),(193,'r&b'),(194,'edm'),(195,'latin'),(196,'edm'),(197,'rock'),(198,'r&b'),(199,'rock'),(200,'pop'),(201,'rock'),(202,'rock'),(203,'edm'),(204,'latin'),(205,'latin'),(206,'pop'),(207,'edm'),(208,'rock'),(209,'latin'),(210,'rap'),(211,'pop'),(212,'latin'),(213,'edm'),(214,'rap'),(215,'rock'),(216,'r&b'),(217,'latin'),(218,'rock'),(219,'r&b'),(220,'pop'),(221,'latin'),(222,'pop'),(223,'latin'),(224,'edm'),(225,'latin'),(226,'pop'),(227,'pop'),(228,'edm'),(229,'rap'),(230,'rap'),(231,'latin'),(232,'rock'),(233,'edm'),(234,'latin'),(235,'pop'),(236,'rap'),(237,'latin'),(238,'latin'),(239,'r&b'),(240,'rap'),(241,'r&b'),(242,'pop'),(243,'rap'),(244,'latin'),(245,'edm'),(246,'r&b'),(247,'edm'),(248,'r&b'),(249,'pop'),(250,'edm'),(251,'latin'),(252,'pop'),(253,'pop'),(254,'rap'),(255,'rock'),(256,'rock'),(257,'r&b'),(258,'r&b'),(259,'rap'),(260,'latin'),(261,'rock'),(262,'edm'),(263,'edm'),(264,'rap'),(265,'rock'),(266,'r&b'),(267,'rock'),(268,'edm'),(269,'r&b'),(270,'edm'),(271,'r&b'),(272,'r&b'),(273,'edm'),(274,'r&b'),(275,'rock'),(276,'latin'),(277,'r&b'),(278,'pop'),(279,'pop'),(280,'latin'),(281,'r&b'),(282,'pop'),(283,'edm'),(284,'r&b'),(285,'latin'),(286,'latin'),(287,'r&b'),(288,'rap'),(289,'rap'),(290,'latin'),(291,'pop'),(292,'pop'),(293,'rock'),(294,'r&b'),(295,'pop'),(296,'rap'),(297,'pop'),(298,'rap'),(299,'edm'),(300,'r&b'),(301,'rap'),(302,'rock'),(303,'r&b'),(304,'latin'),(305,'r&b'),(306,'r&b'),(307,'pop'),(308,'rap'),(309,'rock'),(310,'edm'),(311,'pop'),(312,'rap'),(313,'rap'),(314,'rap'),(315,'edm'),(316,'latin'),(317,'rock'),(318,'edm'),(319,'latin'),(320,'edm'),(321,'pop'),(322,'rap'),(323,'latin'),(324,'latin'),(325,'rock'),(326,'r&b'),(327,'latin'),(328,'latin'),(329,'r&b'),(330,'pop'),(331,'latin'),(332,'edm'),(333,'pop'),(334,'rock'),(335,'r&b'),(336,'rap'),(337,'r&b'),(338,'r&b'),(339,'rap'),(340,'edm'),(341,'rap'),(342,'edm'),(343,'edm'),(344,'pop'),(345,'edm'),(346,'latin'),(347,'edm'),(348,'pop'),(349,'latin'),(350,'edm'),(351,'latin'),(352,'r&b'),(353,'latin'),(354,'edm'),(355,'edm'),(356,'pop'),(357,'r&b'),(358,'rap'),(359,'r&b'),(360,'rap'),(361,'rap'),(362,'r&b'),(363,'latin'),(364,'rap'),(365,'pop'),(366,'pop'),(367,'latin'),(368,'rock'),(369,'pop'),(370,'edm'),(371,'edm'),(372,'r&b'),(373,'r&b'),(374,'rap'),(375,'edm'),(376,'r&b'),(377,'rock'),(378,'rap'),(379,'rap'),(380,'r&b'),(381,'rock'),(382,'edm'),(383,'edm'),(384,'latin'),(385,'r&b'),(386,'r&b'),(387,'pop'),(388,'r&b'),(389,'latin'),(390,'pop'),(391,'edm'),(392,'rap'),(393,'r&b'),(394,'r&b'),(395,'rock'),(396,'latin'),(397,'pop'),(398,'rock'),(399,'edm'),(400,'rock'),(401,'latin'),(402,'rap'),(403,'r&b'),(404,'rock'),(405,'rap'),(406,'r&b'),(407,'edm'),(408,'pop'),(409,'rap'),(410,'rock'),(411,'pop'),(412,'rap'),(413,'latin'),(414,'pop'),(415,'rap'),(416,'pop'),(417,'edm'),(418,'pop'),(419,'edm'),(420,'rock'),(421,'r&b'),(422,'r&b'),(423,'latin'),(424,'pop'),(425,'latin'),(426,'pop'),(427,'rock'),(428,'pop'),(429,'rock'),(430,'rock'),(431,'r&b'),(432,'latin'),(433,'latin'),(434,'latin'),(435,'pop'),(436,'pop'),(437,'rap'),(438,'latin'),(439,'rap'),(440,'latin'),(441,'rap'),(442,'rock'),(443,'rock'),(444,'r&b'),(445,'pop'),(446,'rock'),(447,'latin'),(448,'pop'),(449,'rap'),(450,'edm'),(451,'latin'),(452,'rock'),(453,'edm'),(454,'edm'),(455,'edm'),(456,'latin'),(457,'pop'),(458,'rap'),(459,'edm'),(460,'latin'),(461,'rap'),(462,'rap'),(463,'rock'),(464,'r&b'),(465,'edm'),(466,'rap'),(467,'latin'),(468,'edm'),(469,'pop'),(470,'r&b'),(471,'edm'),(472,'latin'),(473,'pop'),(474,'latin'),(475,'pop'),(476,'rock'),(477,'edm'),(478,'r&b'),(479,'edm'),(480,'pop'),(481,'r&b'),(482,'pop'),(483,'latin'),(484,'edm'),(485,'edm'),(486,'edm'),(487,'edm'),(488,'latin'),(489,'r&b'),(490,'rock'),(491,'rock'),(492,'pop'),(493,'edm'),(494,'r&b'),(495,'r&b'),(496,'rap'),(497,'rap'),(498,'rap'),(499,'pop'),(500,'rap'),(501,'rock'),(502,'pop'),(503,'rap'),(504,'rock'),(505,'latin'),(506,'rock'),(507,'edm'),(508,'edm'),(509,'pop'),(510,'latin'),(511,'r&b'),(512,'pop'),(513,'rock'),(514,'rock'),(515,'r&b'),(516,'rock'),(517,'rap'),(518,'rap'),(519,'edm'),(520,'edm'),(521,'pop'),(522,'rock'),(523,'r&b'),(524,'r&b'),(525,'rap'),(526,'pop'),(527,'rock'),(528,'rap'),(529,'edm'),(530,'pop'),(531,'latin'),(532,'rap'),(533,'latin'),(534,'latin'),(535,'rock'),(536,'rock'),(537,'pop'),(538,'edm'),(539,'r&b'),(540,'r&b'),(541,'pop'),(542,'rock'),(543,'edm'),(544,'r&b'),(545,'edm'),(546,'r&b'),(547,'latin'),(548,'r&b'),(549,'rock'),(550,'r&b'),(551,'pop'),(552,'pop'),(553,'latin'),(554,'rock'),(555,'rap'),(556,'pop'),(557,'r&b'),(558,'edm'),(559,'edm'),(560,'r&b'),(561,'rap'),(562,'r&b'),(563,'pop'),(564,'rap'),(565,'pop'),(566,'rock'),(567,'rap'),(568,'pop'),(569,'r&b'),(570,'pop'),(571,'latin'),(572,'latin'),(573,'edm'),(574,'rock'),(575,'r&b'),(576,'pop'),(577,'pop'),(578,'rap'),(579,'r&b'),(580,'r&b'),(581,'rock'),(582,'latin'),(583,'pop'),(584,'rock'),(585,'rock'),(586,'latin'),(587,'pop'),(588,'rock'),(589,'edm'),(590,'latin'),(591,'edm'),(592,'latin'),(593,'latin'),(594,'rap'),(595,'latin'),(596,'rock'),(597,'rock'),(598,'rap'),(599,'rock'),(600,'rock'),(601,'pop'),(602,'r&b'),(603,'r&b'),(604,'rock'),(605,'latin'),(606,'rap'),(607,'pop'),(608,'r&b'),(609,'edm'),(610,'r&b'),(611,'edm'),(612,'r&b'),(613,'r&b'),(614,'rap'),(615,'pop'),(616,'pop'),(617,'pop'),(618,'edm'),(619,'rock'),(620,'r&b'),(621,'rap'),(622,'r&b'),(623,'r&b'),(624,'edm'),(625,'edm'),(626,'pop'),(627,'pop'),(628,'r&b'),(629,'rap'),(630,'latin'),(631,'r&b'),(632,'pop'),(633,'rap'),(634,'rap'),(635,'latin'),(636,'edm'),(637,'latin'),(638,'rock'),(639,'latin'),(640,'rock'),(641,'latin'),(642,'pop'),(643,'pop'),(644,'edm'),(645,'pop'),(646,'pop'),(647,'latin'),(648,'pop'),(649,'r&b'),(650,'r&b'),(651,'edm'),(652,'rap'),(653,'pop'),(654,'r&b'),(655,'pop'),(656,'latin'),(657,'edm');
/*!40000 ALTER TABLE `Genre` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-02 14:47:28
