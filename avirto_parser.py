from AvitoParser import AvitoParser
from AdClass import AdClass
from AvitoSaver import AvitoSaver
import requests
from PIL import Image
from time import sleep

def add_to_list(list_a, list_b):
    for i in list_b:
        list_a.append(i)
    return list_a

all_list = []

avitoParser = AvitoParser("Москва")
avitoParser.set_category("Квартиры")

items = avitoParser.get_ads(1)

'''
aSaver = AvitoSaver()
aSaver.set_filename("ads")
aSaver.set_ads_data(all_list)
aSaver.add_to_csv()
aSaver.save_images()
'''

print("Загрузка завершена")
