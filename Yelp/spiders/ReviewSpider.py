__author__ = 'Tharun'

from Yelp.items import ReviewItem
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv
from selenium import webdriver

with open('users_yelp.csv', 'rU') as file:
    rows = csv.reader(file)
    urls = []
    rows.next()
    for row in rows:
        urls.append("http://www.yelp.com/user_details_reviews_self?userid="+row[0])

class ReviewsSpider(CrawlSpider):
    name = "yelp"
    handle_httpstatus_list = [404]
    download_delay = 0.5
    allowed_domains = ["www.yelp.com"]
    # start_urls = (
    #    'http://www.yelp.com/user_details_reviews_self?userid=--4rAAfZnEIAKJE80aIiYg',
    # )
    start_urls = list(set(urls))
    rules = (
        # Extract next links and parse them with the spider's method parse_start_url
        Rule(LinkExtractor(restrict_xpaths=('//a[@class="page-option prev-next next"]',)),
             follow=True, callback='parse_start_url'),
    )

    def parse_start_url(self, response):
        user_id = response.url.split('?')[-1].split('=')[-1]
        profile = response.xpath('//div[@class="user-profile_info arrange_unit"]')
        name = ''.join(profile.xpath('.//h1/text()').extract())
        location = ''.join(profile.xpath('.//h3[@class="user-location alternate"]/text()').extract())
        friend_count = ''.join(profile.xpath('.//li[@class="friend-count"]/span/strong/text()').extract())
        review_count = ''.join(profile.xpath('.//li[@class="review-count"]/span/strong/text()').extract())
        photo_count = ''.join(profile.xpath('.//li[@class="photo-count"]/span/strong/text()').extract())

        reviews = response.xpath('//ul[@class="ytype ylist ylist-bordered reviews"]/li')
        for review in reviews:
            reviewItem = ReviewItem()
            reviewItem['user_id'] = user_id
            reviewItem['name'] = name
            reviewItem['location'] = location
            reviewItem['friend_count'] = friend_count
            reviewItem['review_count'] = review_count
            reviewItem['photo_count'] = photo_count
            reviewItem['review_id'] = ''.join(review.xpath('.//div[@class="review"]/@data-review-id').extract())
            reviewItem['biz_link'] = ''.join(review.xpath('.//a[@class="biz-name"]/@href').extract())
            reviewItem['biz_name'] = ''.join(review.xpath('.//a[@class="biz-name"]/span/text()').extract())
            reviewItem['price'] =  len(''.join(review.xpath('.//div[@class="price-category"]/span/span/text()').extract()))
            reviewItem['category'] = ';'.join(review.xpath('.//span[@class="category-str-list"]/a/text()').extract())
            reviewItem['address'] =  ';'.join(review.xpath('.//address/text()').extract()).strip()
            reviewItem['rating'] = ''.join(review.xpath('.//i/@title').extract()).strip().split("star")[0].strip()
            reviewItem['review_date'] = ''.join(review.xpath('.//span[@class="rating-qualifier"]/text()').extract()).strip()
            desc_unclean = ''.join(review.xpath('.//p/text()').extract()).rstrip()
            reviewItem['desc'] =  desc_unclean.replace(u"\u2018", "").replace(u"\u2019", "").replace(u"\u201c","").replace(u"\u201d", "").replace(u"\u2026","")
            reviewItem['funny'] = ''.join(review.xpath('.//a[@rel="funny"]/span/span[@class="count"]/text()').extract()).rstrip()
            reviewItem['cool'] = ''.join(review.xpath('.//a[@rel="cool"]/span/span[@class="count"]/text()').extract()).rstrip()
            reviewItem['useful'] = ''.join(review.xpath('.//a[@rel="useful"]/span/span[@class="count"]/text()').extract()).rstrip()
            yield reviewItem
        pass