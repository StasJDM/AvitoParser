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
    
