from tinydb import TinyDB
from tinydb import where
import uuid
import datetime


class Posts:
    def __init__(self):
        self.posts = TinyDB('posts.json')
        self.posts.purge()

    def create(self, seller_name, seller_rating, prod_name, price):
        post = {'seller_name': seller_name,
                'prod_name': prod_name,
                'price': price,
                'time': str(datetime.datetime.utcnow()),
                'seller_rating': seller_rating,
                'id': str(uuid.uuid4())
                }
        self.posts.insert(post)

    def delete(self, seller_name=None, prod_name=None):
        if prod_name:
            self.posts.remove(where('prod_name') == prod_name)
        if seller_name:
            self.posts.remove(where('seller_name') == seller_name)

    def fetch_all(self):
        return self.posts.all()

    def fetch_feeds(self, seller_name):
        feeds = self.posts.search(where('seller_name') == seller_name)
        return feeds

    def clear_all(self):
        self.posts.purge()


posts = Posts()
