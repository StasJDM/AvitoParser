import pymysql

class DatabaseSaver:

    IMAGES_TABLE_NAME = "images"
    ADS_TABLE_NAME = "ads"

    def __init__(self):
        self.__connection = pymysql.connect(
            host='localhost',
            user='mysql',
            password='mysql',
            database='ads',
            cursorclass=pymysql.cursors.DictCursor)

    def insert_ad(self, ad):
        with self.__connection as connection:
            sql = "INSERT INTO ads(`id`, `title`, `category`, `time`, `price`, `location`, `address`, `lat`, `lng`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')"
            with connection.cursor() as cursor:
                cursor.execute(sql.format(ad.id,
                                ad.title,
                                ad.category,
                                ad.time,
                                ad.price,
                                ad.location,
                                ad.address,
                                ad.lat,
                                ad.lng))
                cursor.close()
                for img in ad.images:
                    self.insert_image(connection, img)
            connection.commit()

    def save_hash(self, img_hash):
        try:
            with self.__connection as connection:
                with connection.cursor() as cursor:
                    sql = "UPDATE images SET ahash='{0}', dhash='{1}', phash='{2}', whash='{3}', colorhash='{4}', crop_resistant='{5}', is_hashed='1' WHERE name='{6}'"
                    cursor.execute(sql.format(
                        img_hash['ahash'],
                        img_hash['dhash'],
                        img_hash['phash'],
                        img_hash['whash'],
                        img_hash['colorhash'],
                        img_hash['crop_resistant_hash'],
                        img_hash['name']))
                    cursor.close()
                connection.commit()
            print("Сохранен хэш для " + img_hash['name'])
        except Exception:
            print("Ошибка сохранения хэша")

    @classmethod
    def insert_image(cls, connection, img):
        with connection.cursor() as cursor:
            sql = "INSERT INTO images(`name`, `id_publication`, `url`, `number`) VALUES ('{0}', '{1}', '{2}', '{3}')"
            cursor.execute(sql.format(
                img.name,
                img.ad_id,
                img.url,
                img.number))
            cursor.close()

    def get_unhashed_ads(self):
        with self.__connection as connection:
            with connection.cursor() as cursor:
                sql = "SELECT `name` FROM images WHERE is_hashed='0'"
                cursor.execute(sql)
                rows = cursor.fetchall()
                return rows

    def get_hashed_ads(self):
        with self.__connection as connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM images WHERE is_hashed='1'"
                cursor.execute(sql)
                rows = cursor.fetchall()
                return rows
