# 1/2
def parse(self, response):
    # Extracted course titles
    crs_titles = response.xpath(
        '//h4[contains(@class,"block__title")]/text()'
    ).extract()
    # Extracted course descriptions
    crs_descrs = response.xpath(
        '//p[contains(@class,"block__description")]/text()'
    ).extract()
    # Fill in the dictionary
    for crs_title, crs_descr in zip(crs_titles, crs_descrs):
        dc_dict[crs_title] = crs_descr


# 2/2
import scrapy

# Import the CrawlerProcess
from scrapy.crawler import CrawlerProcess


# Create the Spider class
class YourSpider(scrapy.Spider):
    name = "yourspider"

    # start_requests method
    def start_requests(self):
        yield scrapy.Request(url=url_short, callback=self.parse)

    def parse(self, response):
        # My version of the parser you wrote in the previous part
        crs_titles = response.xpath(
            '//h4[contains(@class,"block__title")]/text()'
        ).extract()
        crs_descrs = response.xpath(
            '//p[contains(@class,"block__description")]/text()'
        ).extract()
        for crs_title, crs_descr in zip(crs_titles, crs_descrs):
            dc_dict[crs_title] = crs_descr


# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(YourSpider)
process.start()
