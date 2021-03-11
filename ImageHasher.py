import imagehash
from PIL import Image

class ImageHasher:

    def __init__(self):
        pass

    def set_image_path(self, image_path):
        self.__image_path = image_path

    def get_image(image_name):
        return Image.open(IMAGE_PATH + image_name)

    def get_ahash(image):
        return imagehash.average_hash(image)

    def get_phash(image):
        return imagehash.phash(image)

    def get_dhash(image):
        return imagehash.dhash(image)

    def get_whash(image):
        return imagehash.whash(image)

    def get_colorhash(image):
        return imagehash.colorhash(image)

    def get_crop_resistant_hash(image):
        return imagehash.crop_resistant_hash(image)

    def get_difference(hash_x, hash_y):
        return abs(hash_x - hash_y)

    def get_crop_difference(hash_original, hash_cropped):
        return hash_original.hash_diff(hash_cropped)

    def get_hashes(image_name):
        image = get_image(image_path)
        ahash = str(get_ahash(image))
        phash = str(get_phash(image))
        dhash = str(get_dhash(image))
        whash = str(get_whash(image))
        colorhash = str(get_colorhash(image))
        crop_resistant_hash = str(get_crop_resistant_hash(image))
        hashes = {
            "ahash" : ahash,
            "phash" : phash,
            "dhash" : dhash,
            "whash" : whash,
            "colorhash" : colorhash,
            "crop_resistant_hash" : crop_resistant_hash
            }
        return hashes;
