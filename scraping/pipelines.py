# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import psycopg2


class PostgresPipeline(object):

    def __init__(self):
        self.create_connection()


    def create_connection(self):
        self.conn = psycopg2.connect(host="postgres",
                                     database="sreality",
                                     user="testuser",
                                     password="testpassword",
                                     port=5432)
        self.curr = self.conn.cursor()


    def process_item(self, item, spider):
        self.store_in_db(item)
        return item

    def store_in_db(self, item):
        try:
            self.curr.execute(f""" INSERT INTO sreality_flats (title, img_urls) VALUES('{item["title"]}', ARRAY {item["img_urls"]});""")
        except BaseException as e:
            print(e)
        self.conn.commit()
