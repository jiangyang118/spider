1、安装&启动
https://www.cnblogs.com/hongwest/p/7298257.html

以管理员模式启动CMD，切换到MongoDB的安装目录，并执行命令：mongod --dbpath "D:\mongodb\data\db"  --logpath "D:\mongodb\logs\log.txt"  

备注：事先要在d盘创建 \mongodb文件夹，data文件夹，db文件夹，logs文件夹。
 

2、pip install mongoengine
命令行执行上述命令时，需要关闭fiddler，不然无法下载。