#Problem 6-1
favorite_movie = { 'title': 'The Dark Knight', 'rating': 'PG-13', 'director': 'Christopher Nolan', 'year_released': 2008, 'main_actor': 'Heath Ledger', 'box_office': '$1.005 billion',
                  'cast': []}

#Problem 6-2
product = {'item_number': 210, 'product_name': 'Headphones', 'current_price': 59.99}

print('Original Price: $' + str(product['current_price']))

increase_percentage = 0.30
new_price = product['current_price'] * (1 + increase_percentage)

product['current_price'] = new_price

print('Updated price: $' + str(product['current_price']))

print('the price of ' + product['product_name'] + ' has been increased by 30%. ')

#Problem 6-3
print('Favorite Movie Details:')
for key, value in favorite_movie.items():
        print(key + ': ' + str(value))

#Problem 6-4
item_list = [{'item': 'Laptop', 'price': 999.99, 'quantity': 5},
             {'item': 'Smartphone', 'price': 799.99, 'quantity': 10},
             {'item': 'Headphones', 'price': 199.99, 'quantity': 15}]
for item in item_list:
    print('Item: ' + item['item'])
    print('Price: $' + str(item['price']))
    print('Quantity: ' + str(item['quantity']))

#Problem 6-5
favorite_movie['cast'].append('Christian Bale')
favorite_movie['cast'].append('Heath Ledger')
favorite_movie['cast'].append('Aaron Eckhart')
favorite_movie['cast'].append('Maggie Gyllenhall')

print('Favorite Movie Details:')
for key, value in favorite_movie.items():
    if key == 'cast':
        print(key + ':')
        for actor in value:
            print(' - ' + actor)
        else:
             print(key + ':' + str(value))
    