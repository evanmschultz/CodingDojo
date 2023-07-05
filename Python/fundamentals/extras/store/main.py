from store import Store

'''
    file to test store's code
'''
store = Store('Test Store')  # instantiate Store instance

# add single product in a list with a length of 1
store.add_products([{'name': 'test_name_1', 'price': 20,
                    'category': 'test_category_1'}])

# add multiple products in a list
store.add_products([{
    'name': 'test_name_2',
    'price': 20,
    'category': 'test_category_2'
},
    {
    'name': 'test_name_3',
    'price': 20,
    'category': 'test_category_2'
}])

# update product and print its info
store.products[1].update_price(0.2, False).print_info()
store.products[0].print_info()
store.inflation(0.05)  # increase store's prices
store.set_clearance('test_category_2', 0.2)  # set clearance on category
store.sell_product(1)  # mark the product with the id of 1 as sold

print('\nShow remaining inventory:')
store.show_inventory()
