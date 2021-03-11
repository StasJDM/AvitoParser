class ImageClass:

    def __init__(self, name):
        self.name = name

    def __init__(self, image_url, ad_id, number):
        self.name = "image_" + str(ad_id) + "_" + str(number) + ".jpg"
        self.url = image_url
        self.ad_id = ad_id
        self.number = number

    def set_hashes(hash_struct):
        self.ahash = hash_struct['ahash']
        self.dhash = hash_struct['dhash']
        self.phash = hash_struct['phash']
        self.whash = hash_struct['whash']
        self.colorhash = hash_struct['colorhash']
        self.crop_resistant_hash = hash_struct['crop_resistant_hash']
