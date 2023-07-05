from product import Product


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
