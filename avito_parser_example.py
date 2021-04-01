from AvitoParser import AvitoParser
from AdClass import AdClass
from AvitoSaver import AvitoSaver
from ImageHasher import ImageHasher
from DatabaseSaver import DatabaseSaver
import requests
from PIL import Image
from time import sleep

all_list = []

avitoParser = AvitoParser("Калининград")
avitoParser.set_category("Квартиры")

items = avitoParser.get_ads(100)

aSaver = AvitoSaver()

for item in items:
    try:
        DatabaseSaver().insert_ad(item)
        aSaver.save_image(item.images)
    except Exception as e:
        print(e)

print("Загрузка завершена")
