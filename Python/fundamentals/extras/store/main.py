from store import Store

store = Store('Test Store')


store.add_product({'name': 'test_name_1', 'price': 20,
                  'category': 'test_category_1'})

store.add_multiple_products([{
    'name': 'test_name_2',
    'price': 20,
    'category': 'test_category_2'
},
    {
    'name': 'test_name_3',
    'price': 20,
    'category': 'test_category_2'
}])

store.products[1].update_price(0.2, False).print_info()
store.products[0].print_info()
store.inflation(0.05)
store.set_clearance('test_category_2', 0.2)

store.sell_product(1)
print(store.products)
