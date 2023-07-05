from product import Product


class Store:
    def __init__(self, name, products=[]):  # initialize instance of the Store class
        self.name = name
        self.products = products

    # adds all the products from a list / make sure it is a LIST of dictionaries with a length >= 1
    def add_products(self, product_list):
        for product in product_list:

            # gets a dictionary as an argument
            self.products.append(
                Product(product['name'], product['price'], product['category']))

        return self  # return self so multiple methods can be strung together

    # if the product id exists in the products list, remove it and print the product
    def sell_product(self, id):
        sold_product = None

        # loop through product list, check if the product id matches the argument id
        for product in self.products:
            if product.id == id:
                sold_product = product  # update sold product variable
                # remove the product from the products list
                self.products.remove(product)
                break  # exit for loop

        if sold_product:
            print(
                f'{sold_product.name} was sold for ${sold_product.price} from the {sold_product.category} category!')
        else:
            print(f'There is no product with an ID of {id} in the inventory!')

        return self  # return self so multiple methods can be strung together

    # increases the price of all the products in the store's product list

    def inflation(self, percentage_increase):
        for product in self.products:
            old_price = product.price

            product.price *= (1 + percentage_increase)
            print(f'{product.name}\'s price was increased by {percentage_increase * 100}%. It was ${old_price} and now costs ${product.price}')

        return self  # return self so multiple methods can be strung together

    # decreases all the prices in a specified category in the store's product list
    def set_clearance(self, category, percentage_decrease):
        for product in self.products:
            if product.category == category:
                old_price = product.price
                product.price *= (1 - percentage_decrease)

                print(
                    f'{product.name}\'s price went down by {percentage_decrease * 100}%. It was ${old_price} and now is ${product.price}')

        return self  # return self so multiple methods can be strung together

    # print out all the product information
    def show_inventory(self):
        for product in self.products:
            product.print_info()

        return self  # return self so multiple methods can be strung together
