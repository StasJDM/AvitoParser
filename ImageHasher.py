import imagehash
from PIL import Image

class ImageHasher:

    def __init__(self):
        pass

    def set_image_path(self, image_path):
        self.__image_path = image_path

    @staticmethod
    def get_image(image_name):
        return Image.open("downloads/img/" + image_name)

    @staticmethod
    def get_ahash(image):
        return imagehash.average_hash(image)
    
    @staticmethod
    def get_phash(image):
        return imagehash.phash(image)

    @staticmethod
    def get_dhash(image):
        return imagehash.dhash(image)

    @staticmethod
    def get_whash(image):
        return imagehash.whash(image)

    @staticmethod
    def get_colorhash(image):
        return imagehash.colorhash(image)

    @staticmethod
    def get_crop_resistant_hash(image):
        return imagehash.crop_resistant_hash(image)

    @staticmethod
    def get_difference(hash_x, hash_y):
        return abs(hash_x - hash_y)

    @staticmethod
    def get_crop_difference(hash_original, hash_cropped):
        return hash_original.hash_diff(hash_cropped)

    @staticmethod
    def get_hashes(image_name):
        image = ImageHasher.get_image(image_name)
        ahash = str(ImageHasher.get_ahash(image))
        phash = str(ImageHasher.get_phash(image))
        dhash = str(ImageHasher.get_dhash(image))
        whash = str(ImageHasher.get_whash(image))
        colorhash = str(ImageHasher.get_colorhash(image))
        crop_resistant_hash = str(ImageHasher.get_crop_resistant_hash(image))
        hashes = {
            "name" : image_name,
            "ahash" : ahash,
            "phash" : phash,
            "dhash" : dhash,
            "whash" : whash,
            "colorhash" : colorhash,
            "crop_resistant_hash" : crop_resistant_hash
            }
        print("Вычеслен хэш для: " + image_name)
        return hashes;
