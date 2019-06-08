from seller import Seller
from customer import Customer

sellers = Seller()
customers = Customer()


# Create 3 sellers
sellers.create('1st seller', 3)
sellers.create('2nd seller', 4.1)
sellers.create('3rd seller', 5.0)


# delete 2nd seller
#print(sellers.fetch_all())
#sellers.delete('2nd seller')
#print(sellers.fetch_all())


# publish feeds
sellers.publish('3rd seller', '1st product', 150)
sellers.publish('1st seller', '2nd product', 200)
sellers.publish('1st seller', '4th product', 250)
sellers.publish('1st seller', '3rd product', 350)
sellers.publish('3rd seller', '5rd product', 5000)
sellers.publish('2nd seller', '6th product', 5555)


# create customers
customers.create('1st customer')
customers.create('2nd customer')
#customers.create('3rd customer')

customers.subscribe('1st customer', '1st seller')
customers.subscribe('1st customer', '2nd seller')
customers.subscribe('1st customer', '3rd seller')

#print(customers.fetch_feeds('1st customer'))
#sellers.delete_post('2nd seller', '6th product')
print(customers.fetch_feeds('1st customer'))
print(customers.fetch_feeds('1st customer', 'seller_rating'))

#print(customers.fetch_all())
# print(customers.fetch_feeds('1st customer', 'time'))

# sellers.delete('3rd seller')
# print(customers.fetch_feeds('1st customer', 'time'))

#sellers.publish('3rd seller', '7th product', 5555)
'''
print(customers.fetch_all())
customers.delete('1st customer')
print(customers.fetch_all())
'''


'''
# customers subscribing to sellers
customers.subscribe('1st customer', '1st seller')
customers.subscribe('1st customer', '3rd seller')

customers.subscribe('2nd customer', '3rd seller')

customers.subscribe('3rd customer', '1st seller')
customers.subscribe('3rd customer', '3rd seller')


# fetch all customers
print(customers.fetch_all())

customers.unsubscribe('1st customer', '3rd seller')

print(customers.fetch_all())


# customer fetch feeds
print(customers.fetch_feeds('1st customer', 'time'))

print(customers.fetch_feeds('2nd customer', 'time'))

print(customers.fetch_feeds('3rd customer', 'time'))
print(customers.fetch_feeds('3rd customer', 'seller_rating'))


'''