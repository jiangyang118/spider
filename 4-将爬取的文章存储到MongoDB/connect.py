
from mongoengine import connect
# 连接 mongodb，无需事先创建数据库
connect('weixin', host='localhost', port=27017)