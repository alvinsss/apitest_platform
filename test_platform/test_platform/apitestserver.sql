/*
Navicat MySQL Data Transfer

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2019-06-19 18:33:06
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
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
INSERT INTO `auth_group` VALUES ('1', 'QA');

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`) USING BTREE,
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissions_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
INSERT INTO `auth_group_permissions` VALUES ('1', '1', '1');
INSERT INTO `auth_group_permissions` VALUES ('2', '1', '2');
INSERT INTO `auth_group_permissions` VALUES ('3', '1', '3');
INSERT INTO `auth_group_permissions` VALUES ('4', '1', '4');
INSERT INTO `auth_group_permissions` VALUES ('5', '1', '5');
INSERT INTO `auth_group_permissions` VALUES ('6', '1', '6');
INSERT INTO `auth_group_permissions` VALUES ('7', '1', '7');
INSERT INTO `auth_group_permissions` VALUES ('8', '1', '8');
INSERT INTO `auth_group_permissions` VALUES ('9', '1', '9');
INSERT INTO `auth_group_permissions` VALUES ('10', '1', '10');
INSERT INTO `auth_group_permissions` VALUES ('11', '1', '11');
INSERT INTO `auth_group_permissions` VALUES ('12', '1', '12');
INSERT INTO `auth_group_permissions` VALUES ('13', '1', '13');
INSERT INTO `auth_group_permissions` VALUES ('14', '1', '14');
INSERT INTO `auth_group_permissions` VALUES ('15', '1', '15');
INSERT INTO `auth_group_permissions` VALUES ('16', '1', '16');
INSERT INTO `auth_group_permissions` VALUES ('17', '1', '17');
INSERT INTO `auth_group_permissions` VALUES ('18', '1', '18');
INSERT INTO `auth_group_permissions` VALUES ('19', '1', '19');
INSERT INTO `auth_group_permissions` VALUES ('20', '1', '20');
INSERT INTO `auth_group_permissions` VALUES ('21', '1', '21');
INSERT INTO `auth_group_permissions` VALUES ('22', '1', '22');
INSERT INTO `auth_group_permissions` VALUES ('23', '1', '23');
INSERT INTO `auth_group_permissions` VALUES ('24', '1', '24');
INSERT INTO `auth_group_permissions` VALUES ('25', '1', '25');
INSERT INTO `auth_group_permissions` VALUES ('26', '1', '26');
INSERT INTO `auth_group_permissions` VALUES ('28', '1', '28');
INSERT INTO `auth_group_permissions` VALUES ('29', '1', '29');
INSERT INTO `auth_group_permissions` VALUES ('30', '1', '30');
INSERT INTO `auth_group_permissions` VALUES ('31', '1', '31');
INSERT INTO `auth_group_permissions` VALUES ('32', '1', '32');
INSERT INTO `auth_group_permissions` VALUES ('33', '1', '33');
INSERT INTO `auth_group_permissions` VALUES ('34', '1', '34');
INSERT INTO `auth_group_permissions` VALUES ('35', '1', '35');
INSERT INTO `auth_group_permissions` VALUES ('36', '1', '36');
INSERT INTO `auth_group_permissions` VALUES ('37', '1', '37');
INSERT INTO `auth_group_permissions` VALUES ('38', '1', '38');
INSERT INTO `auth_group_permissions` VALUES ('39', '1', '39');
INSERT INTO `auth_group_permissions` VALUES ('40', '1', '40');
INSERT INTO `auth_group_permissions` VALUES ('41', '1', '41');
INSERT INTO `auth_group_permissions` VALUES ('42', '1', '42');
INSERT INTO `auth_group_permissions` VALUES ('43', '1', '43');
INSERT INTO `auth_group_permissions` VALUES ('44', '1', '44');
INSERT INTO `auth_group_permissions` VALUES ('45', '1', '45');
INSERT INTO `auth_group_permissions` VALUES ('46', '1', '46');
INSERT INTO `auth_group_permissions` VALUES ('47', '1', '47');
INSERT INTO `auth_group_permissions` VALUES ('48', '1', '48');
INSERT INTO `auth_group_permissions` VALUES ('49', '1', '49');
INSERT INTO `auth_group_permissions` VALUES ('50', '1', '50');
INSERT INTO `auth_group_permissions` VALUES ('51', '1', '51');
INSERT INTO `auth_group_permissions` VALUES ('52', '1', '52');
INSERT INTO `auth_group_permissions` VALUES ('53', '1', '53');
INSERT INTO `auth_group_permissions` VALUES ('54', '1', '54');
INSERT INTO `auth_group_permissions` VALUES ('55', '1', '55');
INSERT INTO `auth_group_permissions` VALUES ('56', '1', '56');
INSERT INTO `auth_group_permissions` VALUES ('57', '1', '57');
INSERT INTO `auth_group_permissions` VALUES ('58', '1', '58');
INSERT INTO `auth_group_permissions` VALUES ('59', '1', '59');
INSERT INTO `auth_group_permissions` VALUES ('60', '1', '60');

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
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`) USING BTREE,
  CONSTRAINT `auth_permission_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can view content type', '4', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('17', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('20', 'Can view session', '5', 'view_session');
INSERT INTO `auth_permission` VALUES ('21', 'Can add user', '6', 'add_userprofile');
INSERT INTO `auth_permission` VALUES ('22', 'Can change user', '6', 'change_userprofile');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete user', '6', 'delete_userprofile');
INSERT INTO `auth_permission` VALUES ('24', 'Can view user', '6', 'view_userprofile');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 项目管理', '7', 'add_project');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 项目管理', '7', 'change_project');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 项目管理', '7', 'delete_project');
INSERT INTO `auth_permission` VALUES ('28', 'Can view 项目管理', '7', 'view_project');
INSERT INTO `auth_permission` VALUES ('29', 'Can add 模块管理', '8', 'add_module');
INSERT INTO `auth_permission` VALUES ('30', 'Can change 模块管理', '8', 'change_module');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete 模块管理', '8', 'delete_module');
INSERT INTO `auth_permission` VALUES ('32', 'Can view 模块管理', '8', 'view_module');
INSERT INTO `auth_permission` VALUES ('33', 'Can add 用例管理', '9', 'add_testcase');
INSERT INTO `auth_permission` VALUES ('34', 'Can change 用例管理', '9', 'change_testcase');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete 用例管理', '9', 'delete_testcase');
INSERT INTO `auth_permission` VALUES ('36', 'Can view 用例管理', '9', 'view_testcase');
INSERT INTO `auth_permission` VALUES ('37', 'Can add User Widget', '10', 'add_userwidget');
INSERT INTO `auth_permission` VALUES ('38', 'Can change User Widget', '10', 'change_userwidget');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete User Widget', '10', 'delete_userwidget');
INSERT INTO `auth_permission` VALUES ('40', 'Can view User Widget', '10', 'view_userwidget');
INSERT INTO `auth_permission` VALUES ('41', 'Can add log entry', '11', 'add_log');
INSERT INTO `auth_permission` VALUES ('42', 'Can change log entry', '11', 'change_log');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete log entry', '11', 'delete_log');
INSERT INTO `auth_permission` VALUES ('44', 'Can view log entry', '11', 'view_log');
INSERT INTO `auth_permission` VALUES ('45', 'Can add Bookmark', '12', 'add_bookmark');
INSERT INTO `auth_permission` VALUES ('46', 'Can change Bookmark', '12', 'change_bookmark');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete Bookmark', '12', 'delete_bookmark');
INSERT INTO `auth_permission` VALUES ('48', 'Can view Bookmark', '12', 'view_bookmark');
INSERT INTO `auth_permission` VALUES ('49', 'Can add User Setting', '13', 'add_usersettings');
INSERT INTO `auth_permission` VALUES ('50', 'Can change User Setting', '13', 'change_usersettings');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete User Setting', '13', 'delete_usersettings');
INSERT INTO `auth_permission` VALUES ('52', 'Can view User Setting', '13', 'view_usersettings');
INSERT INTO `auth_permission` VALUES ('53', 'Can add captcha store', '14', 'add_captchastore');
INSERT INTO `auth_permission` VALUES ('54', 'Can change captcha store', '14', 'change_captchastore');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete captcha store', '14', 'delete_captchastore');
INSERT INTO `auth_permission` VALUES ('56', 'Can view captcha store', '14', 'view_captchastore');
INSERT INTO `auth_permission` VALUES ('57', 'Can add 任务管理', '15', 'add_testtask');
INSERT INTO `auth_permission` VALUES ('58', 'Can change 任务管理', '15', 'change_testtask');
INSERT INTO `auth_permission` VALUES ('59', 'Can delete 任务管理', '15', 'delete_testtask');
INSERT INTO `auth_permission` VALUES ('60', 'Can view 任务管理', '15', 'view_testtask');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$150000$os6qWLVkoHiA$kZoHE1NQJXWcE521i3FTOS0aNE8ghZ8pLx/DJuL9FaM=', '2019-06-05 12:00:58', '1', 'admin', '', '', 'admin@qq.com', '1', '1', '2019-04-09 12:26:11');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$150000$V98Lw12ZjkNB$VHoyoAjtTUdI7aKlxND00VA55/CIVWT4HXn5917SCQ4=', null, '1', 'alvin', '王', '海林', 'aa@qq.com', '1', '1', '2019-04-09 12:29:00');
INSERT INTO `auth_user` VALUES ('3', 'pbkdf2_sha256$150000$os6qWLVkoHiA$kZoHE1NQJXWcE521i3FTOS0aNE8ghZ8pLx/DJuL9FaM=', '2019-06-03 15:14:01', '1', 'wanghailin', '', '', 'wanghailin@baice100.com', '1', '1', '2019-04-09 12:26:11');

-- ----------------------------
-- Table structure for `captcha_captchastore`
-- ----------------------------
DROP TABLE IF EXISTS `captcha_captchastore`;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of captcha_captchastore
-- ----------------------------
INSERT INTO `captcha_captchastore` VALUES ('94', 'XDUI', 'xdui', '544b2dce6cad1fb840af3a532ca96486e0d30534', '2019-06-19 15:00:59');
INSERT INTO `captcha_captchastore` VALUES ('95', 'QIUC', 'qiuc', 'a391d39a73bb630bcc40c242c9dec460db670cf6', '2019-06-19 15:01:13');
INSERT INTO `captcha_captchastore` VALUES ('96', 'RNAZ', 'rnaz', 'f59274c8fdbcaec121705d7c84013da53331903f', '2019-06-19 15:01:14');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`) USING BTREE,
  KEY `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` (`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
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
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('14', 'captcha', 'captchastore');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('8', 'module', 'module');
INSERT INTO `django_content_type` VALUES ('7', 'project', 'project');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('9', 'testcase', 'testcase');
INSERT INTO `django_content_type` VALUES ('15', 'testtask', 'testtask');
INSERT INTO `django_content_type` VALUES ('6', 'users', 'userprofile');
INSERT INTO `django_content_type` VALUES ('12', 'xadmin', 'bookmark');
INSERT INTO `django_content_type` VALUES ('11', 'xadmin', 'log');
INSERT INTO `django_content_type` VALUES ('13', 'xadmin', 'usersettings');
INSERT INTO `django_content_type` VALUES ('10', 'xadmin', 'userwidget');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-06-03 13:53:21');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2019-06-03 13:53:21');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2019-06-03 13:53:21');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2019-06-03 13:53:22');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2019-06-03 13:53:22');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2019-06-03 13:53:22');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2019-06-03 13:53:22');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2019-06-03 13:53:22');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0007_alter_validators_add_error_messages', '2019-06-03 13:53:22');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0008_alter_user_username_max_length', '2019-06-03 13:53:22');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0009_alter_user_last_name_max_length', '2019-06-03 13:53:22');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0010_alter_group_name_max_length', '2019-06-03 13:53:22');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0011_update_proxy_permissions', '2019-06-03 13:53:22');
INSERT INTO `django_migrations` VALUES ('14', 'users', '0001_initial', '2019-06-03 13:53:23');
INSERT INTO `django_migrations` VALUES ('15', 'admin', '0001_initial', '2019-06-03 13:53:24');
INSERT INTO `django_migrations` VALUES ('16', 'admin', '0002_logentry_remove_auto_add', '2019-06-03 13:53:24');
INSERT INTO `django_migrations` VALUES ('17', 'admin', '0003_logentry_add_action_flag_choices', '2019-06-03 13:53:24');
INSERT INTO `django_migrations` VALUES ('18', 'captcha', '0001_initial', '2019-06-03 13:53:24');
INSERT INTO `django_migrations` VALUES ('19', 'sessions', '0001_initial', '2019-06-03 13:53:24');
INSERT INTO `django_migrations` VALUES ('20', 'testcase', '0001_initial', '2019-06-03 13:53:25');
INSERT INTO `django_migrations` VALUES ('21', 'testtask', '0001_initial', '2019-06-03 13:57:46');
INSERT INTO `django_migrations` VALUES ('22', 'xadmin', '0001_initial', '2019-06-03 13:57:47');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('14ggwjaeq0kg91pnfx6r7duacou5kund', 'MzQxYzJhYWJjNmQ1MGYzMTE3NWM1OWMwMmY1MmM0YmE5NDE1ZTMwOTp7fQ==', '2019-06-17 20:54:06');
INSERT INTO `django_session` VALUES ('2un5jp5lcom16wfqpnwqoxdh6a9h8u6e', 'ZTlkYWZmMzZhNTg4NmUzMjZjMDZjYjdkZDhlZTg1YzhjMjllZTc4ODp7Il9hdXRoX3VzZXJfaWQiOiIyNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmY1ZWVkNjg3ZWYwMzc2NTBjYjBiM2MzZmE5ZTdmMGFlOGQ1MDljMiJ9', '2019-06-19 15:54:12');
INSERT INTO `django_session` VALUES ('3cr1m9uaun01v460qncocujz9tbvhs98', 'OTgzNmRmY2MzN2FhOGFhY2M4MmMwZjI0MTE3MGUzMTQ4YjRiMzJkNTp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjBkZTgwNmQzNTY3NjFmN2QxMDhkOWE1ZjU0MTFhMTQ2ZGMyZmUxNCJ9', '2019-06-25 19:13:18');
INSERT INTO `django_session` VALUES ('3g81jtjz6aa5w0zam6lulbjchqtfy4ao', 'MzQxYzJhYWJjNmQ1MGYzMTE3NWM1OWMwMmY1MmM0YmE5NDE1ZTMwOTp7fQ==', '2019-06-17 20:52:35');
INSERT INTO `django_session` VALUES ('42xaq326yeljofemhzuick7jvinjav0j', 'NTVlYWViNWNkNGJlMTdiYjU2MjFlNDY3N2IzYmNhZmY1ZDk3MTAwOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIn0=', '2019-07-03 15:07:52');
INSERT INTO `django_session` VALUES ('4grog5f0esafmqzbexbidza7ezk4ywyh', 'M2MzMjFhZTdhOTU1YWY5YzM5NTU2YmQwMGVmMDNmMzcwOGQ1YzNiNjp7Il9hdXRoX3VzZXJfaWQiOiIyNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzFjZmI0OThlNDU0MzhiZWY3N2FlMjdlNTIwMDVhOGYyZmNkNGFlNyJ9', '2019-06-19 16:09:18');
INSERT INTO `django_session` VALUES ('4mnpjauymsl3thrqqipyncgp8wdqgt85', 'NTVlYWViNWNkNGJlMTdiYjU2MjFlNDY3N2IzYmNhZmY1ZDk3MTAwOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIn0=', '2019-06-24 16:52:37');
INSERT INTO `django_session` VALUES ('4okem0d7bip4a7niqo26tttum1mmin0s', 'MzNkNDMyMDkwMWM5OWM4MTZhNDkzNzNmMDZiMGUzY2E1ZGZhN2RiZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIiwiTElTVF9RVUVSWSI6W1sidXNlcnMiLCJ1c2VycHJvZmlsZSJdLCIiXX0=', '2019-06-20 13:12:42');
INSERT INTO `django_session` VALUES ('55ep3dyz1tdf8e7868a0wt5mbf8au005', 'MzQxYzJhYWJjNmQ1MGYzMTE3NWM1OWMwMmY1MmM0YmE5NDE1ZTMwOTp7fQ==', '2019-06-17 21:03:33');
INSERT INTO `django_session` VALUES ('5au5dx2p4h7wwi8um8wovnnobmw5ipyy', 'MzQxYzJhYWJjNmQ1MGYzMTE3NWM1OWMwMmY1MmM0YmE5NDE1ZTMwOTp7fQ==', '2019-06-17 21:18:35');
INSERT INTO `django_session` VALUES ('7b5u7my1rrl5hk2ogyx26p81dqg6smhe', 'NTVlYWViNWNkNGJlMTdiYjU2MjFlNDY3N2IzYmNhZmY1ZDk3MTAwOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIn0=', '2019-06-27 22:23:46');
INSERT INTO `django_session` VALUES ('9hrhkcqi4xihr2s8fcj7keooxkue4jok', 'ZjM0NGNiM2JhNGI4Y2NhODFiM2RjNTRlY2VlZWE5ZGU1M2VmNzk4ZDp7Il9hdXRoX3VzZXJfaWQiOiIyMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiM2M4YmE0MDQzYTBjMTQ3NGEyZmY2OTk4NGNhOWNmZGY1ZTY1MGM0OSJ9', '2019-06-19 15:35:53');
INSERT INTO `django_session` VALUES ('akef5n92eqh2i7uisvr4mot9pmbtdpb6', 'NTVlYWViNWNkNGJlMTdiYjU2MjFlNDY3N2IzYmNhZmY1ZDk3MTAwOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIn0=', '2019-06-20 19:14:14');
INSERT INTO `django_session` VALUES ('ctr9qr0s6t9jvbnsxc01b6g1bozed9x2', 'NTVlYWViNWNkNGJlMTdiYjU2MjFlNDY3N2IzYmNhZmY1ZDk3MTAwOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIn0=', '2019-07-03 18:32:07');
INSERT INTO `django_session` VALUES ('cvsnenditlnbu5vmthclttoxgi4lvaw5', 'NTVlYWViNWNkNGJlMTdiYjU2MjFlNDY3N2IzYmNhZmY1ZDk3MTAwOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIn0=', '2019-06-30 20:12:20');
INSERT INTO `django_session` VALUES ('dfvn9vlzkw7nqz2rwhdgn6cpu692t9p6', 'NDEwZDY4ZmQ1YTc2YTIxZGI5NDEwMGU5MTE5N2RmMjhiN2EzMTgxMzp7Il9hdXRoX3VzZXJfaWQiOiIzMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTBhMmNmOTJhMGRmODNjZmQyOTEwOGVjZjNhNzEyMjI0MTc2NDNmOCJ9', '2019-07-03 14:07:23');
INSERT INTO `django_session` VALUES ('e2z95pvv4v9qm6yvph1t2g5n8d20iqva', 'Yzg1NjY1MGI5ZWYxYzg3N2Y0YThiOTdmMzAwZWYzNWYzNThmYWMxYTp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTZiMmJhMWIyYzk4NWNkYmUzNTkwZDg5Nzg5NTkyZmE3ZTZkMDFjNSJ9', '2019-06-20 13:35:34');
INSERT INTO `django_session` VALUES ('k3r0q4lb3ln2s4q5nh50co3wpl34l9p5', 'NTVlYWViNWNkNGJlMTdiYjU2MjFlNDY3N2IzYmNhZmY1ZDk3MTAwOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIn0=', '2019-07-03 09:45:34');
INSERT INTO `django_session` VALUES ('kc8tvit1ekn3jyib64u2on4lxn83b7mx', 'ZjRkNTBiNTJhMDU1ODNlYzFjMmI2NWZjYTk4ZTY2ZGJkMDM3NzUyNDp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMzRlZjg3ZWUxZTYzYzMwYTZlMDFjMjFmNmVlY2I0MzhkNjEyYTU1OSJ9', '2019-06-19 16:18:29');
INSERT INTO `django_session` VALUES ('l7378w6w71wz5e7bobrxfj2i37gm5ns7', 'NTVlYWViNWNkNGJlMTdiYjU2MjFlNDY3N2IzYmNhZmY1ZDk3MTAwOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIn0=', '2019-06-18 20:48:27');
INSERT INTO `django_session` VALUES ('mnibyiccrahev114iruawprycrzbb5sl', 'NTVlYWViNWNkNGJlMTdiYjU2MjFlNDY3N2IzYmNhZmY1ZDk3MTAwOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIn0=', '2019-07-02 13:12:33');
INSERT INTO `django_session` VALUES ('moisx9o5edam79z2cavilwwgnjvqbssl', 'ZjNmMjc3MDJmMGIwZDg0NzMxNDEyODc5Yjc0Yjg3MjNiODlmZjEzMjp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MzcxOTAyZmI4YmYwMmNmY2ZmYTI2YjY1OTY0ODg2NzE3NGYxZWQxIn0=', '2019-06-17 15:14:01');
INSERT INTO `django_session` VALUES ('nk670dq3k16xux108ox28cjq3crxp8n8', 'NTVlYWViNWNkNGJlMTdiYjU2MjFlNDY3N2IzYmNhZmY1ZDk3MTAwOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIn0=', '2019-06-30 18:07:06');
INSERT INTO `django_session` VALUES ('nsm0s6vmrt3g5hr940etfk6mshgbmv0m', 'MzQxYzJhYWJjNmQ1MGYzMTE3NWM1OWMwMmY1MmM0YmE5NDE1ZTMwOTp7fQ==', '2019-06-17 21:13:39');
INSERT INTO `django_session` VALUES ('o6ep5e35xq2tvdm432ir2d3q5q59k3em', 'NTVlYWViNWNkNGJlMTdiYjU2MjFlNDY3N2IzYmNhZmY1ZDk3MTAwOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIn0=', '2019-06-24 10:11:14');
INSERT INTO `django_session` VALUES ('pld6p5bduabn9fz5puc5ajtqdqmmgniy', 'ZjYxNWRhNjQ4M2VhNzZhNmQyZjBlOTA3ZTE5NjFlMDI5OTRiMGFmZDp7Il9hdXRoX3VzZXJfaWQiOiIyNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZDgzNWRkODRlYzA3NjJjYzk0ZDhjYWRhY2VlOTQ4ZTAyYWU5NDMzOSJ9', '2019-06-19 15:57:11');
INSERT INTO `django_session` VALUES ('pzmj5w35v7s7c9xrwb11xm2l5t5g72nq', 'NjhiYTg5ZWEyODI3YzgzMzY0YTI2OThlZjcxM2U0YjQ3Mzk2NDFhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiM2I0MGI1NDNjYWNiNzFmNjFlOTZkZmYwYjQ1YmUwMWExMmQ5YWNiYSJ9', '2019-06-25 19:50:02');
INSERT INTO `django_session` VALUES ('qpwn7shitci2r7snri5ch8cogj0609zl', 'OTgzNmRmY2MzN2FhOGFhY2M4MmMwZjI0MTE3MGUzMTQ4YjRiMzJkNTp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjBkZTgwNmQzNTY3NjFmN2QxMDhkOWE1ZjU0MTFhMTQ2ZGMyZmUxNCJ9', '2019-07-01 17:41:20');
INSERT INTO `django_session` VALUES ('so1jsqq8vbupgkp5fqzszax19k0itdev', 'OTgzNmRmY2MzN2FhOGFhY2M4MmMwZjI0MTE3MGUzMTQ4YjRiMzJkNTp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjBkZTgwNmQzNTY3NjFmN2QxMDhkOWE1ZjU0MTFhMTQ2ZGMyZmUxNCJ9', '2019-06-25 19:13:42');
INSERT INTO `django_session` VALUES ('tazpr1wwuiw84ith79z3vqj2mmbw2kgd', 'NTNlYmY5NTc2ZGFhYTlhMjhlNzg2ZGVlMjBjZjU5YmJmY2FkMWYyMjp7Il9hdXRoX3VzZXJfaWQiOiIzMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTdjYTViN2VlMTMzNzg1ZmE1NDVmYWZlMGE2ZWFjZWVkYzFmYjRiZCJ9', '2019-07-03 15:00:29');
INSERT INTO `django_session` VALUES ('us8nh4v2pt441ekvmvubxyw8q6tg94os', 'Yzg1NjY1MGI5ZWYxYzg3N2Y0YThiOTdmMzAwZWYzNWYzNThmYWMxYTp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTZiMmJhMWIyYzk4NWNkYmUzNTkwZDg5Nzg5NTkyZmE3ZTZkMDFjNSJ9', '2019-06-19 16:56:36');
INSERT INTO `django_session` VALUES ('uwg552vgz4m3qek060xwh88hoovupjl5', 'Yzg1NjY1MGI5ZWYxYzg3N2Y0YThiOTdmMzAwZWYzNWYzNThmYWMxYTp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTZiMmJhMWIyYzk4NWNkYmUzNTkwZDg5Nzg5NTkyZmE3ZTZkMDFjNSJ9', '2019-06-20 18:39:39');
INSERT INTO `django_session` VALUES ('z983233cvu53ypx8cc438yhikwxu9kty', 'NTVlYWViNWNkNGJlMTdiYjU2MjFlNDY3N2IzYmNhZmY1ZDk3MTAwOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTBiNzMzNWE3YmZhZGQ0MmVlYTNmZmM5MDVkNTMyMWI3YWU1YmEwIn0=', '2019-06-24 18:49:03');
INSERT INTO `django_session` VALUES ('zds3kptjmn4s2fuwcjfnd74a9wjjfla2', 'Yzg1NjY1MGI5ZWYxYzg3N2Y0YThiOTdmMzAwZWYzNWYzNThmYWMxYTp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTZiMmJhMWIyYzk4NWNkYmUzNTkwZDg5Nzg5NTkyZmE3ZTZkMDFjNSJ9', '2019-06-20 14:24:33');

-- ----------------------------
-- Table structure for `locustmanager_locustscript`
-- ----------------------------
DROP TABLE IF EXISTS `locustmanager_locustscript`;
CREATE TABLE `locustmanager_locustscript` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `scriptname` varchar(50) NOT NULL,
  `host` varchar(200) NOT NULL,
  `encryption` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `locustfile` varchar(1000) NOT NULL,
  `module_id` int(11) NOT NULL,
  `username` varchar(10) NOT NULL,
  `del_status` int(11) NOT NULL,
  `slave_num` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `locustmanager_locust_module_id_b6e286c5_fk_module_mo` (`module_id`) USING BTREE,
  CONSTRAINT `locustmanager_locustscript_ibfk_1` FOREIGN KEY (`module_id`) REFERENCES `module_module` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of locustmanager_locustscript
-- ----------------------------

-- ----------------------------
-- Table structure for `module_module`
-- ----------------------------
DROP TABLE IF EXISTS `module_module`;
CREATE TABLE `module_module` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `describe` longtext NOT NULL,
  `create_time` datetime NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `personal_module_project_id_e87dfb79_fk_personal_project_id` (`project_id`) USING BTREE,
  CONSTRAINT `module_module_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `project_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of module_module
-- ----------------------------

-- ----------------------------
-- Table structure for `project_project`
-- ----------------------------
DROP TABLE IF EXISTS `project_project`;
CREATE TABLE `project_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `describe` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `del_status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of project_project
-- ----------------------------

-- ----------------------------
-- Table structure for `pyunitest_unittestscript`
-- ----------------------------
DROP TABLE IF EXISTS `pyunitest_unittestscript`;
CREATE TABLE `pyunitest_unittestscript` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `username` varchar(10) NOT NULL,
  `scriptname` varchar(50) NOT NULL,
  `create_time` datetime NOT NULL,
  `py_file` varchar(100) NOT NULL,
  `del_status` int(11) NOT NULL,
  `test_result` tinyint(1) NOT NULL,
  `module_id` int(11) NOT NULL,
  `uploadfilename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pyunitest_unittestscript_module_id_4314ff79_fk_module_module_id` (`module_id`) USING BTREE,
  CONSTRAINT `pyunitest_unittestscript_ibfk_1` FOREIGN KEY (`module_id`) REFERENCES `module_module` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of pyunitest_unittestscript
-- ----------------------------

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
  `create_time` datetime NOT NULL,
  `module_id` int(11) NOT NULL,
  `encryption` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `testcase_testcase_module_id_4e4d6811_fk_module_module_id` (`module_id`) USING BTREE,
  CONSTRAINT `testcase_testcase_ibfk_1` FOREIGN KEY (`module_id`) REFERENCES `module_module` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of testcase_testcase
-- ----------------------------

-- ----------------------------
-- Table structure for `testtask_testtask`
-- ----------------------------
DROP TABLE IF EXISTS `testtask_testtask`;
CREATE TABLE `testtask_testtask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `describe` longtext NOT NULL,
  `status` int(11) NOT NULL,
  `cases` longtext NOT NULL,
  `create_time` datetime NOT NULL,
  `del_status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of testtask_testtask
-- ----------------------------

-- ----------------------------
-- Table structure for `users_userprofile`
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile`;
CREATE TABLE `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `unickname` varchar(20) DEFAULT NULL,
  `ubirthday` date DEFAULT NULL,
  `uaddress` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_userprofile
-- ----------------------------
INSERT INTO `users_userprofile` VALUES ('1', 'pbkdf2_sha256$150000$MT0Md1wu6vqd$SVEdXgJa910vOCoTC+KkehhJXKzXPXxYIlvI0n/pxxc=', '2019-06-19 18:32:07', '1', 'admin', '', '', 'admin@qq.com', '1', '1', '2019-06-03 13:59:56', null, '2019-06-03', '');
INSERT INTO `users_userprofile` VALUES ('20', 'pbkdf2_sha256$150000$wE4HwyVE9M3m$T6SRNJ9zUIiwl4shlZgwX5Ku3AuVycZsS8ruwP/LAUY=', '2019-06-19 16:54:21', '0', 'wanghailin', '', '', '', '0', '1', '2019-06-05 13:13:00', null, '2019-06-05', '北京');

-- ----------------------------
-- Table structure for `users_userprofile_groups`
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile_groups`;
CREATE TABLE `users_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_groups_userprofile_id_group_id_823cf2fc_uniq` (`userprofile_id`,`group_id`) USING BTREE,
  KEY `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` (`group_id`) USING BTREE,
  CONSTRAINT `users_userprofile_groups_ibfk_1` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_groups_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_userprofile_groups
-- ----------------------------
INSERT INTO `users_userprofile_groups` VALUES ('1', '20', '1');

-- ----------------------------
-- Table structure for `users_userprofile_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile_user_permissions`;
CREATE TABLE `users_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_user_p_userprofile_id_permissio_d0215190_uniq` (`userprofile_id`,`permission_id`) USING BTREE,
  KEY `users_userprofile_us_permission_id_393136b6_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `users_userprofile_user_permissions_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_userprofile_user_permissions_ibfk_2` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_userprofile_user_permissions
-- ----------------------------

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
  KEY `xadmin_bookmark_content_type_id_60941679_fk_django_co` (`content_type_id`) USING BTREE,
  KEY `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` (`user_id`) USING BTREE,
  CONSTRAINT `xadmin_bookmark_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
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
  `action_time` datetime NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`) USING BTREE,
  KEY `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` (`user_id`) USING BTREE,
  CONSTRAINT `xadmin_log_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_log
-- ----------------------------
INSERT INTO `xadmin_log` VALUES ('1', '2019-06-06 12:53:17', '127.0.0.1', '1', 'QA', 'create', '已添加。', '3', '1');
INSERT INTO `xadmin_log` VALUES ('2', '2019-06-06 12:54:49', '127.0.0.1', '1', 'QA', 'change', '修改 permissions', '3', '1');
INSERT INTO `xadmin_log` VALUES ('3', '2019-06-06 12:55:32', '127.0.0.1', '20', 'wanghailin', 'change', '修改 last_login，groups 和 uaddress', '6', '1');

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
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` (`user_id`) USING BTREE,
  CONSTRAINT `xadmin_usersettings_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
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
  KEY `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` (`user_id`) USING BTREE,
  CONSTRAINT `xadmin_userwidget_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_userwidget
-- ----------------------------
