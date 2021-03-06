from AvitoParser import AvitoParser
from AdClass import AdClass
from AvitoSaver import AvitoSaver
import requests
from PIL import Image
from time import sleep

avitoParser = AvitoParser("Москва")
avitoParser.set_category("Квартиры")

items = avitoParser.get_ads(100)

aSaver = AvitoSaver()
aSaver.set_filename("moscow")
aSaver.set_ads_data(items)
aSaver.save_to_csv()
aSaver.save_to_json()
aSaver.save_images()

print("Загрузка завершена")
