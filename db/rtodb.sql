/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.5.8-log : Database - rto_management_system
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`rto_management_system` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `rto_management_system`;

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `desc` varchar(100) DEFAULT NULL,
  `datetime` varchar(30) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`desc`,`datetime`,`reply`) values 
(1,1,'bbbbb','2023-10-12 12:52:42.777258','hello'),
(2,3,'hiii','2023-10-13 12:33:12.620732','pending');

/*Table structure for table `exam` */

DROP TABLE IF EXISTS `exam`;

CREATE TABLE `exam` (
  `exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_date` varchar(20) DEFAULT NULL,
  `exam_time` varchar(10) DEFAULT NULL,
  `license_request_id` int(11) DEFAULT NULL,
  `exam_type` varchar(50) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `exam` */

insert  into `exam`(`exam_id`,`exam_date`,`exam_time`,`license_request_id`,`exam_type`,`Status`) values 
(1,'2023-10-14','12:55',1,'learnersexam','passed'),
(2,'2023-10-27','13:57',1,'Driving','passed'),
(3,'2023-10-19','12:22',2,'learnersexam','passed'),
(4,'2023-10-27','15:23',2,'Driving','passed');

/*Table structure for table `license` */

DROP TABLE IF EXISTS `license`;

CREATE TABLE `license` (
  `license_id` int(11) NOT NULL AUTO_INCREMENT,
  `license_number` varchar(50) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `license_for` varchar(50) DEFAULT NULL,
  `issued_date` varchar(50) DEFAULT NULL,
  `valid_upto` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`license_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `license` */

insert  into `license`(`license_id`,`license_number`,`user_id`,`license_for`,`issued_date`,`valid_upto`) values 
(1,'111',1,'motor cycle with gear','2023-10-11 19:43:45','2023-10-12'),
(2,'111',1,'motor cycle without gear	','2023-10-11','2023-10-19');

/*Table structure for table `license_categ` */

DROP TABLE IF EXISTS `license_categ`;

CREATE TABLE `license_categ` (
  `categid` int(11) NOT NULL AUTO_INCREMENT,
  `licensecateg` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`categid`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `license_categ` */

insert  into `license_categ`(`categid`,`licensecateg`,`amount`) values 
(1,'motor cycle with gear','2000'),
(2,'motor cycle without gear	','2000'),
(3,'light motor vehicle','4000'),
(4,'heavy motor vehicle','6000');

/*Table structure for table `license_files` */

DROP TABLE IF EXISTS `license_files`;

CREATE TABLE `license_files` (
  `file_id` int(11) NOT NULL AUTO_INCREMENT,
  `license_request_id` int(11) DEFAULT NULL,
  `id_proof` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `birth certificate` varchar(100) DEFAULT NULL,
  `education_certificate` varchar(100) DEFAULT NULL,
  `medical_certificate` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`file_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `license_files` */

insert  into `license_files`(`file_id`,`license_request_id`,`id_proof`,`photo`,`birth certificate`,`education_certificate`,`medical_certificate`) values 
(1,1,'static/files/4cd5417b-ff90-4b7a-a572-d2c3571c9a43RTO Management - Modules and Tables (1).docx','static/files/0d9bf592-cbbf-4d55-b15e-08f0cfa6ebc5RTO Management - Modules and Tables (1).docx','static/files/05900b58-27c2-4a43-b42a-a0348fa93dceRTO Management - Modules and Tables (1).docx','static/files/987f339d-a17d-478d-bd22-824a09a2d209RTO Management - Modules and Tables (1).docx','static/files/3f77339c-ca11-435c-883b-e6582a6f9889RTO Management - Modules and Tables (1).docx'),
(2,2,'static/files/643faa0b-4d9a-4b0a-91b4-a79779e85db7RTO Management - Modules and Tables (1).docx','static/files/b74d6050-5e63-491e-84be-0f9f26c2f14aRTO Management - Modules and Tables (1).docx','static/files/425a7ec0-bd4f-4fbd-8642-383f9de78285RTO Management - Modules and Tables (1).docx','static/files/50ef747f-2f1e-47e8-9482-e8a4be542d9dRTO Management - Modules and Tables (1).docx','static/files/8bcec656-c720-4d4b-bcc2-b291b2a45d28RTO Management - Modules and Tables (1).docx');

/*Table structure for table `licenserequest` */

DROP TABLE IF EXISTS `licenserequest`;

CREATE TABLE `licenserequest` (
  `license_request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `datetime` varchar(50) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `categid` int(11) DEFAULT NULL,
  PRIMARY KEY (`license_request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `licenserequest` */

insert  into `licenserequest`(`license_request_id`,`user_id`,`datetime`,`status`,`categid`) values 
(1,1,'2023-10-12 10:00:43','approved',2),
(2,3,'2023-10-13 12:17:47','approved',3);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'ernakulam','12345','mvd'),
(3,'alappuzha','12345','mvd'),
(4,'anu','12345','user'),
(5,'ammu','12345','user'),
(6,'ernakulam1','12345','mvd'),
(7,'anna','12345','user');

/*Table structure for table `motorvehicledepartment` */

DROP TABLE IF EXISTS `motorvehicledepartment`;

CREATE TABLE `motorvehicledepartment` (
  `mvd_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `rt_number` varchar(10) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mvd_id`)
) ENGINE=MyISAM AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

/*Data for the table `motorvehicledepartment` */

insert  into `motorvehicledepartment`(`mvd_id`,`login_id`,`place`,`rt_number`,`phone`,`email`) values 
(24,34,'palakkad','kl-08','9888888888','palakkad@gmail.com'),
(29,45,'paravur','kl-42','9999999999','paravur@gmail.com'),
(32,49,'ernakulam','kl-07','55555','abi@gmail.com'),
(33,2,'ernakulam','kl-07','1212121212','ernakulam@gmail.com'),
(34,3,'Alappuzha','kl-08','7676767667','alappuzha@gmail.com'),
(35,6,'ernakulam','kl-07','2222222222','ernak@gmail.com');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notify_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `desc` varchar(50) DEFAULT NULL,
  `datetime` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`notify_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notify_id`,`user_id`,`desc`,`datetime`) values 
