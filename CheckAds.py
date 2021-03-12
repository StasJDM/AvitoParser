from AvitoParser import AvitoParser
from AdClass import AdClass
from AvitoSaver import AvitoSaver
from ImageHasher import ImageHasher
from DatabaseSaver import DatabaseSaver
import requests
from PIL import Image
from time import sleep

avitoParser = AvitoParser("Краснодар")
avitoParser.set_category("Квартиры")

ads = DatabaseSaver().get_hashed_ads()

items = avitoParser.get_ads(1)

for i in items:
    for img in i.images:
        res = requests.get(img.url, stream=True).raw
        image = Image.open(res)
        hashes = ImageHasher.get_hashes_by_image(image, img.name)
        for db_hash in ads:
            diff = ImageHasher.get_difference(db_hash, hashes)

print("Загрузка завершена")
