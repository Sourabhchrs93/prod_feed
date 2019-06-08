import uuid
from tinydb import TinyDB
from tinydb import where
from posts import posts


class Customer:
    def __init__(self):
        self.customer = TinyDB('customer.json')
        self.customer.purge()

    def create(self, name):
            seller = {'name': name,
                      'subscribed': [],
                      'hidden_posts': [],
                      'id': str(uuid.uuid4())}
            self.customer.insert(seller)

    def delete(self, name):
        self.customer.remove(where('name') == name)

    def subscribe(self, customer_name, seller_name):
        result = self.customer.search(where('name') == customer_name)[0]
        subs = result['subscribed']
        subs.append(seller_name)
        self.customer.update({'subscribed': subs}, where('name') == customer_name)

    def unsubscribe(self, customer_name, seller_name):
        result = self.customer.search(where('name') == customer_name)[0]
        subs = result['subscribed']
        try:
            subs.remove(seller_name)
        except:
            return {'error': "did not subscribed"}

        self.customer.update({'subscribed': subs}, where('name') == customer_name)

    def fetch_feeds(self, customer_name, rank='time'):
        result = self.customer.search(where('name') == customer_name)[0]
        subs = result['subscribed']
        feeds = []
        for sub in subs:
            feeds += posts.fetch_feeds(sub)

        if rank == 'time':
            feeds = sorted(feeds, key=lambda i: i['time'], reverse=True)

        if rank == 'seller_rating':
            feeds = sorted(feeds, key=lambda i: i['seller_rating'], reverse=True)

        return feeds

    def hide_post(self, customer_name, post_id):
        result = self.customer.search(where('name') == customer_name)[0]
        hide = result['hidden_posts']
        hide.append(post_id)
        self.customer.update({'hidden_posts': hide}, where('name') == customer_name)

    def fetch_all(self):
        return self.customer.all()

    def clear_all(self):
        self.customer.purge()