from AvitoParser import AvitoParser
from AvitoSaver import AvitoSaver
from DatabaseSaver import DatabaseSaver

avitoParser = AvitoParser("Калининград")
avitoParser.set_category("Квартиры")

items = avitoParser.get_ads(10)

aSaver = AvitoSaver()

for item in items:
    try:
        DatabaseSaver().insert_ad(item)
        aSaver.save_image(item.images)
    except Exception as e:
        print(e)

print("Загрузка завершена")
