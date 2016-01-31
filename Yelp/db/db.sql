create database yelp_crawl;
DROP TABLE IF EXISTS yelp_crawl.reviews;
CREATE TABLE yelp_crawl.reviews (
review_id varchar(255),
user_id varchar(255),
name varchar(255),
location varchar(255),
friend_count int,
review_count int,
photo_count int,
biz_link text,
biz_name text,
price int,
category text,
address text,
rating double,
review_date varchar(255),
descp text,
funny varchar(255),
cool varchar(255),
useful varchar(255),
updated datetime,
PRIMARY KEY(review_id, user_id)
) DEFAULT CHARSET=utf8;

SELECT review_count, count(*) FROM yelp_crawl.reviews group by user_id;