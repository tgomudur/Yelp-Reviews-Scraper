# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_id = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    friend_count = scrapy.Field()
    review_count = scrapy.Field()
    photo_count = scrapy.Field()
    review_id = scrapy.Field()
    biz_name = scrapy.Field()
    biz_link = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    address = scrapy.Field()
    rating = scrapy.Field()
    review_date = scrapy.Field()
    desc = scrapy.Field()
    funny = scrapy.Field()
    cool = scrapy.Field()
    useful = scrapy.Field()
    pass
