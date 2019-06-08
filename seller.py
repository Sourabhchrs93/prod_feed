import uuid
from tinydb import TinyDB
from tinydb import where
from posts import posts


class Seller:
    def __init__(self):
        self.sellers = TinyDB('sellers.json')
        self.posts = posts
        self.sellers.purge()

    def create(self, name, rating):
        seller = {'name': name,
                  'id': str(uuid.uuid4()),
                  'rating': rating
                  }
        self.sellers.insert(seller)

    def delete(self, name):
        self.sellers.remove(where('name') == name)
        self.posts.delete(seller_name=name)

    def publish(self, seller_name, prod_name, price):
        result = self.sellers.search(where('name') == seller_name)[0]
        seller_rating = result['rating']
        self.posts.create(seller_name, seller_rating, prod_name, price)

    def delete_post(self, seller_name, prod_name):
        self.posts.delete(seller_name, prod_name)

    def fetch_all(self):
        return self.sellers.all()

    def clear_all(self):
        self.sellers.purge()