(1,2,'hiiiiii','2023-10-12 12:53:45.365664'),
(2,3,'hiiiii','2023-10-13 12:33:41.117792');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `payment_for_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`user_id`,`payment_for_id`,`type`,`amount`,`date`) values 
(1,1,1,'license','2000','2023-10-12 10:03:19'),
(2,1,2,'vehicle_registration','5000','2023-10-12 12:25:44'),
(3,2,1,'vehicle_registration','5000','2023-10-12 12:36:31'),
(4,3,2,'license','4000','2023-10-13 12:19:03'),
(5,3,3,'vehicle_registration','5000','2023-10-13 12:25:30');

/*Table structure for table `permitrequest` */

DROP TABLE IF EXISTS `permitrequest`;

CREATE TABLE `permitrequest` (
  `permit_request_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` int(11) DEFAULT NULL,
  `requested_date` varchar(20) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`permit_request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `permitrequest` */

insert  into `permitrequest`(`permit_request_id`,`vehicle_id`,`requested_date`,`status`) values 
(1,2,'2023-10-12 12:41:32','approved'),
(2,2,'2023-10-12','approved'),
(3,3,'2023-10-13 12:28:11','approved'),
(4,3,'2023-10-13','approved');

/*Table structure for table `taxipermit` */

DROP TABLE IF EXISTS `taxipermit`;

CREATE TABLE `taxipermit` (
  `permit_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` int(11) DEFAULT NULL,
  `from_date` date DEFAULT NULL,
  `to_date` date DEFAULT NULL,
  PRIMARY KEY (`permit_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `taxipermit` */

insert  into `taxipermit`(`permit_id`,`vehicle_id`,`from_date`,`to_date`) values 
(1,2,'2010-06-12','2023-10-10'),
(2,3,'2023-01-13','2023-10-12');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `house_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pincode` varchar(10) DEFAULT NULL,
  `blood_group` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`first_name`,`last_name`,`dob`,`gender`,`house_name`,`place`,`pincode`,`blood_group`) values 
(1,4,'anu','m','1995-07-13','female','abc','Ernakulam','121212','A +ve'),
(2,5,'ammu','j','1997-06-14','female','tttt','Alappuzha','555555','B +ve'),
(3,7,'anna','k','1998-06-25','female','abddd','Kottayam','111111','A -ve');

/*Table structure for table `vehicles` */

DROP TABLE IF EXISTS `vehicles`;

CREATE TABLE `vehicles` (
  `vehicle_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `vehicle_type` varchar(10) DEFAULT NULL,
  `brand_name` varchar(50) DEFAULT NULL,
  `model_name` varchar(50) DEFAULT NULL,
  `no_of_seats` int(15) DEFAULT NULL,
  `color` varchar(50) DEFAULT NULL,
  `applied_date` varchar(50) DEFAULT NULL,
  `inspection_date` varchar(50) DEFAULT NULL,
  `fuel_type` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `vehicle_number` varchar(10) DEFAULT NULL,
  `number_status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`vehicle_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `vehicles` */

insert  into `vehicles`(`vehicle_id`,`user_id`,`vehicle_type`,`brand_name`,`model_name`,`no_of_seats`,`color`,`applied_date`,`inspection_date`,`fuel_type`,`status`,`vehicle_number`,`number_status`) values 
(1,2,'car','aaaa','72',22,'black','2023-10-12 12:25:16.564414','2023-10-14','gfy','registration pending','111','approved'),
(3,3,'car','abc','aaa',6,'black','2023-10-13 12:24:55.890011','2023-10-26','aag','registration pending','454','approved'),
(2,1,'van','Abc','72',22,'white','2023-10-12 12:36:05.163792','2023-10-13','gfy','registration pending','222','approved');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
