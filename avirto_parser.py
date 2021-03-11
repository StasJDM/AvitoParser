from AvitoParser import AvitoParser
from AdClass import AdClass
from AvitoSaver import AvitoSaver
from ImageHasher import ImageHasher
from DatabaseSaver import DatabaseSaver
import requests
from PIL import Image
from time import sleep

all_list = []

avitoParser = AvitoParser("Москва")
avitoParser.set_category("Квартиры")

items = avitoParser.get_ads(3)

#databaseSaver = DatabaseSaver()
for i in items:
    DatabaseSaver().insert_ad(i)

'''
aSaver = AvitoSaver()
aSaver.set_filename("ads")
aSaver.set_ads_data(items)
aSaver.add_to_csv()
aSaver.save_images()
'''

print("Загрузка завершена")
