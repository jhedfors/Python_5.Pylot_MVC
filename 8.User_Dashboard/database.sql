-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: user_dashboard
-- ------------------------------------------------------
-- Server version	5.5.41-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` text,
  `author_id` int(11) NOT NULL,
  `messages_id` int(11) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `modified_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_users1_idx` (`author_id`),
  KEY `fk_comments_messages1_idx` (`messages_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`messages_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (3,'test2',7,6,'2016-05-16 15:30:43','2016-05-16 15:30:43'),(4,'ggggg',7,9,'2016-05-16 16:25:06','2016-05-16 16:25:06'),(5,'hhhh',7,9,'2016-05-16 16:29:38','2016-05-16 16:29:38'),(6,'again\r\n',7,3,'2016-05-16 16:49:25','2016-05-16 16:49:25');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text,
  `recip_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `modified_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users1_idx` (`recip_id`),
  KEY `fk_messages_users2_idx` (`author_id`),
  CONSTRAINT `fk_messages_users1` FOREIGN KEY (`recip_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_messages_users2` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (2,'test',6,6,'2016-05-16 09:32:03','2016-05-16 09:32:03'),(3,'test',7,7,'2016-05-16 13:20:29','2016-05-16 13:20:29'),(4,'tests',6,7,'2016-05-16 13:21:15','2016-05-16 13:21:15'),(5,'again',6,7,'2016-05-16 13:29:57','2016-05-16 13:29:57'),(6,'jeff leaving message for kazu(6)',6,7,'2016-05-16 13:38:13','2016-05-16 13:38:13'),(7,'another',6,7,'2016-05-16 15:49:39','2016-05-16 15:49:39'),(8,'lajsdlfjlasdf',7,7,'2016-05-16 16:13:11','2016-05-16 16:13:11'),(9,'first',7,7,'2016-05-16 16:19:02','2016-05-16 16:19:02');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_level` varchar(45) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `modified_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (6,'Kazu','Hedfors','description','kazu@hedfors.net','$2b$12$lH4X1xLpsPEGv1xR9v2XluclAKjgrpzfZdGG5OkLr6kzb/S7sHzNS','normal','2016-05-16 09:23:15','2016-05-16 09:23:15'),(7,'Jeff','Hedfors',' Sweet!','jeff@hedfors.net','$2b$12$icT5jFG5mS093YKw1PDQe.RUeQZlJ9OnNW6N71stZEj8Rg12WB08O','admin','2016-05-16 13:05:28','2016-05-16 13:05:28'),(9,'Jayden','Hedfors','','jayden@hedfors.net','$2b$12$9vDeMb487O1Q2OxifPxk/.IKVfubb6VenLPybe92YWq51GXv/8Y26','normal','2016-05-16 17:08:41','2016-05-16 17:08:41'),(10,'Keefer','Hedfors','','keefer@hedfors.net','$2b$12$W9hmgykYIRCW6S6T3oaGj.nGYw1.OmoG6Keswf9WX6M4UnLK1MOXq','normal','2016-05-16 17:26:04','2016-05-16 17:26:04');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-16 17:44:04
