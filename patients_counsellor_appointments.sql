-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: patients_counsellor_appointments
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_analytics`
--

DROP TABLE IF EXISTS `app_analytics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_analytics` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_active` tinyint(1) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  `action` varchar(50) DEFAULT NULL,
  `search_params` longtext,
  `app_version` varchar(50) DEFAULT NULL,
  `platform` varchar(50) DEFAULT NULL,
  `brand` varchar(50) DEFAULT NULL,
  `device` varchar(250) DEFAULT NULL,
  `device_model` varchar(50) DEFAULT NULL,
  `device_ip` varchar(50) DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_analytics_user_id_ea94e4d1_fk_app_user_mst_id` (`user_id`),
  CONSTRAINT `app_analytics_user_id_ea94e4d1_fk_app_user_mst_id` FOREIGN KEY (`user_id`) REFERENCES `app_user_mst` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_analytics`
--

LOCK TABLES `app_analytics` WRITE;
/*!40000 ALTER TABLE `app_analytics` DISABLE KEYS */;
INSERT INTO `app_analytics` VALUES (1,1,'2023-10-25 07:12:20.012646','2023-10-25 07:12:20.012657','Create Patient','{}',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(2,1,'2023-10-25 07:32:50.638271','2023-10-25 07:32:50.638288','Create Patient','{}',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(3,1,'2023-10-25 07:33:49.431839','2023-10-25 07:33:49.431848','Create Patient','{}',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(4,1,'2023-10-25 07:34:53.441696','2023-10-25 07:34:53.441706','Create Patient','{}',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(5,1,'2023-10-25 07:35:54.815427','2023-10-25 07:35:54.815443','Create Patient','<QueryDict: {\'patient_name\': [\'Atif fUsman\'], \'patient_email\': [\'atifusman@test.com\'], \'patient_password\': [\'test@123\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(6,1,'2023-10-25 07:37:21.182157','2023-10-25 07:37:21.182169','Create Patient','<QueryDict: {\'patient_name\': [\'Atif fUsman\'], \'patient_email\': [\'atifusman@test.com\'], \'patient_password\': [\'test@123\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(7,1,'2023-10-25 07:43:43.852906','2023-10-25 07:43:43.852917','Create Patient','<QueryDict: {\'patient_name\': [\'Atif fUsman\'], \'patient_email\': [\'atifusman1@test.com\'], \'patient_password\': [\'test@123\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(8,1,'2023-10-25 07:54:38.429830','2023-10-25 07:54:38.429838','Create Patient','<QueryDict: {\'patient_name\': [\'Atif fUsman\'], \'patient_email\': [\'atifusman4@test.com\'], \'patient_password\': [\'test@123\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(9,1,'2023-10-25 08:11:41.480510','2023-10-25 08:11:41.480520','Create Counsellor','<QueryDict: {\'counsellor_name\': [\'Atif fUsman\'], \'counsellor_email\': [\'atifusman4@test.com\'], \'counsellor_password\': [\'test@123\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(10,1,'2023-10-25 08:11:51.184785','2023-10-25 08:11:51.184800','Create Counsellor','<QueryDict: {\'counsellor_name\': [\'Atif fUsman\'], \'counsellor_email\': [\'atifusman4@test.com\'], \'counsellor_password\': [\'test@123\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(11,1,'2023-10-25 08:14:25.021596','2023-10-25 08:14:25.021607','Create Counsellor','<QueryDict: {\'counsellor_name\': [\'Atif fUsman\'], \'counsellor_email\': [\'atifusman4@testq.com\'], \'counsellor_password\': [\'test@123\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(12,1,'2023-10-25 09:06:28.766444','2023-10-25 09:06:28.766456','Patient List','{}',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(13,1,'2023-10-25 09:07:31.616036','2023-10-25 09:07:31.616049','Patient List','{}',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(14,1,'2023-10-25 09:08:43.228791','2023-10-25 09:08:43.228800','Patient List','{}',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(15,1,'2023-10-25 09:11:18.236762','2023-10-25 09:11:18.236771','Patient List','<QueryDict: {\'page\': [\'1\'], \'reqRecs\': [\'10\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(16,1,'2023-10-25 09:12:01.115285','2023-10-25 09:12:01.115293','Patient List','<QueryDict: {\'page\': [\'1\'], \'reqRecs\': [\'10\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(17,1,'2023-10-25 09:15:36.375129','2023-10-25 09:15:36.375142','Patient List','<QueryDict: {\'page\': [\'1\'], \'reqRecs\': [\'10\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(18,1,'2023-10-25 09:15:45.022923','2023-10-25 09:15:45.022934','Patient List','<QueryDict: {\'page\': [\'1\'], \'reqRecs\': [\'10\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(19,1,'2023-10-25 09:17:23.797245','2023-10-25 09:17:23.797256','Counsellors List','<QueryDict: {\'page\': [\'1\'], \'reqRecs\': [\'10\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(20,1,'2023-10-25 09:18:38.458112','2023-10-25 09:18:38.458121','Counsellors List','<QueryDict: {\'page\': [\'1\'], \'reqRecs\': [\'10\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(21,1,'2023-10-25 09:19:01.797065','2023-10-25 09:19:01.797074','Counsellors List','<QueryDict: {\'page\': [\'1\'], \'reqRecs\': [\'10\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(22,1,'2023-10-25 09:40:23.023793','2023-10-25 09:40:23.023802','Counsellor Details','<QueryDict: {\'counsellor_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(23,1,'2023-10-25 09:40:33.480194','2023-10-25 09:40:33.480202','Counsellor Details','<QueryDict: {\'counsellor_id\': [\'5\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(24,1,'2023-10-25 09:46:35.476268','2023-10-25 09:46:35.476277','Patient Details','<QueryDict: {\'patient_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(25,1,'2023-10-25 10:03:00.752132','2023-10-25 10:03:00.752141','Counsellor Delete','<QueryDict: {\'counsellor_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(26,1,'2023-10-25 10:05:36.546903','2023-10-25 10:05:36.546913','Patient Delete','<QueryDict: {\'patient_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(27,1,'2023-10-25 10:06:20.609961','2023-10-25 10:06:20.609971','Patient Delete','<QueryDict: {\'patient_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(28,1,'2023-10-25 10:06:46.879052','2023-10-25 10:06:46.879063','Patient Delete','<QueryDict: {\'patient_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(29,1,'2023-10-25 10:07:11.549213','2023-10-25 10:07:11.549222','Patient Delete','<QueryDict: {\'patient_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(30,1,'2023-10-25 10:08:04.392114','2023-10-25 10:08:04.392122','Patient Delete','<QueryDict: {\'patient_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(31,1,'2023-10-25 10:21:50.986383','2023-10-25 10:21:50.986395','Counsellor Delete','<QueryDict: {\'counsellor_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(32,1,'2023-10-25 10:21:57.545630','2023-10-25 10:21:57.545639','Counsellor Delete','<QueryDict: {\'counsellor_id\': [\'2\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(33,1,'2023-10-25 10:45:54.478575','2023-10-25 10:45:54.478587','Patient Update','<QueryDict: {\'patient_id\': [\'1\'], \'patient_name\': [\'Atif Usman Hashim Hajo Ahmed\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(34,1,'2023-10-25 10:48:18.137892','2023-10-25 10:48:18.137900','Patient Update','<QueryDict: {\'patient_id\': [\'1\'], \'patient_name\': [\'Atif Usman Hashim Hajo Ahmed\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(35,1,'2023-10-25 10:56:27.266872','2023-10-25 10:56:27.266882','Counsellor Update','<QueryDict: {\'counsellor_id\': [\'1\'], \'counsellor_name\': [\'Atif Memon\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(36,1,'2023-10-25 10:56:52.664854','2023-10-25 10:56:52.664868','Counsellor Update','<QueryDict: {\'counsellor_id\': [\'1\'], \'counsellor_name\': [\'Atif Memon\'], \'counsellor_email\': [\'atifusman@test.cocm\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(37,1,'2023-10-25 10:57:00.444011','2023-10-25 10:57:00.444019','Counsellor Update','<QueryDict: {\'counsellor_id\': [\'1\'], \'counsellor_name\': [\'Atif Memon\'], \'counsellor_email\': [\'atifusman1@test.cocm\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(38,1,'2023-10-25 12:37:53.909404','2023-10-25 12:37:53.909414','Active Appointments List','<QueryDict: {\'patient_id\': [\'1\'], \'appointment_date\': [\'2023-11-29\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(39,1,'2023-10-25 12:42:24.815294','2023-10-25 12:42:24.815303','Active Appointments List','<QueryDict: {\'patient_id\': [\'1\'], \'appointment_date\': [\'2023-11-29\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(40,1,'2023-10-25 12:42:57.305295','2023-10-25 12:42:57.305306','Active Appointments List','<QueryDict: {\'patient_id\': [\'1\'], \'appointment_date\': [\'2023-11-29\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(41,1,'2023-10-25 12:43:25.523408','2023-10-25 12:43:25.523417','Active Appointments List','<QueryDict: {\'patient_id\': [\'1\'], \'appointment_date\': [\'2023-11-29\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(42,1,'2023-10-25 12:55:17.085239','2023-10-25 12:55:17.085249','Active Appointments List','<QueryDict: {\'start_date\': [\'2023-10-01\'], \'end_date\': [\'2023-10-31\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(43,1,'2023-10-25 12:55:51.110799','2023-10-25 12:55:51.110810','Active Appointments List','<QueryDict: {\'start_date\': [\'2023-10-01\'], \'end_date\': [\'2023-10-31\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(44,1,'2023-10-25 12:56:05.794937','2023-10-25 12:56:05.794945','Active Appointments List','<QueryDict: {\'start_date\': [\'2023-10-01\'], \'end_date\': [\'2023-12-31\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(45,1,'2023-10-25 13:39:00.385519','2023-10-25 13:39:00.385530','Appointment Details','<QueryDict: {\'appointment_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(46,1,'2023-10-25 13:44:31.890192','2023-10-25 13:44:31.890201','Appointment Details','<QueryDict: {\'appointment_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(47,1,'2023-10-25 13:44:49.997636','2023-10-25 13:44:49.997645','Appointment Details','<QueryDict: {\'start_date\': [\'2023-10-01\'], \'end_date\': [\'2023-11-30\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(48,1,'2023-10-25 13:45:48.253425','2023-10-25 13:45:48.253436','Appointment Details','<QueryDict: {\'start_date\': [\'2023-10-01\'], \'end_date\': [\'2023-11-30\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(49,1,'2023-10-25 13:46:12.011731','2023-10-25 13:46:12.011741','Appointment Details','<QueryDict: {\'start_date\': [\'2023-10-01\'], \'end_date\': [\'2023-11-30\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(50,1,'2023-10-25 13:47:13.212881','2023-10-25 13:47:13.212890','Appointment Details','<QueryDict: {\'start_date\': [\'2023-10-01\'], \'end_date\': [\'2023-11-30\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(51,1,'2023-10-25 13:47:26.064071','2023-10-25 13:47:26.064079','Appointment Details','<QueryDict: {\'appointment_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(52,1,'2023-10-25 13:49:49.055427','2023-10-25 13:49:49.055445','Appointment Delete','<QueryDict: {\'start_date\': [\'2023-10-01\'], \'end_date\': [\'2023-11-30\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(53,1,'2023-10-25 13:50:45.138943','2023-10-25 13:50:45.138951','Appointment Delete','<QueryDict: {\'start_date\': [\'2023-10-01\'], \'end_date\': [\'2023-11-30\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(54,1,'2023-10-25 13:51:10.807480','2023-10-25 13:51:10.807489','Appointment Details','<QueryDict: {\'appointment_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(55,1,'2023-10-25 13:51:12.577234','2023-10-25 13:51:12.577243','Appointment Details','<QueryDict: {\'appointment_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(56,1,'2023-10-25 13:53:24.031253','2023-10-25 13:53:24.031263','Appointment Details','<QueryDict: {\'start_date\': [\'2023-10-01\'], \'end_date\': [\'2023-11-30\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(57,1,'2023-10-25 13:55:43.542013','2023-10-25 13:55:43.542030','Appointment Details','<QueryDict: {\'start_date\': [\'2023-10-01\'], \'end_date\': [\'2023-11-30\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(58,1,'2023-10-25 13:57:45.795108','2023-10-25 13:57:45.795117','Appointment Delete','<QueryDict: {\'appointment_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(59,1,'2023-10-25 13:59:08.857613','2023-10-25 13:59:08.857622','Appointment Delete','<QueryDict: {\'appointment_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL),(60,1,'2023-10-25 14:00:11.435135','2023-10-25 14:00:11.435148','Appointment Delete','<QueryDict: {\'appointment_id\': [\'1\']}>',NULL,NULL,NULL,NULL,NULL,'127.0.0.1',NULL);
/*!40000 ALTER TABLE `app_analytics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_appointments`
--

DROP TABLE IF EXISTS `app_appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_appointments` (
  `is_active` tinyint(1) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  `appointment_id` int NOT NULL AUTO_INCREMENT,
  `appointment_code` varchar(50) DEFAULT NULL,
  `appointment_date` datetime(6) DEFAULT NULL,
  `appointment_counsellor_id` int DEFAULT NULL,
  `appointment_patient_id` int DEFAULT NULL,
  `deleted_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`appointment_id`),
  UNIQUE KEY `appointment_code` (`appointment_code`),
  KEY `app_appointments_appointment_counsell_5ac93e57_fk_app_couns` (`appointment_counsellor_id`),
  KEY `app_appointments_appointment_patient__4a907c2c_fk_app_patie` (`appointment_patient_id`),
  CONSTRAINT `app_appointments_appointment_counsell_5ac93e57_fk_app_couns` FOREIGN KEY (`appointment_counsellor_id`) REFERENCES `app_counsellor` (`counsellor_id`),
  CONSTRAINT `app_appointments_appointment_patient__4a907c2c_fk_app_patie` FOREIGN KEY (`appointment_patient_id`) REFERENCES `app_patient` (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_appointments`
--

LOCK TABLES `app_appointments` WRITE;
/*!40000 ALTER TABLE `app_appointments` DISABLE KEYS */;
INSERT INTO `app_appointments` VALUES (0,'2023-10-25 11:43:17.000000','2023-10-25 11:43:17.000000',1,'A-Uu4tK914KWc4','2023-11-28 19:00:00.000000',1,1,'2023-10-25 14:00:11.000000'),(1,'2023-10-25 12:20:36.000000','2023-10-25 12:20:36.000000',2,'A-3FTpFGaiPqbm','2023-11-28 19:00:00.000000',1,1,NULL),(1,'2023-10-25 12:21:42.000000','2023-10-25 12:21:42.000000',3,'A-WBW3NEuE6Y7R','2023-11-28 19:00:00.000000',2,1,NULL),(1,'2023-10-25 12:23:16.174621','2023-10-25 12:23:16.174629',4,'A-zFmD8yAUPBYv','2023-11-28 19:00:00.000000',2,1,NULL),(1,'2023-10-25 12:26:19.472837','2023-10-25 12:26:19.472853',5,'A-dX2vSowDTCyJ','2023-11-20 19:00:00.000000',2,1,NULL);
/*!40000 ALTER TABLE `app_appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_counsellor`
--

DROP TABLE IF EXISTS `app_counsellor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_counsellor` (
  `is_active` tinyint(1) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  `counsellor_id` int NOT NULL AUTO_INCREMENT,
  `counsellor_code` varchar(50) DEFAULT NULL,
  `counsellor_name` varchar(250) DEFAULT NULL,
  `counsellor_email` varchar(250) NOT NULL,
  `counsellor_password` varchar(15) NOT NULL,
  `deleted_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`counsellor_id`),
  UNIQUE KEY `counsellor_email` (`counsellor_email`),
  UNIQUE KEY `counsellor_code` (`counsellor_code`),
  KEY `app_counsellor_counsellor_name_d037cfec` (`counsellor_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_counsellor`
--

LOCK TABLES `app_counsellor` WRITE;
/*!40000 ALTER TABLE `app_counsellor` DISABLE KEYS */;
INSERT INTO `app_counsellor` VALUES (1,'2023-10-25 08:11:41.000000','2023-10-25 08:11:41.000000',1,'C-WdCGi9C8ZGez','Atif Memon','atifusman1@test.cocm','test@123',NULL),(1,'2023-10-25 08:14:25.000000','2023-10-25 08:14:25.000000',2,'C-G9rETcTMwVrz','Atif fUsman','atifusman4@testq.com','test@123',NULL);
/*!40000 ALTER TABLE `app_counsellor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_login_analytics`
--

DROP TABLE IF EXISTS `app_login_analytics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_login_analytics` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `action` varchar(50) DEFAULT NULL,
  `source` varchar(300) DEFAULT NULL,
  `device_ip` varchar(50) DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `modified_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_login_analytics_user_id_fe82a194_fk_app_user_mst_id` (`user_id`),
  CONSTRAINT `app_login_analytics_user_id_fe82a194_fk_app_user_mst_id` FOREIGN KEY (`user_id`) REFERENCES `app_user_mst` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_login_analytics`
--

LOCK TABLES `app_login_analytics` WRITE;
/*!40000 ALTER TABLE `app_login_analytics` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_login_analytics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_patient`
--

DROP TABLE IF EXISTS `app_patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_patient` (
  `is_active` tinyint(1) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `patient_code` varchar(50) DEFAULT NULL,
  `patient_name` varchar(250) DEFAULT NULL,
  `patient_email` varchar(250) NOT NULL,
  `patient_password` varchar(15) NOT NULL,
  `deleted_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`patient_id`),
  UNIQUE KEY `patient_email` (`patient_email`),
  UNIQUE KEY `patient_code` (`patient_code`),
  KEY `app_patient_patient_name_61bd14d4` (`patient_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_patient`
--

LOCK TABLES `app_patient` WRITE;
/*!40000 ALTER TABLE `app_patient` DISABLE KEYS */;
INSERT INTO `app_patient` VALUES (1,'2023-10-25 07:37:21.000000','2023-10-25 07:37:21.000000',1,'P-v63afYXBJEi2','Atif Usman Hashim Hajo Ahmed','atifusman@test.com','test@123',NULL),(1,'2023-10-25 07:43:43.913427','2023-10-25 07:43:43.913451',2,'P-IJWIOyCiCJtw','Atif fUsman','atifusman1@test.com','test@123',NULL),(1,'2023-10-25 07:54:38.496140','2023-10-25 07:54:38.496156',3,'P-EW3JrP8Hydn0','Atif fUsman','atifusman4@test.com','test@123',NULL);
/*!40000 ALTER TABLE `app_patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_user_mst`
--

DROP TABLE IF EXISTS `app_user_mst`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_user_mst` (
  `id` bigint NOT NULL AUTO_INCREMENT,
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
  `user_no` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `user_role_id` int DEFAULT NULL,
  `contact_no` varchar(50) DEFAULT NULL,
  `contact_no_flag` tinyint(1) NOT NULL,
  `is_auth` tinyint(1) NOT NULL,
  `is_counseller` tinyint(1) NOT NULL,
  `is_patient` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `unique_user_no` (`user_no`),
  KEY `app_user_mst_user_role_id_11aa3454_fk_app_user_role_role_id` (`user_role_id`),
  KEY `app_user_mst_user_no_bfcfb793` (`user_no`),
  CONSTRAINT `app_user_mst_user_role_id_11aa3454_fk_app_user_role_role_id` FOREIGN KEY (`user_role_id`) REFERENCES `app_user_role` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_user_mst`
--

LOCK TABLES `app_user_mst` WRITE;
/*!40000 ALTER TABLE `app_user_mst` DISABLE KEYS */;
INSERT INTO `app_user_mst` VALUES (1,'pbkdf2_sha256$260000$XXo3EsQ6ALlC1RlG5r8xgc$88AcJa/6A6jnEBJXpS7BPSckejFHf46EoAQ2qH6yNXI=','2023-10-24 22:13:05.290222',1,'admin','','','admin@test.com',1,1,'2023-10-24 18:53:12.058806','U-RCjUWljXhB7c',NULL,NULL,NULL,0,1,0,0);
/*!40000 ALTER TABLE `app_user_mst` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_user_mst_groups`
--

DROP TABLE IF EXISTS `app_user_mst_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_user_mst_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `appuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_user_mst_groups_appuser_id_group_id_7b1c2cf9_uniq` (`appuser_id`,`group_id`),
  KEY `app_user_mst_groups_group_id_81a008dd_fk_auth_group_id` (`group_id`),
  CONSTRAINT `app_user_mst_groups_appuser_id_7ef215df_fk_app_user_mst_id` FOREIGN KEY (`appuser_id`) REFERENCES `app_user_mst` (`id`),
  CONSTRAINT `app_user_mst_groups_group_id_81a008dd_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_user_mst_groups`
--

LOCK TABLES `app_user_mst_groups` WRITE;
/*!40000 ALTER TABLE `app_user_mst_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_user_mst_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_user_mst_user_permissions`
--

DROP TABLE IF EXISTS `app_user_mst_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_user_mst_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `appuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_user_mst_user_permis_appuser_id_permission_id_813c5946_uniq` (`appuser_id`,`permission_id`),
  KEY `app_user_mst_user_pe_permission_id_765efb94_fk_auth_perm` (`permission_id`),
  CONSTRAINT `app_user_mst_user_pe_appuser_id_a1989cf0_fk_app_user_` FOREIGN KEY (`appuser_id`) REFERENCES `app_user_mst` (`id`),
  CONSTRAINT `app_user_mst_user_pe_permission_id_765efb94_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_user_mst_user_permissions`
--

LOCK TABLES `app_user_mst_user_permissions` WRITE;
/*!40000 ALTER TABLE `app_user_mst_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_user_mst_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_user_role`
--

DROP TABLE IF EXISTS `app_user_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_user_role` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `role_code` varchar(50) DEFAULT NULL,
  `role_name` varchar(50) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `modified_date` datetime(6) NOT NULL,
  PRIMARY KEY (`role_id`),
  UNIQUE KEY `unique_role_code` (`role_code`),
  KEY `app_user_role_role_code_e7595653` (`role_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_user_role`
--

LOCK TABLES `app_user_role` WRITE;
/*!40000 ALTER TABLE `app_user_role` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_user_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add app user',1,'add_appuser'),(2,'Can change app user',1,'change_appuser'),(3,'Can delete app user',1,'delete_appuser'),(4,'Can view app user',1,'view_appuser'),(5,'Can add login analytics',2,'add_loginanalytics'),(6,'Can change login analytics',2,'change_loginanalytics'),(7,'Can delete login analytics',2,'delete_loginanalytics'),(8,'Can view login analytics',2,'view_loginanalytics'),(9,'Can add user role',3,'add_userrole'),(10,'Can change user role',3,'change_userrole'),(11,'Can delete user role',3,'delete_userrole'),(12,'Can view user role',3,'view_userrole'),(13,'Can add log entry',4,'add_logentry'),(14,'Can change log entry',4,'change_logentry'),(15,'Can delete log entry',4,'delete_logentry'),(16,'Can view log entry',4,'view_logentry'),(17,'Can add permission',5,'add_permission'),(18,'Can change permission',5,'change_permission'),(19,'Can delete permission',5,'delete_permission'),(20,'Can view permission',5,'view_permission'),(21,'Can add group',6,'add_group'),(22,'Can change group',6,'change_group'),(23,'Can delete group',6,'delete_group'),(24,'Can view group',6,'view_group'),(25,'Can add content type',7,'add_contenttype'),(26,'Can change content type',7,'change_contenttype'),(27,'Can delete content type',7,'delete_contenttype'),(28,'Can view content type',7,'view_contenttype'),(29,'Can add session',8,'add_session'),(30,'Can change session',8,'change_session'),(31,'Can delete session',8,'delete_session'),(32,'Can view session',8,'view_session'),(33,'Can add Token',9,'add_token'),(34,'Can change Token',9,'change_token'),(35,'Can delete Token',9,'delete_token'),(36,'Can view Token',9,'view_token'),(37,'Can add token',10,'add_tokenproxy'),(38,'Can change token',10,'change_tokenproxy'),(39,'Can delete token',10,'delete_tokenproxy'),(40,'Can view token',10,'view_tokenproxy'),(41,'Can add site',11,'add_site'),(42,'Can change site',11,'change_site'),(43,'Can delete site',11,'delete_site'),(44,'Can view site',11,'view_site'),(45,'Can add application',12,'add_application'),(46,'Can change application',12,'change_application'),(47,'Can delete application',12,'delete_application'),(48,'Can view application',12,'view_application'),(49,'Can add access token',13,'add_accesstoken'),(50,'Can change access token',13,'change_accesstoken'),(51,'Can delete access token',13,'delete_accesstoken'),(52,'Can view access token',13,'view_accesstoken'),(53,'Can add grant',14,'add_grant'),(54,'Can change grant',14,'change_grant'),(55,'Can delete grant',14,'delete_grant'),(56,'Can view grant',14,'view_grant'),(57,'Can add refresh token',15,'add_refreshtoken'),(58,'Can change refresh token',15,'change_refreshtoken'),(59,'Can delete refresh token',15,'delete_refreshtoken'),(60,'Can view refresh token',15,'view_refreshtoken'),(61,'Can add id token',16,'add_idtoken'),(62,'Can change id token',16,'change_idtoken'),(63,'Can delete id token',16,'delete_idtoken'),(64,'Can view id token',16,'view_idtoken'),(65,'Can add app analytics',17,'add_appanalytics'),(66,'Can change app analytics',17,'change_appanalytics'),(67,'Can delete app analytics',17,'delete_appanalytics'),(68,'Can view app analytics',17,'view_appanalytics'),(69,'Can add patient',18,'add_patient'),(70,'Can change patient',18,'change_patient'),(71,'Can delete patient',18,'delete_patient'),(72,'Can view patient',18,'view_patient'),(73,'Can add counsellor',19,'add_counsellor'),(74,'Can change counsellor',19,'change_counsellor'),(75,'Can delete counsellor',19,'delete_counsellor'),(76,'Can view counsellor',19,'view_counsellor'),(77,'Can add appointment',20,'add_appointment'),(78,'Can change appointment',20,'change_appointment'),(79,'Can delete appointment',20,'delete_appointment'),(80,'Can view appointment',20,'view_appointment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_app_user_mst_id` FOREIGN KEY (`user_id`) REFERENCES `app_user_mst` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_app_user_mst_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_app_user_mst_id` FOREIGN KEY (`user_id`) REFERENCES `app_user_mst` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-10-24 22:14:14.943040','1','couseling-appointments.com',2,'[{\"changed\": {\"fields\": [\"Domain name\", \"Display name\"]}}]',11,1),(2,'2023-10-25 09:17:04.787142','2','Atif fUsman (atifusman4@testq.com)',2,'[{\"changed\": {\"fields\": [\"Counsellor code\"]}}]',19,1),(3,'2023-10-25 09:17:14.642502','1','Atif fUsman (atifusman4@test.com)',2,'[{\"changed\": {\"fields\": [\"Counsellor code\"]}}]',19,1),(4,'2023-10-25 10:07:31.820622','1','Atif fUsman (atifusman@test.com)',2,'[{\"changed\": {\"fields\": [\"Is active\"]}}]',18,1),(5,'2023-10-25 10:23:23.945783','1','Atif fUsman (atifusman@test.com)',2,'[{\"changed\": {\"fields\": [\"Is active\", \"Deleted date\"]}}]',18,1),(6,'2023-10-25 10:23:49.048720','2','Atif fUsman (atifusman4@testq.com)',2,'[{\"changed\": {\"fields\": [\"Is active\", \"Deleted date\"]}}]',19,1),(7,'2023-10-25 10:24:03.370274','1','Atif fUsman (atifusman4@test.com)',2,'[{\"changed\": {\"fields\": [\"Is active\"]}}]',19,1),(8,'2023-10-25 12:23:49.524567','1','A-Uu4tK914KWc4',2,'[{\"changed\": {\"fields\": [\"Appointment counsellor\"]}}]',20,1),(9,'2023-10-25 12:23:58.062611','2','A-3FTpFGaiPqbm',2,'[{\"changed\": {\"fields\": [\"Appointment counsellor\"]}}]',20,1),(10,'2023-10-25 12:24:06.933818','3','A-WBW3NEuE6Y7R',2,'[{\"changed\": {\"fields\": [\"Appointment counsellor\"]}}]',20,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (4,'admin','logentry'),(17,'appapi','appanalytics'),(20,'appointmentsapp','appointment'),(19,'appointmentsapp','counsellor'),(18,'appointmentsapp','patient'),(6,'auth','group'),(5,'auth','permission'),(1,'authapp','appuser'),(2,'authapp','loginanalytics'),(3,'authapp','userrole'),(9,'authtoken','token'),(10,'authtoken','tokenproxy'),(7,'contenttypes','contenttype'),(13,'oauth2_provider','accesstoken'),(12,'oauth2_provider','application'),(14,'oauth2_provider','grant'),(16,'oauth2_provider','idtoken'),(15,'oauth2_provider','refreshtoken'),(8,'sessions','session'),(11,'sites','site');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-10-24 14:05:21.070424'),(2,'contenttypes','0002_remove_content_type_name','2023-10-24 14:05:21.217967'),(3,'auth','0001_initial','2023-10-24 14:05:22.109700'),(4,'auth','0002_alter_permission_name_max_length','2023-10-24 14:05:22.225581'),(5,'auth','0003_alter_user_email_max_length','2023-10-24 14:05:22.258924'),(6,'auth','0004_alter_user_username_opts','2023-10-24 14:05:22.286961'),(7,'auth','0005_alter_user_last_login_null','2023-10-24 14:05:22.312080'),(8,'auth','0006_require_contenttypes_0002','2023-10-24 14:05:22.326700'),(9,'auth','0007_alter_validators_add_error_messages','2023-10-24 14:05:22.361861'),(10,'auth','0008_alter_user_username_max_length','2023-10-24 14:05:22.387859'),(11,'auth','0009_alter_user_last_name_max_length','2023-10-24 14:05:22.443168'),(12,'auth','0010_alter_group_name_max_length','2023-10-24 14:05:22.483054'),(13,'auth','0011_update_proxy_permissions','2023-10-24 14:05:22.511334'),(14,'auth','0012_alter_user_first_name_max_length','2023-10-24 14:05:22.542274'),(15,'authapp','0001_initial','2023-10-24 14:05:23.727461'),(16,'admin','0001_initial','2023-10-24 14:05:24.024505'),(17,'admin','0002_logentry_remove_auto_add','2023-10-24 14:05:24.045530'),(18,'admin','0003_logentry_add_action_flag_choices','2023-10-24 14:05:24.079110'),(19,'authtoken','0001_initial','2023-10-24 14:05:24.296952'),(20,'authtoken','0002_auto_20160226_1747','2023-10-24 14:05:24.416370'),(21,'authtoken','0003_tokenproxy','2023-10-24 14:05:24.438331'),(22,'oauth2_provider','0001_initial','2023-10-24 14:05:26.029370'),(23,'oauth2_provider','0002_auto_20190406_1805','2023-10-24 14:05:26.174986'),(24,'oauth2_provider','0003_auto_20201211_1314','2023-10-24 14:05:26.360621'),(25,'oauth2_provider','0004_auto_20200902_2022','2023-10-24 14:05:27.295543'),(26,'sessions','0001_initial','2023-10-24 14:05:27.387641'),(27,'sites','0001_initial','2023-10-24 14:05:27.465538'),(28,'sites','0002_alter_domain_unique','2023-10-24 14:05:27.580234'),(29,'authapp','0002_auto_20231024_1909','2023-10-24 14:09:21.975207'),(30,'authapp','0003_auto_20231024_1909','2023-10-24 14:09:44.421330'),(31,'appapi','0001_initial','2023-10-24 14:46:51.748090'),(32,'authapp','0004_auto_20231024_2355','2023-10-24 18:55:31.170815'),(33,'appointmentsapp','0001_initial','2023-10-25 05:16:38.788999'),(34,'appointmentsapp','0002_auto_20231025_1120','2023-10-25 06:21:04.205957'),(35,'appointmentsapp','0003_auto_20231025_1237','2023-10-25 07:37:07.052667'),(36,'appointmentsapp','0004_auto_20231025_1253','2023-10-25 07:53:52.291548');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('a9226brskbzt9uuwrpc9o6hri8cpidi0','.eJxVjMsOwiAQRf-FtSE8BVy67zeQGZhK1UBS2pXx35WkC13ee07Oi0XYtxL3TmtcMrswyU6_H0J6UB0g36HeGk-tbuuCfCj8oJ1PLdPzerh_gQK9jKzNoCyRys7ppP2sKKBWMhknRLLCWUkuWE9o9Nmi9y5oBBlMmP13avb-AM3HNvk:1qvPe5:7o4FZvQd6rN60XMmklbUPu7HMgp2PsdBawlgemK7-JQ','2023-11-07 22:13:05.301549');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_site` (
  `id` int NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'couseling-appointments.com','couseling-appointments.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_accesstoken`
--

DROP TABLE IF EXISTS `oauth2_provider_accesstoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_accesstoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` varchar(255) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `scope` longtext NOT NULL,
  `application_id` bigint DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `source_refresh_token_id` bigint DEFAULT NULL,
  `id_token_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token` (`token`),
  UNIQUE KEY `source_refresh_token_id` (`source_refresh_token_id`),
  UNIQUE KEY `id_token_id` (`id_token_id`),
  KEY `oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_app_user_mst_id` (`user_id`),
  CONSTRAINT `oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_acce_id_token_id_85db651b_fk_oauth2_pr` FOREIGN KEY (`id_token_id`) REFERENCES `oauth2_provider_idtoken` (`id`),
  CONSTRAINT `oauth2_provider_acce_source_refresh_token_e66fbc72_fk_oauth2_pr` FOREIGN KEY (`source_refresh_token_id`) REFERENCES `oauth2_provider_refreshtoken` (`id`),
  CONSTRAINT `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_app_user_mst_id` FOREIGN KEY (`user_id`) REFERENCES `app_user_mst` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_accesstoken`
--

LOCK TABLES `oauth2_provider_accesstoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_application`
--

DROP TABLE IF EXISTS `oauth2_provider_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_application` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `client_id` varchar(100) NOT NULL,
  `redirect_uris` longtext NOT NULL,
  `client_type` varchar(32) NOT NULL,
  `authorization_grant_type` varchar(32) NOT NULL,
  `client_secret` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `skip_authorization` tinyint(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `algorithm` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_id` (`client_id`),
  KEY `oauth2_provider_application_user_id_79829054_fk_app_user_mst_id` (`user_id`),
  KEY `oauth2_provider_application_client_secret_53133678` (`client_secret`),
  CONSTRAINT `oauth2_provider_application_user_id_79829054_fk_app_user_mst_id` FOREIGN KEY (`user_id`) REFERENCES `app_user_mst` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_application`
--

LOCK TABLES `oauth2_provider_application` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_application` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_grant`
--

DROP TABLE IF EXISTS `oauth2_provider_grant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_grant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `redirect_uri` longtext NOT NULL,
  `scope` longtext NOT NULL,
  `application_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `code_challenge` varchar(128) NOT NULL,
  `code_challenge_method` varchar(10) NOT NULL,
  `nonce` varchar(255) NOT NULL,
  `claims` longtext NOT NULL DEFAULT (_utf8mb4''),
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `oauth2_provider_gran_application_id_81923564_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_grant_user_id_e8f62af8_fk_app_user_mst_id` (`user_id`),
  CONSTRAINT `oauth2_provider_gran_application_id_81923564_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_grant_user_id_e8f62af8_fk_app_user_mst_id` FOREIGN KEY (`user_id`) REFERENCES `app_user_mst` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_grant`
--

LOCK TABLES `oauth2_provider_grant` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_grant` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_grant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_idtoken`
--

DROP TABLE IF EXISTS `oauth2_provider_idtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_idtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `jti` char(32) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `scope` longtext NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `application_id` bigint DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `jti` (`jti`),
  KEY `oauth2_provider_idto_application_id_08c5ff4f_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_idtoken_user_id_dd512b59_fk_app_user_mst_id` (`user_id`),
  CONSTRAINT `oauth2_provider_idto_application_id_08c5ff4f_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_idtoken_user_id_dd512b59_fk_app_user_mst_id` FOREIGN KEY (`user_id`) REFERENCES `app_user_mst` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_idtoken`
--

LOCK TABLES `oauth2_provider_idtoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_idtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_idtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_refreshtoken`
--

DROP TABLE IF EXISTS `oauth2_provider_refreshtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_refreshtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` varchar(255) NOT NULL,
  `access_token_id` bigint DEFAULT NULL,
  `application_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `revoked` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `access_token_id` (`access_token_id`),
  UNIQUE KEY `oauth2_provider_refreshtoken_token_revoked_af8a5134_uniq` (`token`,`revoked`),
  KEY `oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_refreshtoken_user_id_da837fce_fk_app_user_mst_id` (`user_id`),
  CONSTRAINT `oauth2_provider_refr_access_token_id_775e84e8_fk_oauth2_pr` FOREIGN KEY (`access_token_id`) REFERENCES `oauth2_provider_accesstoken` (`id`),
  CONSTRAINT `oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_refreshtoken_user_id_da837fce_fk_app_user_mst_id` FOREIGN KEY (`user_id`) REFERENCES `app_user_mst` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_refreshtoken`
--

LOCK TABLES `oauth2_provider_refreshtoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-25 19:02:26
