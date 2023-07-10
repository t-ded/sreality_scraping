from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.srealityspider import SrealityspiderSpider


SrealityspiderSpider.custom_settings={"ITEM_PIPELINES": {"pipelines.PostgresPipeline": 300}}

process = CrawlerProcess(get_project_settings())
process.crawl(SrealityspiderSpider)
process.start()