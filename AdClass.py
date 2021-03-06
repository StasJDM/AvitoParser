class AdClass:

    def __init__(self, id, category, title, time):
        self.id = id
        self.category = category
        self.title = title
        self.time = time

    def add_images(self, images):
        self.images_count = len(images)
        self.images = images

    def set_price(self, price):
        self.price = price

    def set_geo(self, location, address, lat, lng):
        self.location = location
        self.address = address
        self.lat = lat
        self.lng = lng

    def get_list_data(self):
        list_data = {
            "id" : self.id,
            "category" : self.category,
            "title" : self.title,
            "time" : self.time,
            "price" : self.price,
            "location" : self.location,
            "address" : self.address,
            "lat" : self.lat,
            "lng" : self.lng,
            "images_count" : self.images_count,
            "images" : self.images
        }

        return list_data

    @staticmethod
    def get_columns():
        columns = ["id",
                   "category",
                   "title",
                   "time",
                   "price",
                   "location",
                   "address",
                   "lat",
                   "lng",
                   "images_count",
                   "images"]
        return columns
