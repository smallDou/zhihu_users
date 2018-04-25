# 分布式+手动添加代理池爬取知乎用户信息
## Python
至少Python3.5以上
## mongoDB
安装好之后开启服务
## 代理配置
list.txt存放可用代理，可手工测试
## 启动方式
```
cd zhihu_users
scrapy crawl zhihu
```
## **Stttings.py 配置**
```
MONGO_URI = 'localhost'  #MongoDB host 使用默认端口号
MONGO_DATABASES = 'zhihu_user' #MongoDB 数据库名称
分布式设置
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
REDIS_URL = 'redis://root:smallq@host:6379'
```

