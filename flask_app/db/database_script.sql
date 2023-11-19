CREATE DATABASE  IF NOT EXISTS `whatsdown` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `whatsdown`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: whatsdown
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `chats`
--

DROP TABLE IF EXISTS `chats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chats` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user1_id` int NOT NULL,
  `user2_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_chats_users1_idx` (`user1_id`),
  KEY `fk_chats_users2_idx` (`user2_id`),
  CONSTRAINT `fk_chats_users1` FOREIGN KEY (`user1_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_chats_users2` FOREIGN KEY (`user2_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chats`
--

LOCK TABLES `chats` WRITE;
/*!40000 ALTER TABLE `chats` DISABLE KEYS */;
INSERT INTO `chats` VALUES (1,1,5,'2023-11-11 20:30:46','2023-11-11 20:30:46'),(2,1,6,'2023-11-11 20:30:46','2023-11-11 20:30:46'),(3,5,2,'2023-11-11 20:30:46','2023-11-11 20:30:46'),(4,5,6,'2023-11-15 19:31:03','2023-11-15 19:31:03'),(5,9,1,'2023-11-15 20:21:06','2023-11-15 20:21:06'),(6,1,3,'2023-11-16 23:24:36','2023-11-16 23:24:36'),(7,3,9,'2023-11-17 00:38:55','2023-11-17 00:38:55'),(8,1,8,'2023-11-18 13:05:57','2023-11-18 13:05:57'),(9,1,4,'2023-11-18 13:19:12','2023-11-18 13:19:12'),(10,1,7,'2023-11-18 20:06:32','2023-11-18 20:06:32'),(11,10,1,'2023-11-18 22:42:20','2023-11-18 22:42:20'),(12,2,10,'2023-11-19 01:53:24','2023-11-19 01:53:24'),(13,2,1,'2023-11-19 01:55:11','2023-11-19 01:55:11');
/*!40000 ALTER TABLE `chats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logins`
--

DROP TABLE IF EXISTS `logins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pwd` varchar(255) DEFAULT NULL,
  `users_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_logins_users_idx` (`users_id`),
  CONSTRAINT `fk_logins_users` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logins`
--

