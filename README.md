# JumiaCrawler
This spider is made with scrapy, a python library. It allows us to scrape product data from all available pages in Jumia
#Prerequisites
__env__: Pycharm
__python__ version >3.6
__library__ : scrapy

# run Project
To Run this spider tap the following command in the root directory:
 rm output.json;scrapy crawl jumia -o output.json -a product=<Product name>

# Output
__output.json__ is a json file where the scraped data is stored.




