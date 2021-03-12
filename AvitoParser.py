from AdClass import AdClass
from ImageClass import ImageClass
import requests
from urllib.request import quote
from urllib.request import unquote
from datetime import datetime
from math import floor
from time import sleep
from time import time

import warnings

warnings.filterwarnings("ignore")


class AvitoParser:

    SLEEP_TIMING = 7
    
    REGION_INFO = 'region_info'
    CATEGORIES_INFO = 'categories_info'
    AVITO_MAIN = 'avito_main'

    avito_urls = {
        'region_info': 'https://m.avito.ru/api/1/slocations?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
                       '&locationId=621540&limit=10&q=',
        'categories_info': 'https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=',
        'avito_main': 'https://avito.ru'
    }

    def __init__(self, region):
        self.__region = region
        self.__region_id = self.get_region_id_by_name(region)

    def change_region(self, region):
        self.__region = region
        self.__region_id = self.get_region_id_by_name(region)

    def get_json_by_request(url):
        try:
            resp = requests.get(url, verify=False)
            json_content = resp.json()
            if 'status' in json_content.keys():
                if json_content['status'] == 'internal-error':
                    print('internal-error')
                    get_json_by_request(url)
            return json_content
        except requests.exceptions.ProxyError:
            sleep(0.001)
            get_json_by_request(url)

    @classmethod
    def get_region_id_by_name(cls, region_name):
        json_content = AvitoParser.get_json_by_request(
            f'{AvitoParser.avito_urls[AvitoParser.REGION_INFO]}{quote(region_name)}')

        if json_content is None:
            return None

        locations = json_content['result']['locations']
        
        return locations[0]['id']


    @staticmethod
    def get_all_categories_by_region_id(region_id):
        json_content = AvitoParser.get_json_by_request(f'{AvitoParser.avito_urls[AvitoParser.CATEGORIES_INFO]}{region_id}')
        main_categories = json_content['categories']

        return main_categories

    def set_category(self, category_name):
        self.__category = category_name
        json_content = AvitoParser.get_json_by_request(f'{AvitoParser.avito_urls[AvitoParser.CATEGORIES_INFO]}{self.__region_id}')
        main_categories = json_content['categories']
        for category in main_categories:
            if category['name'] == category_name:
                self.__category_id = category['name']
            if 'children' in category.keys():
                subcategories = category['children']
                for subcategory in subcategories:
                    if subcategory['name'] == category_name:
                        self.__category_id = subcategory['id']

    def get_ads(self, limit_shows=1):
        time = floor(datetime.timestamp(datetime.now().replace(second=0, microsecond=0)))

        json_content = AvitoParser.get_json_by_request(
            'https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&'
            f'locationId={int(self.__region_id)}&categoryId={self.__category_id}&page=1&display=list&limit={limit_shows}'
        )

        items = json_content['result']['items']

        ads = []
        for item in items:
            if (item['type'] == "item"):
                try:
                    item = item['value']
                    adClass = AdClass(item['id'], item['category']['name'], item['title'], item['time'])
                    adClass.set_price(item['price'])
                    adClass.set_geo(item['location'], item['address'], item['coords']['lat'], item['coords']['lng'])
                    images = self.get_ad_info_by_id(adClass.id)['images']
                    images_class = []
                    for i in range(len(images)):
                        img_cls = ImageClass(images[i]['640x480'], adClass.id, i)
                        images_class.append(img_cls)
                    adClass.add_images(images_class)
                    ads.append(adClass)
                    print("Загружено объявление " + str(item['id']))
                    sleep(self.SLEEP_TIMING)
                except Exception as e:
                    print("Не удалось загрузить объявление")
                    print(e)

        return ads


    @classmethod
    def get_add_json_info_by_id(cls, add_id):
        json_content = AvitoParser.get_json_by_request(
            f'https://m.avito.ru/api/14/items/{add_id}?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        )

        return json_content

    @classmethod
    def get_ad_info_by_id(cls, add_id):
        add_json_info = AvitoParser.get_add_json_info_by_id(add_id)

        return add_json_info

    @property
    def region(self):
        return self.__region

    @property
    def region_id(self):
        return self.__region_id

    @property
    def category(self):
        return self.__category

    @property
    def category_id(self):
        return self.__category_id
