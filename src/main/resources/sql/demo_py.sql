/*
 Navicat Premium Data Transfer

 Source Server         : 本地环境
 Source Server Type    : MySQL
 Source Server Version : 80018
 Source Host           : localhost:3306
 Source Schema         : selenium

 Target Server Type    : MySQL
 Target Server Version : 80018
 File Encoding         : 65001

 Date: 06/01/2022 18:23:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for demo_py
-- ----------------------------
DROP TABLE IF EXISTS `demo_py`;
CREATE TABLE `demo_py` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号(必填,相当于步骤,默认从1开始)',
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '相关描述(必填)',
  `model` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '步骤模块(必填)',
  `elementAction` enum('CLICK','SEND_KEYS','SWITCH_TO_FRAME','CLEAR','HOVER','GET_TEXT','ALERT','WAIT','RUN_SCRIPT','REFRESH','SWITCH_WINDOW','SWITCH_MY_FRAME','RUN_METHOD','DRAG') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '查找这个元素后操作的动作(必填)',
  `clickAction` enum('JS','API','BY_TAG_TYPE','RIGHT_CLICK','DOUBLE_CLICK','') CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '点击使用的方法',
  `element` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '要查找的元素(非必填)',
  `findType` enum('ID','NAME','CLASS_NAME','TAG_NAME','XPATH','LINK_TEXT','CSS_SELECTOR') CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '元素查询的方式(非必填)',
  `ext` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '预留字段',
  `valid` enum('Y','N') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'Y' COMMENT '是否有效(必填)',
  `callBack` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '执行回调',
  `wait` int(5) DEFAULT NULL COMMENT '自定义查询这个dom节点需要等待的时间(非必填,单位:秒)',
  `retry` int(5) DEFAULT NULL COMMENT '自定义查询这个dom节点重试次数(非必填)',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='demo';

-- ----------------------------
-- Records of demo_py
-- ----------------------------
BEGIN;
INSERT INTO `demo_py` VALUES (1, '输入alert脚本', '百度', 'RUN_SCRIPT', NULL, NULL, NULL, '{\'script\': \'alert(111)\'}', 'Y', NULL, NULL, NULL);
INSERT INTO `demo_py` VALUES (2, '点击alert', '百度', 'ALERT', NULL, NULL, NULL, NULL, 'Y', NULL, NULL, NULL);
INSERT INTO `demo_py` VALUES (3, '搜索栏输入kw', '百度', 'SEND_KEYS', NULL, 'kw', 'ID', 'selenium', 'Y', '', NULL, NULL);
INSERT INTO `demo_py` VALUES (4, '刷新页面', '百度', 'REFRESH', NULL, NULL, NULL, NULL, 'Y', NULL, NULL, NULL);
INSERT INTO `demo_py` VALUES (5, '搜索栏输入kw', '百度', 'SEND_KEYS', NULL, 'kw', 'ID', 'selenium', 'Y', '', NULL, NULL);
INSERT INTO `demo_py` VALUES (7, '点击百度一下', '百度', 'CLICK', 'API', 'su', 'ID', NULL, 'Y', NULL, NULL, NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
