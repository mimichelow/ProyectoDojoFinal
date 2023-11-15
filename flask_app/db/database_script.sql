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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chats`
--

LOCK TABLES `chats` WRITE;
/*!40000 ALTER TABLE `chats` DISABLE KEYS */;
INSERT INTO `chats` VALUES (1,1,5,'2023-11-11 20:30:46','2023-11-11 20:30:46'),(2,1,6,'2023-11-11 20:30:46','2023-11-11 20:30:46'),(3,5,2,'2023-11-11 20:30:46','2023-11-11 20:30:46');
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logins`
--

LOCK TABLES `logins` WRITE;
/*!40000 ALTER TABLE `logins` DISABLE KEYS */;
INSERT INTO `logins` VALUES (1,'$2b$12$WI26NWW3tRyO40fOy0iCueDdkhCAZ8CSv3tTRZ7EXyZyKysumeYV.',1),(2,'$2b$12$aGJMNDj9eqHmKhWsKUEOLevy85kVOxt5tYciJOXcgpKVPrQbMMqlO',2),(3,'$2b$12$E7Yl03nXDw9muBuONXT4y.M1P.5/qlYOwoeTinlp4U0K7Bd4ZiDr2',3),(4,'$2b$12$Bp.YUp3WfuG3wkHueulK5OWxsDjqcwvge4JiTNOg.PxN6OH.xuTUK',4),(5,'$2b$12$JOYzbY9tEeaWYAK1UaoujO0hYDKM3hU1dxa5iJRqvzqIe/RIfU7dG',5),(6,'$2b$12$25RRZRJMietfuiPLnrm2YOw4FZDc6E.Yiv3rdSgGzUZfsreWZzKi.',6),(7,'$2b$12$0aoejbu.d3o4a1EPkuaCcOfNj5lJaWjJVc./KRE3efpwF0N2jqo2y',7),(8,'$2b$12$dPKhAiBEtcenBAkwolk4EetJHvi3VUzyj3AUYBygLe9VqmHMZqXZC',8);
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
  PRIMARY KEY (`id`),
  KEY `fk_messages_chats1_idx` (`chat_id`),
  KEY `fk_messages_users1_idx` (`user_id`),
  CONSTRAINT `fk_messages_chats1` FOREIGN KEY (`chat_id`) REFERENCES `chats` (`id`),
  CONSTRAINT `fk_messages_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'Hola, como va todo?','2023-11-11 20:32:29',1,1),(2,'Bien y tu?','2023-11-11 21:17:12',1,5),(3,'Vamos a estudiar?','2023-11-11 21:17:12',2,1),(4,'sdgadfgs','2023-11-12 06:04:25',1,1),(5,'GGFD','2023-11-12 06:10:33',1,1),(6,'xxxxxx','2023-11-12 06:23:51',1,1),(7,'ssss','2023-11-12 06:24:01',1,1),(14,'hey, I am talking','2023-11-12 07:35:53',1,1),(15,'oooooo','2023-11-12 08:00:05',1,1),(16,'Hey u, reply!','2023-11-12 08:13:35',2,1),(17,'hey, I am talking','2023-11-12 08:17:03',1,1),(18,'Yes, I know!','2023-11-12 08:17:16',1,5),(19,'Sure?','2023-11-12 08:17:44',1,1),(20,'Hey, whatsapp?','2023-11-12 08:17:44',3,5),(21,'Good and u?','2023-11-12 08:22:50',3,5),(22,'holi','2023-11-15 16:13:15',1,1);
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
  `character` int DEFAULT NULL,
  `messages_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_reactions_messages1_idx` (`messages_id`),
  CONSTRAINT `fk_reactions_messages1` FOREIGN KEY (`messages_id`) REFERENCES `messages` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reactions`
--

LOCK TABLES `reactions` WRITE;
/*!40000 ALTER TABLE `reactions` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Kevinx','Duque','kduque','kevin.arturo.jacome.duque@gmail.com','2023-11-12 08:15:22','738a719f468f177e.gif','YES'),(2,'Arturo','Duque','aduque','Art@gmail.com','2023-11-11 21:05:46','user.webp','NO'),(3,'Emir','Duque','eduque','eduque@gmail.com','2023-11-11 21:05:46','user.webp','YES'),(4,'tax','Duque','tduque','taque@gmail.com','2023-11-11 21:05:46','user.webp','NO'),(5,'Moises','Michellow','mmichellow','mm@gmail.com','2023-11-11 21:05:46','738a719f468f177e.gif','NO'),(6,'kim','Michellow','kmichellow','mo@gmail.com','2023-11-11 21:05:46','user.webp','NO'),(7,'uuuuuuuuu','uuuuuu','uuuu','ue@gmail.com','2023-11-11 21:05:46','user.webp','NO'),(8,'EMiliox','Duquex','EDuquex','emilox@gmail.com','2023-11-12 03:45:30','738a719f468f177e.gif','NO');
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

-- Dump completed on 2023-11-15 16:56:31
