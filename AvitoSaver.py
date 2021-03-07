import os
import csv
import json
import requests
from PIL import Image
from time import sleep
from AdClass import AdClass

class AvitoSaver:

    SLEEP_TIMING = 5

    CSV_TYPE = ".csv"
    JSON_TYPE = ".json"

    __filename = "avito_ads"
    __ads_data = []

    def __init__(self):
        try:
            os.makedirs("downloads/img")
        except OSError:
            print ("Создать директорию %s не удалось. Возможно, она была создана раньше" % "downloads/img")
        else:
            print ("Успешно создана директория %s " % "downloads/img")

    def set_filename(self, filename):
        self.__filename = filename

    def set_ads_data(self, adArray):
        self.__ads_data = adArray

    def save_to_csv(self):
        with open("downloads/" + self.__filename + self.CSV_TYPE, "w", newline="", encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=AdClass.get_columns())
            for ad in self.__ads_data:
                writer.writerow(ad.get_list_data())

    def add_to_csv(self):
        with open("downloads/" + self.__filename + self.CSV_TYPE, "a", newline="", encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=AdClass.get_columns())
            for ad in self.__ads_data:
                writer.writerow(ad.get_list_data())

    def save_to_json(self):
        with open("downloads/" + self.__filename + self.JSON_TYPE, "w") as file:
            writer = csv.DictWriter(file, fieldnames=AdClass.get_columns())
            ad_list = []
            for ad in self.__ads_data:
                ad_list.append(ad.get_list_data())
            ad_list = ad_list
            json.dump(ad_list, file, indent=4)

    def save_images(self):
        for ad in self.__ads_data:
            images_url = ad.images
            for i in range(len(images_url)):
                res = requests.get(images_url[i], stream=True).raw
                img = Image.open(res)
                image_name = "downloads/img/image_" + str(ad.id) + "_" + str(i) + ".jpg"
                img.save(image_name, "jpeg")
                print("Загружено изображение: " + image_name)
                sleep(self.SLEEP_TIMING)
