/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - rto_management_system
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
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`desc`,`datetime`,`reply`) values 
(4,9,'dcvgrfgvd','2023-07-02 11:45:24.923565','some problems with server..try again'),
(5,9,'ffgbjkjhygtftgyh','2023-07-02 14:39:51.381868','hello'),
(6,10,'wswdefrfefwdw','2023-07-02 14:40:38.023399','try again');

/*Table structure for table `exam` */

DROP TABLE IF EXISTS `exam`;

CREATE TABLE `exam` (
  `exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_date` varchar(20) DEFAULT NULL,
  `exam_time` varchar(10) DEFAULT NULL,
  `license_request_id` int(11) DEFAULT NULL,
  `exam_type` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `exam` */

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
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `license` */

/*Table structure for table `license_categ` */

DROP TABLE IF EXISTS `license_categ`;

CREATE TABLE `license_categ` (
  `categid` int(11) NOT NULL AUTO_INCREMENT,
  `licensecateg` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`categid`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `license_categ` */

insert  into `license_categ`(`categid`,`licensecateg`) values 
(4,'motor cycle with gear'),
(5,'motor cycle without gear'),
(6,'light motor vehicle'),
(7,'heavy motor vehicle');

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
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

/*Data for the table `license_files` */

insert  into `license_files`(`file_id`,`license_request_id`,`id_proof`,`photo`,`birth certificate`,`education_certificate`,`medical_certificate`) values 
(28,11,'RTO Management - Modules and Tables.docx','RTO Management - Modules and Tables.docx','RTO Management - Modules and Tables.docx','RTO Management - Modules and Tables.docx','RTO Management - Modules and Tables.docx'),
(27,11,'RTO Management - Modules and Tables.docx','RTO Management - Modules and Tables.docx','RTO Management - Modules and Tables.docx','RTO Management - Modules and Tables.docx','RTO Management - Modules and Tables.docx'),
(29,11,'RTO Management - Modules and Tables.docx','RTO Management - Modules and Tables.docx','RTO Management - Modules and Tables.docx','RTO Management - Modules and Tables.docx','RTO Management - Modules and Tables.docx'),
(30,11,'','','','',''),
(31,11,'','','','',''),
(32,11,'','','','','');

/*Table structure for table `licenserequest` */

DROP TABLE IF EXISTS `licenserequest`;

CREATE TABLE `licenserequest` (
  `license_request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `datetime` varchar(50) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `categid` int(11) DEFAULT NULL,
  PRIMARY KEY (`license_request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `licenserequest` */

insert  into `licenserequest`(`license_request_id`,`user_id`,`datetime`,`status`,`categid`) values 
(11,9,'2023-10-01 18:10:22','pending',6),
(10,9,'2023-09-30 22:01:33','pending',4);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(39,'keerthik','12345','user'),
(38,'nesrin','12345','user'),
(34,'palakkad','12345','mvd'),
(1,'admin','admin','admin'),
(40,'aish','12345','user'),
(45,'paravur','12345','mvd'),
(44,'reema','12345','user');

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
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

/*Data for the table `motorvehicledepartment` */

insert  into `motorvehicledepartment`(`mvd_id`,`login_id`,`place`,`rt_number`,`phone`,`email`) values 
(24,34,'palakkad','kl-09','9888888888','palakkad@gmail.com'),
(29,45,'paravur','kl-42','9999999999','paravur@gmail.com');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notify_id` int(11) NOT NULL AUTO_INCREMENT,
  `desc` varchar(50) DEFAULT NULL,
  `datetime` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`notify_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notify_id`,`desc`,`datetime`) values 
(8,'jhgfcdxdctyujki','2023-08-31 10:06:17.710787'),
(7,'abcdefghj','2023-07-02 15:14:12.580877');

/*Table structure for table `permitrequest` */

DROP TABLE IF EXISTS `permitrequest`;

CREATE TABLE `permitrequest` (
  `permit_request_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` int(11) DEFAULT NULL,
  `requested_date` varchar(20) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`permit_request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `permitrequest` */

/*Table structure for table `taxipermit` */

DROP TABLE IF EXISTS `taxipermit`;

CREATE TABLE `taxipermit` (
  `permit_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` int(11) DEFAULT NULL,
  `from_date` varchar(50) DEFAULT NULL,
  `to_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`permit_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `taxipermit` */

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
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`first_name`,`last_name`,`dob`,`gender`,`house_name`,`place`,`pincode`,`blood_group`) values 
(9,38,'nesrin','k s','2001-02-19','female','abcde','paravur','683520','A +ve'),
(10,39,'keerthik','s','2001-12-19','male','abcdef','palakkad','686543','A +ve'),
(11,40,'aish','anilkumar','2001-11-16','female','hgytf','kakkanad','675432','A +ve'),
(12,44,'reema','rafeek','2001-02-12','female','abcde','alappuzha','654328','B +ve');

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
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `vehicles` */

insert  into `vehicles`(`vehicle_id`,`user_id`,`vehicle_type`,`brand_name`,`model_name`,`no_of_seats`,`color`,`applied_date`,`inspection_date`,`fuel_type`,`status`,`vehicle_number`,`number_status`) values 
(17,9,'car','fdf','dvfd',5,'Grey','2023-10-01 22:01:49.468771','pending','diesel','registration pending','pending','pending'),
(16,9,'motorcycle','abcde','abcde',2,'black','2023-09-03 19:56:40.394129','2023-09-20','petrol','registration pending','1010','rejected');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
