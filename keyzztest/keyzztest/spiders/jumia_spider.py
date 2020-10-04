import scrapy
from ..items import KeyzztestItem

class JumiaSpider(scrapy.Spider):
    name ="jumia"
    #start_urls =[
    #    'https://www.jumia.ma/telephones-smartphones/'
   # ]
    def __init__(self,product=None,*args,**kargs):
        super(JumiaSpider, self).__init__(*args, **kargs)
        self.start_urls = ['https://www.jumia.ma/%s' % product]


    def parse(self, response):
        self.log('i just visited' + response.url)

        items = KeyzztestItem()
        all_div_products = response.css('#jm > main > div.row.-pbm > div.-pvs.col12 > section > div.-paxs.row._no-g._4cl-3cm-shs > article > a')

        for product in all_div_products:

            productName = product.css('div.info > h3::text').extract()
            price = product.css('div.info > div.prc::text').extract()
            imageUrl = product.css('div.img-c > img').xpath("@data-src").extract()

            items['productName'] = productName
            items['price'] = price
            items['imageUrl'] = imageUrl
            yield items

        #next_page = 'https://www.jumia.ma/parfums/?page='+str(JumiaSpider.pageNumber)
        #follow paginition link
        next_page_url = response.css('div.pg-w.-pvxl > a:nth-child(6)::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url,callback=self.parse)
