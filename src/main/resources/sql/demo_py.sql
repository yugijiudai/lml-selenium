INSERT INTO selenium.demo_py (description,model,elementAction,clickAction,`element`,findType,ext,valid,callBack,wait,retry) VALUES 
('输入alert脚本','百度','RUN_SCRIPT',NULL,NULL,NULL,'{''script'': ''alert(111)''}','Y',NULL,NULL,NULL)
,('点击alert','百度','ALERT',NULL,NULL,NULL,NULL,'Y',NULL,NULL,NULL)
,('搜索栏输入kw','百度','SEND_KEYS',NULL,'kw','ID','selenium','Y','',NULL,NULL)
,('刷新页面','百度','REFRESH',NULL,NULL,NULL,NULL,'Y',NULL,NULL,NULL)
,('搜索栏输入kw','百度','SEND_KEYS',NULL,'kw','ID','selenium','Y','',NULL,NULL)
,('点击百度一下','百度','CLICK','API','su','ID',NULL,'Y',NULL,NULL,NULL)
;