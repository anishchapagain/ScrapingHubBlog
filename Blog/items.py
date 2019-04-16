# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BlogItem(scrapy.Item):
    # define the fields for your item here like:
	title = scrapy.Field()
	blogUrl = scrapy.Field()
	author_name = scrapy.Field()
	author_url = scrapy.Field()
	post_date = scrapy.Field()
	comments = scrapy.Field()
	basic_description = scrapy.Field()
	pass