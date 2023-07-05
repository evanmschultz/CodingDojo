class Store:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products

    def add_product(self, product):
        self.products.append(
            Product(product['name'], product['price'], product['category']))

    def add_multiple_products(self, product_list):
        for product in product_list:
            self.add_product(product)

    def sell_product(self, id):  # use index for id
        sold_product = self.products.pop(id)
        print(f'{sold_product.name} was sold')

    def inflation(self, percentage_increase):
        for product in self.products:
            old_price = product.price

            product.price *= (1 + percentage_increase)
            print(f'{product.name}\'s price was increased by {percentage_increase * 100}%. It was ${old_price} and now costs ${product.price}')

    def set_clearance(self, category, percentage_decrease):
        for product in self.products:
            if product.category == category:
                old_price = product.price
                product.price *= (1 - percentage_decrease)

                print(
                    f'{product.name}\'s price went down by {percentage_decrease * 100}%. It was ${old_price} and now is ${product.price}')


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def print_info(self):
        print(f'The {self.name} is a {self.category} and costs ${self.price}')

        return self

    def update_price(self, percent_change, is_increased):
        old_price = self.price

        if is_increased:
            self.price *= (1 + percent_change)

            print(
                f'{self.name}\'s rice went up by {percent_change * 100}%. It was ${old_price} and is now ${self.price}')
        else:
            self.price *= (1 - percent_change)

            print(
                f'{self.name}\'s price went down by {percent_change * 100}%. It was ${old_price} and is now ${self.price}')

        return self


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
