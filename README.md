# AvitoParser - парсер объявлений с авито

## Установка необходимых библиотек

```
pip install requests
pip install Pillow
pip install ImageHash
```

## Запуск парксера

### avito_parser_example.py - Пример использования парсера

```python
# Импорт необходимых классов
from AvitoParser import AvitoParser
from AvitoSaver import AvitoSaver
from DatabaseSaver import DatabaseSaver

# Создание парсера и установка региона
avitoParser = AvitoParser("Калининград")
# Ставим категорию
avitoParser.set_category("Квартиры")

# Загружаем 10 объявлений в список items
items = avitoParser.get_ads(10)
 
# Создание сэйвера
aSaver = AvitoSaver()

# Перебор каждого объявления
for item in items:
    try:
        # Сохранение объявления в БД
        DatabaseSaver().insert_ad(item)
        # Сохранение картинок объявления
        aSaver.save_image(item.images)
    except Exception as e:
        # Если произошла ошибка при сохранение - информируем
        print(e)
        
# Информируем о конце загрузки объявлений
print("Загрузка завершена")

```

### image_hashing_example.py - Пример использования хэщера картинок

```python
# Импорт необходимых классов
from DatabaseSaver import DatabaseSaver
from ImageHasher import ImageHasher

# Загружаем из БД список неотхэшированных картинок
images = DatabaseSaver().get_unhashed_ads()

# Хэшируем изображения
image_hashes = [ImageHasher.get_hashes(img['name']) for img in images]

# Проходимся по картинкам
for i in image_hashes:
    try:
        # Пытаемся сохранить хэши в БД
        DatabaseSaver().save_hash(i)
    except Exception as e:
        # Если все плохо - информируем
        print(e)
```

## Сохранение в базу данных

```python
# Импорт класса для сохранения данных в БД
from DatabaseSaver import DatabaseSaver

# Сохранения объявления в БД
# item - объект классса AdClass
DatabaseSaver().insert_ad(item)
```

### Струтура базы данных для хранения объявлений и картинок

По умолчанию: 
* Host: localhost
* User: mysql
* Password: mysql
* Database: ads

Таблицы:
* ads
* images

#### Таблица - ads
```
CREATE TABLE `ads` (
  `id` bigint UNSIGNED NOT NULL,
  `title` varchar(255) NOT NULL,
  `category` varchar(63) NOT NULL,
  `time` varchar(15) NOT NULL,
  `price` varchar(30) NOT NULL,
  `location` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `lat` varchar(30) NOT NULL,
  `lng` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

#### Таблица - images

```buildoutcfg
CREATE TABLE `images` (
  `name` varchar(50) NOT NULL,
  `id_ad` bigint NOT NULL,
  `url` varchar(255) NOT NULL,
  `number` tinyint UNSIGNED NOT NULL,
  `is_hashed` tinyint(1) NOT NULL DEFAULT '0',
  `ahash` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `dhash` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `phash` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `whash` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `colorhash` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `crop_resistant_hash` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```