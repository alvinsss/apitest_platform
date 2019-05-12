/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306_qa
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : apitestserver

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2019-05-12 21:54:35
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add permission', '1', 'add_permission');
INSERT INTO `auth_permission` VALUES ('2', 'Can change permission', '1', 'change_permission');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete permission', '1', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('4', 'Can view permission', '1', 'view_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can add group', '2', 'add_group');
INSERT INTO `auth_permission` VALUES ('6', 'Can change group', '2', 'change_group');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete group', '2', 'delete_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can view group', '2', 'view_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can add user', '3', 'add_user');
INSERT INTO `auth_permission` VALUES ('10', 'Can change user', '3', 'change_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete user', '3', 'delete_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can view user', '3', 'view_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can view content type', '4', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('17', 'Can add User Widget', '5', 'add_userwidget');
INSERT INTO `auth_permission` VALUES ('18', 'Can change User Widget', '5', 'change_userwidget');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete User Widget', '5', 'delete_userwidget');
INSERT INTO `auth_permission` VALUES ('20', 'Can view User Widget', '5', 'view_userwidget');
INSERT INTO `auth_permission` VALUES ('21', 'Can add User Setting', '6', 'add_usersettings');
INSERT INTO `auth_permission` VALUES ('22', 'Can change User Setting', '6', 'change_usersettings');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete User Setting', '6', 'delete_usersettings');
INSERT INTO `auth_permission` VALUES ('24', 'Can view User Setting', '6', 'view_usersettings');
INSERT INTO `auth_permission` VALUES ('25', 'Can add log entry', '7', 'add_log');
INSERT INTO `auth_permission` VALUES ('26', 'Can change log entry', '7', 'change_log');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete log entry', '7', 'delete_log');
INSERT INTO `auth_permission` VALUES ('28', 'Can view log entry', '7', 'view_log');
INSERT INTO `auth_permission` VALUES ('29', 'Can add Bookmark', '8', 'add_bookmark');
INSERT INTO `auth_permission` VALUES ('30', 'Can change Bookmark', '8', 'change_bookmark');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete Bookmark', '8', 'delete_bookmark');
INSERT INTO `auth_permission` VALUES ('32', 'Can view Bookmark', '8', 'view_bookmark');
INSERT INTO `auth_permission` VALUES ('33', 'Can add module', '9', 'add_module');
INSERT INTO `auth_permission` VALUES ('34', 'Can change module', '9', 'change_module');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete module', '9', 'delete_module');
INSERT INTO `auth_permission` VALUES ('36', 'Can view module', '9', 'view_module');
INSERT INTO `auth_permission` VALUES ('37', 'Can add project', '10', 'add_project');
INSERT INTO `auth_permission` VALUES ('38', 'Can change project', '10', 'change_project');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete project', '10', 'delete_project');
INSERT INTO `auth_permission` VALUES ('40', 'Can view project', '10', 'view_project');
INSERT INTO `auth_permission` VALUES ('41', 'Can add log entry', '11', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('42', 'Can change log entry', '11', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete log entry', '11', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('44', 'Can view log entry', '11', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('45', 'Can add session', '12', 'add_session');
INSERT INTO `auth_permission` VALUES ('46', 'Can change session', '12', 'change_session');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete session', '12', 'delete_session');
INSERT INTO `auth_permission` VALUES ('48', 'Can view session', '12', 'view_session');
INSERT INTO `auth_permission` VALUES ('49', 'Can add captcha store', '13', 'add_captchastore');
INSERT INTO `auth_permission` VALUES ('50', 'Can change captcha store', '13', 'change_captchastore');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete captcha store', '13', 'delete_captchastore');
INSERT INTO `auth_permission` VALUES ('52', 'Can view captcha store', '13', 'view_captchastore');
INSERT INTO `auth_permission` VALUES ('53', 'Can add 项目管理', '14', 'add_project');
INSERT INTO `auth_permission` VALUES ('54', 'Can change 项目管理', '14', 'change_project');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete 项目管理', '14', 'delete_project');
INSERT INTO `auth_permission` VALUES ('56', 'Can view 项目管理', '14', 'view_project');
INSERT INTO `auth_permission` VALUES ('57', 'Can add 模块管理', '15', 'add_module');
INSERT INTO `auth_permission` VALUES ('58', 'Can change 模块管理', '15', 'change_module');
INSERT INTO `auth_permission` VALUES ('59', 'Can delete 模块管理', '15', 'delete_module');
INSERT INTO `auth_permission` VALUES ('60', 'Can view 模块管理', '15', 'view_module');
INSERT INTO `auth_permission` VALUES ('61', 'Can add test case', '16', 'add_testcase');
INSERT INTO `auth_permission` VALUES ('62', 'Can change test case', '16', 'change_testcase');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete test case', '16', 'delete_testcase');
INSERT INTO `auth_permission` VALUES ('64', 'Can view test case', '16', 'view_testcase');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$150000$os6qWLVkoHiA$kZoHE1NQJXWcE521i3FTOS0aNE8ghZ8pLx/DJuL9FaM=', '2019-05-12 20:52:09.616320', '1', 'admin', '', '', 'admin@qq.com', '1', '1', '2019-04-09 12:26:11.401600');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$150000$V98Lw12ZjkNB$VHoyoAjtTUdI7aKlxND00VA55/CIVWT4HXn5917SCQ4=', null, '1', 'alvin', '王', '海林', 'aa@qq.com', '1', '1', '2019-04-09 12:29:00.000000');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------
INSERT INTO `auth_user_user_permissions` VALUES ('1', '2', '1');
INSERT INTO `auth_user_user_permissions` VALUES ('2', '2', '2');
INSERT INTO `auth_user_user_permissions` VALUES ('3', '2', '3');
INSERT INTO `auth_user_user_permissions` VALUES ('4', '2', '4');
INSERT INTO `auth_user_user_permissions` VALUES ('5', '2', '5');
INSERT INTO `auth_user_user_permissions` VALUES ('6', '2', '6');
INSERT INTO `auth_user_user_permissions` VALUES ('7', '2', '7');
INSERT INTO `auth_user_user_permissions` VALUES ('8', '2', '8');
INSERT INTO `auth_user_user_permissions` VALUES ('9', '2', '9');
INSERT INTO `auth_user_user_permissions` VALUES ('10', '2', '10');
INSERT INTO `auth_user_user_permissions` VALUES ('11', '2', '11');
INSERT INTO `auth_user_user_permissions` VALUES ('12', '2', '12');
INSERT INTO `auth_user_user_permissions` VALUES ('13', '2', '13');
INSERT INTO `auth_user_user_permissions` VALUES ('14', '2', '14');
INSERT INTO `auth_user_user_permissions` VALUES ('15', '2', '15');
INSERT INTO `auth_user_user_permissions` VALUES ('16', '2', '16');
INSERT INTO `auth_user_user_permissions` VALUES ('17', '2', '17');
INSERT INTO `auth_user_user_permissions` VALUES ('18', '2', '18');
INSERT INTO `auth_user_user_permissions` VALUES ('19', '2', '19');
INSERT INTO `auth_user_user_permissions` VALUES ('20', '2', '20');
INSERT INTO `auth_user_user_permissions` VALUES ('21', '2', '21');
INSERT INTO `auth_user_user_permissions` VALUES ('22', '2', '22');
INSERT INTO `auth_user_user_permissions` VALUES ('23', '2', '23');
INSERT INTO `auth_user_user_permissions` VALUES ('24', '2', '24');
INSERT INTO `auth_user_user_permissions` VALUES ('25', '2', '25');
INSERT INTO `auth_user_user_permissions` VALUES ('26', '2', '26');
INSERT INTO `auth_user_user_permissions` VALUES ('27', '2', '27');
INSERT INTO `auth_user_user_permissions` VALUES ('28', '2', '28');
INSERT INTO `auth_user_user_permissions` VALUES ('29', '2', '29');
INSERT INTO `auth_user_user_permissions` VALUES ('30', '2', '30');
INSERT INTO `auth_user_user_permissions` VALUES ('31', '2', '31');
INSERT INTO `auth_user_user_permissions` VALUES ('32', '2', '32');
INSERT INTO `auth_user_user_permissions` VALUES ('33', '2', '33');
INSERT INTO `auth_user_user_permissions` VALUES ('34', '2', '34');
INSERT INTO `auth_user_user_permissions` VALUES ('35', '2', '35');
INSERT INTO `auth_user_user_permissions` VALUES ('36', '2', '36');
INSERT INTO `auth_user_user_permissions` VALUES ('37', '2', '37');
INSERT INTO `auth_user_user_permissions` VALUES ('38', '2', '38');
INSERT INTO `auth_user_user_permissions` VALUES ('39', '2', '39');
INSERT INTO `auth_user_user_permissions` VALUES ('40', '2', '40');
INSERT INTO `auth_user_user_permissions` VALUES ('41', '2', '41');
INSERT INTO `auth_user_user_permissions` VALUES ('42', '2', '42');
INSERT INTO `auth_user_user_permissions` VALUES ('43', '2', '43');
INSERT INTO `auth_user_user_permissions` VALUES ('44', '2', '44');
INSERT INTO `auth_user_user_permissions` VALUES ('45', '2', '45');
INSERT INTO `auth_user_user_permissions` VALUES ('46', '2', '46');
INSERT INTO `auth_user_user_permissions` VALUES ('47', '2', '47');
INSERT INTO `auth_user_user_permissions` VALUES ('48', '2', '48');
INSERT INTO `auth_user_user_permissions` VALUES ('49', '2', '49');
INSERT INTO `auth_user_user_permissions` VALUES ('50', '2', '50');
INSERT INTO `auth_user_user_permissions` VALUES ('51', '2', '51');
INSERT INTO `auth_user_user_permissions` VALUES ('52', '2', '52');

-- ----------------------------
-- Table structure for `captcha_captchastore`
-- ----------------------------
DROP TABLE IF EXISTS `captcha_captchastore`;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of captcha_captchastore
-- ----------------------------
INSERT INTO `captcha_captchastore` VALUES ('1', 'RJEU', 'rjeu', '29a282be552f15fc2de0716c3a08edbfd6e0aadb', '2019-04-21 09:41:11.917192');
INSERT INTO `captcha_captchastore` VALUES ('2', 'AFHA', 'afha', '90337b524e6c910d1545aee3d212ee5674a3c29a', '2019-04-25 17:52:07.366732');
INSERT INTO `captcha_captchastore` VALUES ('3', 'XOVN', 'xovn', '803ebe824d0ed4251d252271731c84f06b4c9a22', '2019-04-25 17:52:31.515114');
INSERT INTO `captcha_captchastore` VALUES ('4', 'MZXB', 'mzxb', 'bd71f184503773a03cf9ced879153710e124d18d', '2019-04-25 17:54:07.873625');
INSERT INTO `captcha_captchastore` VALUES ('5', 'SBBV', 'sbbv', '011ef50d598cd1e7ce5934035e96047e00b06589', '2019-04-25 17:55:18.734678');
INSERT INTO `captcha_captchastore` VALUES ('6', 'YWTH', 'ywth', '901f1788df32a882d834a7fe6fced89df16afb1b', '2019-04-25 17:59:05.709660');
INSERT INTO `captcha_captchastore` VALUES ('7', 'YMUY', 'ymuy', '2414551590b90084db226b82bd5cb6de3feeaef9', '2019-04-25 18:00:44.946336');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('11', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('1', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('13', 'captcha', 'captchastore');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('15', 'module', 'module');
INSERT INTO `django_content_type` VALUES ('9', 'personal', 'module');
INSERT INTO `django_content_type` VALUES ('10', 'personal', 'project');
INSERT INTO `django_content_type` VALUES ('14', 'project', 'project');
INSERT INTO `django_content_type` VALUES ('12', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('16', 'testcase', 'testcase');
INSERT INTO `django_content_type` VALUES ('8', 'xadmin', 'bookmark');
INSERT INTO `django_content_type` VALUES ('7', 'xadmin', 'log');
INSERT INTO `django_content_type` VALUES ('6', 'xadmin', 'usersettings');
INSERT INTO `django_content_type` VALUES ('5', 'xadmin', 'userwidget');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-04-09 12:23:31.743468');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-04-09 12:23:31.873476');
INSERT INTO `django_migrations` VALUES ('3', 'contenttypes', '0002_remove_content_type_name', '2019-04-09 12:23:32.754526');
INSERT INTO `django_migrations` VALUES ('4', 'xadmin', '0001_initial', '2019-04-09 12:23:33.484568');
INSERT INTO `django_migrations` VALUES ('5', 'personal', '0001_initial', '2019-04-09 12:23:44.361190');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2019-04-09 12:25:37.972688');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2019-04-09 12:25:38.174700');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2019-04-09 12:25:38.189701');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2019-04-09 12:25:38.279706');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2019-04-09 12:25:38.283706');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2019-04-09 12:25:38.294707');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2019-04-09 12:25:38.423714');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0009_alter_user_last_name_max_length', '2019-04-09 12:25:38.461716');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0010_alter_group_name_max_length', '2019-04-09 12:25:38.557722');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0011_update_proxy_permissions', '2019-04-09 12:25:38.588723');
INSERT INTO `django_migrations` VALUES ('16', 'admin', '0001_initial', '2019-04-09 12:28:13.828603');
INSERT INTO `django_migrations` VALUES ('17', 'admin', '0002_logentry_remove_auto_add', '2019-04-09 12:28:14.130620');
INSERT INTO `django_migrations` VALUES ('18', 'admin', '0003_logentry_add_action_flag_choices', '2019-04-09 12:28:14.146621');
INSERT INTO `django_migrations` VALUES ('19', 'captcha', '0001_initial', '2019-04-09 12:28:14.194624');
INSERT INTO `django_migrations` VALUES ('20', 'sessions', '0001_initial', '2019-04-09 12:28:14.247627');
INSERT INTO `django_migrations` VALUES ('21', 'personal', '0002_auto_20190409_1330', '2019-04-09 13:33:11.167518');
INSERT INTO `django_migrations` VALUES ('22', 'personal', '0003_auto_20190409_1334', '2019-04-09 13:34:30.550058');
INSERT INTO `django_migrations` VALUES ('23', 'personal', '0002_auto_20190410_2114', '2019-04-10 21:14:51.191312');
INSERT INTO `django_migrations` VALUES ('24', 'testcase', '0001_initial', '2019-05-12 18:50:48.353856');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('0g41lu2pvdihc9lqlfjc2x3zfd92yli0', 'NjBjNWM5N2NjOWIzNzJjYTY0NzE2MzgxOGFhYzVjNGJlYWZkMzUyNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MzcxOTAyZmI4YmYwMmNmY2ZmYTI2YjY1OTY0ODg2NzE3NGYxZWQxIn0=', '2019-05-09 21:50:34.018458');
INSERT INTO `django_session` VALUES ('1wwz2fyb5razqehs1ubiho6rjl0maqam', 'NjBjNWM5N2NjOWIzNzJjYTY0NzE2MzgxOGFhYzVjNGJlYWZkMzUyNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MzcxOTAyZmI4YmYwMmNmY2ZmYTI2YjY1OTY0ODg2NzE3NGYxZWQxIn0=', '2019-04-24 10:32:12.496727');
INSERT INTO `django_session` VALUES ('djtkruii6v745bx7czrbxvxxzf9pzlmu', 'NjBjNWM5N2NjOWIzNzJjYTY0NzE2MzgxOGFhYzVjNGJlYWZkMzUyNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MzcxOTAyZmI4YmYwMmNmY2ZmYTI2YjY1OTY0ODg2NzE3NGYxZWQxIn0=', '2019-04-30 21:25:30.056780');
INSERT INTO `django_session` VALUES ('j4tjha4oy2fwxduark5s2a341l16zg4r', 'NjBjNWM5N2NjOWIzNzJjYTY0NzE2MzgxOGFhYzVjNGJlYWZkMzUyNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MzcxOTAyZmI4YmYwMmNmY2ZmYTI2YjY1OTY0ODg2NzE3NGYxZWQxIn0=', '2019-05-26 20:52:09.620320');
INSERT INTO `django_session` VALUES ('lgnq4m6p653czdlr3oyzap98pszlpou4', 'NjBjNWM5N2NjOWIzNzJjYTY0NzE2MzgxOGFhYzVjNGJlYWZkMzUyNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MzcxOTAyZmI4YmYwMmNmY2ZmYTI2YjY1OTY0ODg2NzE3NGYxZWQxIn0=', '2019-05-11 11:01:06.556398');
INSERT INTO `django_session` VALUES ('qqbieeeotzpb3ne1kh6otvxnbarmgmcv', 'NjBjNWM5N2NjOWIzNzJjYTY0NzE2MzgxOGFhYzVjNGJlYWZkMzUyNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MzcxOTAyZmI4YmYwMmNmY2ZmYTI2YjY1OTY0ODg2NzE3NGYxZWQxIn0=', '2019-04-24 10:24:30.311291');
INSERT INTO `django_session` VALUES ('wh7o5rrl0r2xn1u8aa2omqgkxucvcue9', 'NjBjNWM5N2NjOWIzNzJjYTY0NzE2MzgxOGFhYzVjNGJlYWZkMzUyNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MzcxOTAyZmI4YmYwMmNmY2ZmYTI2YjY1OTY0ODg2NzE3NGYxZWQxIn0=', '2019-05-10 10:15:32.386981');

