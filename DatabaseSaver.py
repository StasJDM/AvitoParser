import pymysql

class DatabaseSaver:

    IMAGES_TABLE_NAME = "images"

    def __init__(self):
        self.__con = pymysql.connect(
            host='localhost',
            user='mysql',
            password='mysql',
            database='ads')

    def insert_image(self, imageClass)
