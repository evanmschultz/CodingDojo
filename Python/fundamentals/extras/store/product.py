class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # print out all the product's attributes
    def print_info(self):
        print(f'The {self.name} is a {self.category} and costs ${self.price}')

        return self  # return self so multiple methods can be strung together

    # update the price using conditionals to increase of decrease based on `is_increased` boolean
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

        return self  # return self so multiple methods can be strung together
