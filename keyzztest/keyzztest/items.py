# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Extracted data - > Temporary containers (items) -> Storing in database

import scrapy


class KeyzztestItem(scrapy.Item):
    # define the fields for your item here like:
    productName = scrapy.Field()
    price = scrapy.Field()
    imageUrl = scrapy.Field()