LOCK TABLES `logins` WRITE;
/*!40000 ALTER TABLE `logins` DISABLE KEYS */;
INSERT INTO `logins` VALUES (1,'$2b$12$WI26NWW3tRyO40fOy0iCueDdkhCAZ8CSv3tTRZ7EXyZyKysumeYV.',1),(2,'$2b$12$aGJMNDj9eqHmKhWsKUEOLevy85kVOxt5tYciJOXcgpKVPrQbMMqlO',2),(3,'$2b$12$E7Yl03nXDw9muBuONXT4y.M1P.5/qlYOwoeTinlp4U0K7Bd4ZiDr2',3),(4,'$2b$12$Bp.YUp3WfuG3wkHueulK5OWxsDjqcwvge4JiTNOg.PxN6OH.xuTUK',4),(5,'$2b$12$JOYzbY9tEeaWYAK1UaoujO0hYDKM3hU1dxa5iJRqvzqIe/RIfU7dG',5),(6,'$2b$12$25RRZRJMietfuiPLnrm2YOw4FZDc6E.Yiv3rdSgGzUZfsreWZzKi.',6),(7,'$2b$12$0aoejbu.d3o4a1EPkuaCcOfNj5lJaWjJVc./KRE3efpwF0N2jqo2y',7),(8,'$2b$12$dPKhAiBEtcenBAkwolk4EetJHvi3VUzyj3AUYBygLe9VqmHMZqXZC',8),(9,'$2b$12$P4PdQsP/SGI0q2lupZqa1.eLomRA88H7lOZHXAQvcGPuM.FKn8v52',9),(10,'$2b$12$AFXmAYDMzoy9BfJfKIp9IOm/jj7BmxajgibOkQJkOu1Ih7JoHVdym',10);
/*!40000 ALTER TABLE `logins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` varchar(100) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `chat_id` int NOT NULL,
  `user_id` int NOT NULL,
  `seen` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_chats1_idx` (`chat_id`),
  KEY `fk_messages_users1_idx` (`user_id`),
  CONSTRAINT `fk_messages_chats1` FOREIGN KEY (`chat_id`) REFERENCES `chats` (`id`),
  CONSTRAINT `fk_messages_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'Hola, como va todo?','2023-11-11 20:32:29',1,1,1),(2,'Bien y tu?','2023-11-11 21:17:12',1,5,0),(3,'Vamos a estudiar?','2023-11-11 21:17:12',2,1,1),(4,'sdgadfgs','2023-11-12 06:04:25',1,1,1),(5,'GGFD','2023-11-12 06:10:33',1,1,1),(6,'xxxxxx','2023-11-12 06:23:51',1,1,1),(7,'ssss','2023-11-12 06:24:01',1,1,1),(14,'hey, I am talking','2023-11-12 07:35:53',1,1,1),(15,'oooooo','2023-11-12 08:00:05',1,1,1),(16,'Hey u, reply!','2023-11-12 08:13:35',2,1,1),(17,'hey, I am talking','2023-11-12 08:17:03',1,1,1),(18,'Yes, I know!','2023-11-12 08:17:16',1,5,0),(19,'Sure?','2023-11-12 08:17:44',1,1,1),(20,'Hey, whatsapp?','2023-11-12 08:17:44',3,5,0),(21,'Good and u?','2023-11-12 08:22:50',3,5,0),(22,'holi','2023-11-15 16:13:15',1,1,1),(23,'yoo whats up?','2023-11-15 19:32:30',4,5,1),(24,'Yup','2023-11-15 19:33:29',1,1,1),(25,'w','2023-11-15 19:34:16',3,5,0),(26,'well done!','2023-11-15 19:55:26',1,1,1),(27,'Thank u, it is highly appreacciated!','2023-11-15 19:55:44',1,5,0),(28,'s','2023-11-15 20:06:19',1,1,1),(29,'Hey ,','2023-11-15 20:21:13',5,9,0),(30,'xxxxx','2023-11-15 20:22:11',5,1,0),(31,'z!','2023-11-15 20:22:20',5,9,0),(32,'w','2023-11-15 21:40:43',5,1,0),(33,'s','2023-11-15 22:03:22',5,9,0),(34,'x','2023-11-15 22:42:46',5,9,0),(35,'s','2023-11-16 22:45:08',2,1,1),(36,'s','2023-11-16 23:22:19',1,1,1),(37,'Hola!','2023-11-16 23:24:43',6,1,1),(38,'Hola!','2023-11-16 23:26:38',6,3,0),(39,'Todo bien?','2023-11-16 23:54:24',6,3,0),(40,'.','2023-11-17 00:13:33',6,3,0),(41,'yyyh','2023-11-17 00:14:39',6,1,1),(42,'x','2023-11-17 00:35:52',5,1,0),(43,'x','2023-11-17 00:36:06',2,1,1),(44,'x','2023-11-17 00:38:59',7,3,0),(45,'x','2023-11-17 00:39:16',1,1,1),(46,'xxx','2023-11-17 00:39:32',6,3,0),(47,'.','2023-11-18 13:04:49',5,1,0),(48,'Hello','2023-11-18 13:06:00',8,1,1),(49,'d','2023-11-18 13:18:31',8,1,1),(50,'d','2023-11-18 13:18:41',6,1,1),(51,'x','2023-11-18 13:19:15',9,1,1),(52,'x','2023-11-18 13:26:31',2,1,1),(53,'.','2023-11-18 19:23:14',1,1,1),(54,'ssssss','2023-11-18 20:06:35',10,1,1),(55,'.','2023-11-18 20:57:29',5,1,0),(56,'hello','2023-11-18 21:33:16',5,1,0),(57,'all good','2023-11-18 21:33:29',5,9,0),(58,'x','2023-11-18 21:35:21',5,1,0),(59,'xxxx','2023-11-18 21:36:34',5,1,0),(60,'xxxx','2023-11-18 21:36:42',5,1,0),(61,'xxxxx','2023-11-18 21:37:05',5,9,0),(62,'cccc','2023-11-18 22:39:27',5,9,0),(63,'Hello kevin','2023-11-18 22:42:27',11,10,0),(64,'Hello','2023-11-18 22:42:40',11,1,0),(65,'cccc','2023-11-18 22:47:34',11,1,0),(66,'ccc','2023-11-18 22:47:39',11,1,0),(67,'xxx','2023-11-19 00:29:58',11,1,0),(68,'x','2023-11-19 00:35:29',8,1,1),(69,'xxx','2023-11-19 00:36:23',8,1,1),(70,'x','2023-11-19 00:39:43',8,1,1),(71,'x','2023-11-19 00:39:59',11,10,0),(72,'ccc','2023-11-19 00:46:38',8,1,1),(73,'x','2023-11-19 01:47:59',9,1,1),(74,'xx','2023-11-19 01:50:16',11,10,0),(75,'xxx','2023-11-19 01:50:38',11,1,0),(76,'hello','2023-11-19 01:52:18',11,1,0),(77,'u','2023-11-19 01:52:21',11,1,0),(78,'please','2023-11-19 01:52:25',11,1,0),(79,'hello Sofi','2023-11-19 01:53:34',12,2,1),(80,'Are u there?','2023-11-19 01:54:42',12,2,1),(81,'Kevin are u there?','2023-11-19 01:55:20',13,2,0),(82,'hello','2023-11-19 02:03:11',13,2,0),(83,'please','2023-11-19 02:03:54',11,10,0),(84,'hello kev','2023-11-19 02:04:44',11,10,0),(85,'Are u there?','2023-11-19 02:04:49',11,10,0),(86,'Could u please update the dashboard?','2023-11-19 02:05:22',11,10,0),(87,'Please','2023-11-19 02:05:26',11,10,0),(88,'hello','2023-11-19 02:05:29',11,10,0),(89,'okie','2023-11-19 02:05:35',11,1,0),(90,'hello','2023-11-19 02:09:15',11,10,0),(91,'Helllo','2023-11-19 02:09:25',11,1,0),(92,'bye','2023-11-19 02:09:45',11,1,0),(93,'one more thin','2023-11-19 02:10:12',11,1,0),(94,'ssssssssss','2023-11-19 02:10:38',11,1,0),(95,'ssssss','2023-11-19 02:10:45',11,1,0),(96,'sssssssssss','2023-11-19 02:11:03',6,1,1),(97,'hello','2023-11-19 02:19:10',11,10,0),(98,'are u there','2023-11-19 02:19:17',11,10,0),(99,'ssss','2023-11-19 02:19:48',11,10,1);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reactions`
--

DROP TABLE IF EXISTS `reactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reactions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `reaction` int DEFAULT NULL,
  `message_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_reactions_messages1_idx` (`message_id`),
  CONSTRAINT `fk_reactions_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reactions`
--

LOCK TABLES `reactions` WRITE;
/*!40000 ALTER TABLE `reactions` DISABLE KEYS */;
INSERT INTO `reactions` VALUES (10,1,33),(11,0,34),(12,0,27),(13,0,37),(14,0,38),(15,0,39),(16,0,18),(17,1,46),(18,0,40),(19,0,41),(20,0,31),(21,2,58),(22,1,59),(23,0,60),(24,0,62),(25,1,63),(26,1,71),(27,1,25),(28,1,90),(29,2,98),(30,1,88);
/*!40000 ALTER TABLE `reactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fname` varchar(45) DEFAULT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `nick` varchar(45) DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `created_at` varchar(45) DEFAULT NULL,
  `picture` varchar(150) DEFAULT NULL,
  `dark_mode` varchar(5) DEFAULT 'NO',
  PRIMARY KEY (`id`,`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Kevinx','Duque','kduque','kevin.arturo.jacome.duque@gmail.com','2023-11-16 23:23:14','this_is_fine.gif','NO'),(2,'Arturo','Duque','aduque','Art@gmail.com','2023-11-18 13:21:02','cat.gif','YES'),(3,'Emir','Duque','eduque','eduque@gmail.com','2023-11-16 23:25:56','cuttie.png','NO'),(4,'tax','Duque','tduque','taque@gmail.com','2023-11-18 13:23:59','mew.gif','NO'),(5,'Moises','Michellow','mmichellow','mm@gmail.com','2023-11-18 13:26:15','mario.gif','NO'),(6,'kim','Michellow','kmichellow','mo@gmail.com','2023-11-18 13:20:02','niceee.gif','NO'),(7,'uuuuuuuuu','uuuuuu','uuuuss','ue@gmail.com','2023-11-18 13:24:47','Angry.gif','NO'),(8,'EMiliox','Duquex','EDuquex','emilox@gmail.com','2023-11-12 03:45:30','738a719f468f177e.gif','NO'),(9,'xamo','jacome','xjacome','xamote@gmail.com','2023-11-18 13:25:33','cheer.gif','YES'),(10,'Sofi','Solis','SSolis','sofi@gmail.com','2023-11-18 22:44:52','sonic.gif','YES');
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

-- Dump completed on 2023-11-19  2:27:15
