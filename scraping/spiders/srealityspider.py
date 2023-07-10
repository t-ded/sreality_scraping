import scrapy
import json


class SrealityFlat(scrapy.Item):

    title = scrapy.Field()
    img_urls = scrapy.Field()


class SrealityspiderSpider(scrapy.Spider):
    name = "srealityspider"
    allowed_domains = ["sreality.cz"]
    start_urls = ["https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500"]

    def flatparse(self, response):

        jsoned_resp = response.json()
        flat = SrealityFlat()
        flat["title"] = jsoned_resp["name"]["value"]
        flat["img_urls"] = [image["_links"]["view"]["href"] for image in jsoned_resp["_embedded"]["images"] if image["_links"]["view"]]
        yield flat


    def parse(self, response):
        
        jsoned_resp = response.json()
        for flat in jsoned_resp["_embedded"]["estates"]:
            yield scrapy.Request("https://www.sreality.cz/api" + flat["_links"]["self"]["href"], callback=self.flatparse)