-- ----------------------------
-- Table structure for `module_module`
-- ----------------------------
DROP TABLE IF EXISTS `module_module`;
CREATE TABLE `module_module` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `describe` longtext NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `personal_module_project_id_e87dfb79_fk_personal_project_id` (`project_id`),
  CONSTRAINT `personal_module_project_id_e87dfb79_fk_personal_project_id` FOREIGN KEY (`project_id`) REFERENCES `project_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of module_module
-- ----------------------------
INSERT INTO `module_module` VALUES ('1', 'test11', '111', '2019-04-09 12:38:22.037390', '1');
INSERT INTO `module_module` VALUES ('10', '模块2', '模块2模块2模块2', '2019-05-12 19:15:25.950370', '1');
INSERT INTO `module_module` VALUES ('11', '模块1项目1', 'EncodingEncoding', '2019-05-12 20:04:30.980816', '8');

-- ----------------------------
-- Table structure for `project_project`
-- ----------------------------
DROP TABLE IF EXISTS `project_project`;
CREATE TABLE `project_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `describe` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of project_project
-- ----------------------------
INSERT INTO `project_project` VALUES ('1', '项目2', '项目2', '1', '2019-04-16 12:35:56.000000', '2019-04-16 12:35:56.000000');
INSERT INTO `project_project` VALUES ('8', '项目1', '少时诵诗书所所所所所所所所', '1', '2019-04-16 18:10:49.957717', '2019-05-12 20:14:51.524309');
INSERT INTO `project_project` VALUES ('12', '项目3', '项目3', '0', '2019-05-12 20:21:09.286915', '2019-05-12 20:21:09.286915');

