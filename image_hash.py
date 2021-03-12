from DatabaseSaver import DatabaseSaver
from ImageHasher import ImageHasher

images = DatabaseSaver().get_unhashed_ads()

image_hashes = [ImageHasher.get_hashes(img['name']) for img in images]

for i in image_hashes:
    try:
        DatabaseSaver().save_hash(i)
    except Exception as e:
        print(e)
