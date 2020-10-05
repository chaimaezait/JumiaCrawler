# JumiaCrawler
This spider is made with scrapy, a python library. It allows us to scrape product data from all available pages in Jumia

# Prerequisites

__env__: Pycharm
__python__ version >3.6
__library__ : scrapy

# Run Project

To Run this spider tap the following command in the root directory(./keyzztest):

 __rm output.json;scrapy crawl jumia -o output.json -a product=Product_name__

# Output

__output.json__ is a json file where the scraped data is stored.
# Spider

Go to "./keyzztest/keyzztest/spiders/" directory 

in the __jumia_spider.py__ you will find the scraping algorithm
