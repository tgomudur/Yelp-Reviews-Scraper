# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
import mysql.connector
# from reviews.items import ReviewsItem


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class MySQLStorePipeline(object):

    def __init__(self):
        # create an object to check whether the book has been added
        # self.ids_seen = set()
# create a connection object to the database
        self.conn = mysql.connector.connect(user='root', password='password', database='db_name')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        now = datetime.now().replace(microsecond=0).isoformat(' ')
        insert_book = ("INSERT INTO reviews "
                       "(review_id, user_id, name, location, friend_count,review_count,photo_count,biz_link,biz_name,price,category, address, rating, review_date, descp, funny, cool, useful, updated) "
                       "VALUES (%(review_id)s, %(user_id)s, %(name)s, %(location)s, %(friend_count)s,%(review_count)s,%(photo_count)s,%(biz_link)s,%(biz_name)s,%(price)s,%(category)s,%(address)s,%(rating)s,%(review_date)s,%(descp)s,%(funny)s,%(cool)s, %(useful)s,%(updated)s)")
# data object
        data_book = {'review_id': item['review_id'],
                     'user_id': item['user_id'],
                     'name': item['name'],
                     'location': item['location'],
                     'friend_count': item['friend_count'],
                     'review_count': item['review_count'],
                     'photo_count': item['photo_count'],
                     'biz_link': item['biz_link'],
                     'biz_name': item['biz_name'],
                     'price': item['price'],
                     'category': item['category'],
                     'address': item['address'],
                     'rating': item['rating'],
                     'review_date': item['review_date'],
                     'descp': item['desc'],
                     'funny': item['funny'],
                     'cool': item['cool'],
                     'useful': item['useful'],
                     'updated': now
                     }
# execute the insert query
        try:
            self.cursor.execute(insert_book, data_book)
            self.conn.commit()
            print bcolors.OKGREEN + "success, inserted into database" + bcolors.ENDC
        except Exception as e:
            print bcolors.FAIL + "error, not inserted" + bcolors.ENDC
            print e