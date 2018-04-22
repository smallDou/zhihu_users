# -*- coding: utf-8 -*-
import scrapy
import json
from zhihu_user.items import UserItem
import requests

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_user = 'excited-vczh'

    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'

    followees_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    followees_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        yield scrapy.Request(
            self.user_url.format(
                user=self.start_user, include=self.user_query),
            callback=self.parse_user)
        yield scrapy.Request(
            self.followees_url.format(
                user=self.start_user,
                include=self.followees_query,
                limit=20,
                offset=0),
            callback=self.parse_followees)

        yield scrapy.Request(
            self.followers_url.format(
                user=self.start_user,
                include=self.followers_query,
                limit=20,
                offset=0),
            callback=self.parse_followers)

    def parse_user(self, response):
        result = json.loads(response.text)
        item = UserItem()

        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        yield scrapy.Request(
            self.followees_url.format(
                user=result.get('url_token'),
                include=self.followees_query,
                limit=20,
                offset=0),
            callback=self.parse_followees)

        yield scrapy.Request(
            self.followers_url.format(
                user=result.get('url_token'),
                include=self.followers_query,
                limit=20,
                offset=0),
            callback=self.parse_followers)

    def parse_followees(self, response):
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                yield scrapy.Request(
                    self.user_url.format(
                        user=result.get('url_token'),
                        include=self.user_query),
                    callback=self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield scrapy.Request(next_page,callback=self.parse_followees)

    def parse_followers(self, response):
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                yield scrapy.Request(
                    self.user_url.format(
                        user=result.get('url_token'),
                        include=self.user_query),
                    callback=self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield scrapy.Request(next_page,callback=self.parse_followers)
 