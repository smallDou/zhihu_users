# 手动添加代理池爬取知乎用户信息
## **安装**
***
## 安装Python
### 至少Python3.5以上
## 安装mongoDB
### 安装好之后开启服务
## 配置代理
### list.txt存放可用代理，可手工测试
## 启动方式
```
cd zhihu_user
scrapy crawl zhihu
```
***
## **Stttings.py 配置**
```
MONGO_URI = 'localhost'  #MongoDB host 使用默认端口号
MONGO_DATABASES = 'zhihu_user' #MongoDB 数据库名称

```

