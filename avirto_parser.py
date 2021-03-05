from AvitoParser import AvitoParser
from AdClass import AdClass
import requests
from PIL import Image
from time import sleep

avitoParser = AvitoParser("Ростов-на-Дону")
avitoParser.set_category("Квартиры")

items = avitoParser.get_ads(2)
for item in items:
    print(item.images_count)

'''
images_url = [i['value']['images']['main'][j] for i in items for j in i['value']['images']['main']]
items_id = [i['value']['id'] for i in items]
print(items)

for item in items_id:
    add_info = AvitoParser.get_add_info_by_id(item)
    print(add_info['images'][0]['640x480'])
    print(len(add_info['images']))

for i in range(len(images_url)):
    res = requests.get(images_url[i], stream=True).raw
    img = Image.open(res)
    image_name = "img/image_" + str(i) + ".jpg"
    img.save(image_name, "jpeg")
    print(image_name + " downloaded")
    sleep(2)
'''