-- ----------------------------
-- Table structure for `testcase_testcase`
-- ----------------------------
DROP TABLE IF EXISTS `testcase_testcase`;
CREATE TABLE `testcase_testcase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `url` longtext NOT NULL,
  `method` int(11) NOT NULL,
  `header` longtext NOT NULL,
  `parameter_type` int(11) NOT NULL,
  `parameter_body` longtext NOT NULL,
  `result` longtext NOT NULL,
  `assert_type` int(11) NOT NULL,
  `assert_text` longtext NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `module_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `testcase_testcase_module_id_4e4d6811_fk_module_module_id` (`module_id`),
  CONSTRAINT `testcase_testcase_module_id_4e4d6811_fk_module_module_id` FOREIGN KEY (`module_id`) REFERENCES `module_module` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of testcase_testcase
-- ----------------------------
INSERT INTO `testcase_testcase` VALUES ('1', '测试用例1', 'http://httpbin.org/get', '1', '{}', '1', '{\'key1\': \'value1\', \'key2\': [\'value2\', \'value3\']}', '', '1', 'key2', '2019-05-12 19:46:12.449983', '10');
INSERT INTO `testcase_testcase` VALUES ('2', '用例3', 'http://httpbin.org/get', '1', '{}', '1', '{\'key1\': \'value1\', \'key2\': [\'value2\', \'value3\']}', '', '1', 'value2', '2019-05-12 19:51:10.177012', '10');
INSERT INTO `testcase_testcase` VALUES ('3', '用例3', 'http://httpbin.org/get', '1', '{}', '1', '{\'key1\': \'value1\', \'key2\': [\'value2\', \'value3\']}', '', '1', 'value2', '2019-05-12 19:51:13.257188', '10');
INSERT INTO `testcase_testcase` VALUES ('4', '用例3', 'http://httpbin.org/get', '1', '{}', '1', '{\'key1\': \'value1\', \'key2\': [\'value2\', \'value3\']}', '', '1', 'value2', '2019-05-12 19:51:15.775332', '10');
INSERT INTO `testcase_testcase` VALUES ('5', '用例3', 'http://httpbin.org/get', '1', '{}', '1', '{\'key1\': \'value1\', \'key2\': [\'value2\', \'value3\']}', '', '1', 'value2', '2019-05-12 19:55:34.502131', '10');
INSERT INTO `testcase_testcase` VALUES ('6', '用例4', 'http://httpbin.org/get', '1', '{}', '1', ' {\'key1\': \'value1\', \'key2\': [\'value2\', \'value3\']}', '', '1', 'key1', '2019-05-12 19:57:23.306354', '1');
INSERT INTO `testcase_testcase` VALUES ('7', '用例4-有header', 'https://api.github.com/some/endpoint', '1', '{\'user-agent\': \'my-app/0.0.1\'}', '1', ' {\'key1\': \'value1\', \'key2\': [\'value2\', \'value3\']}', '', '1', 'documentation_url', '2019-05-12 19:58:32.566316', '1');
INSERT INTO `testcase_testcase` VALUES ('8', '用例4-post有参', 'http://httpbin.org/post', '2', '', '2', '{\'key1\': \'value1\', \'key2\': \'value2\'}', '', '1', 'Encoding', '2019-05-12 19:59:40.873222', '1');

