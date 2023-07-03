class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    # Have this method print all of the users' details on separate lines.
    def display_info(self):
        for key, value in self.__dict__.items():
            print(f'{" ".join(key.split("_")).title()}: {value}')

        print('\n')

    # enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        if self.is_rewards_member:
            print(
                f'{self.first_name.capitalize()} {self.last_name.capitalize()} is already a member!\n')
            return

        self.is_rewards_member = True

    # spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f'{self.first_name.capitalize()} doesn\'t have enough points!\n')
        else:
            self.gold_card_points -= amount


user = User('evan', 'schultz', 'evan@evan.com', '36', False, 500)
user.display_info()
user.enroll()
user.display_info()
user.spend_points(100)
user.spend_points(450)
user.display_info()
user.enroll()
