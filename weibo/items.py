# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field


class UserItem(Item):
    collection = 'users'
    
    id = Field()  # id
    name = Field()  # 昵称
    avatar = Field()  # 头像
    cover = Field()  # 封面图片
    gender = Field()  # 性别
    description = Field()  # 描述
    fans_count = Field()  # 粉丝总数
    follows_count = Field()  # 关注总数
    weibos_count = Field()  # 发布微博总数
    verified = Field()  # 是否认证
    verified_reason = Field()  # 认证理由
    verified_type = Field()  # 认证类型
    follows = Field()  # 关注列表-对接
    fans = Field()  # 粉丝列表-对接
    crawled_at = Field()  # 爬取时间


class UserRelationItem(Item):
    collection = 'users'
    
    id = Field()
    follows = Field()
    fans = Field()


class WeiboItem(Item):
    collection = 'weibos'

    id_str = Field()  # 博文id
    attitudes_count = Field()  # 点赞数
    comments_count = Field()  # 评论数
    reposts_count = Field()  # 转载数
    picture = Field()  # 图片
    pictures = Field()  #
    source = Field()  # 来源
    text = Field()  # 博文
    id = Field()
    name = Field()
    created_at = Field()
    crawled_at = Field()  # 爬取的时间
