# AvitoParser - парсер объявлений с авито

## Установка необходимых библиотек

```
pip install requests
pip install Pillow
pip install ImageHash
```

## Запуск парксера

avito_parser_example.py - Пример использования парсера
image_hashing_example.py - Пример использования хэщера картинок

## Сохранение в базу данных

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
```buildoutcfg
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