-- ----------------------------
-- Table structure for `xadmin_bookmark`
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_bookmark`;
CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookmark_content_type_id_60941679_fk_django_co` (`content_type_id`),
  KEY `xadmin_bookmark_user_id_42d307fc_fk_auth_user_id` (`user_id`),
  CONSTRAINT `xadmin_bookmark_content_type_id_60941679_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_bookmark
-- ----------------------------

-- ----------------------------
-- Table structure for `xadmin_log`
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_log`;
CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_log_user_id_bb16a176_fk_auth_user_id` (`user_id`),
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_log
-- ----------------------------
INSERT INTO `xadmin_log` VALUES ('1', '2019-04-09 12:29:05.987586', '127.0.0.1', '2', 'alvin', 'create', '已添加。', '3', '1');
INSERT INTO `xadmin_log` VALUES ('2', '2019-04-09 12:29:40.348551', '127.0.0.1', '2', 'alvin', 'change', '修改 user_permissions，first_name，last_name 和 email', '3', '1');
INSERT INTO `xadmin_log` VALUES ('3', '2019-04-09 12:29:57.124511', '127.0.0.1', '2', 'alvin', 'change', '修改 is_superuser 和 is_staff', '3', '1');

-- ----------------------------
-- Table structure for `xadmin_usersettings`
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_usersettings`;
CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_usersettings
-- ----------------------------
INSERT INTO `xadmin_usersettings` VALUES ('1', 'dashboard:home:pos', '', '1');

-- ----------------------------
-- Table structure for `xadmin_userwidget`
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_userwidget`;
CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_userwidget
-- ----------------------------
