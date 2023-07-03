from bank_account import BankAccount


class AccountHolder:
    def __init__(self, name, email, interest_rate=0.02, balance=0):
        self.name = name
        self.email = email
        self.accounts = [BankAccount(interest_rate, balance)]

    def add_account(self, interest_rate=0.02, balance=0):
        self.accounts.append(BankAccount(interest_rate, balance))
        return self

    def check_account_index(self, account_index):
        if 0 <= account_index < len(self.accounts):

            return True
        else:
            print(f'There is no account with the index {account_index}')

            return False

    def deposit(self, amount, account_index=0):
        account_exists = self.check_account_index(account_index)

        if account_exists:
            self.accounts[account_index].deposit(amount)

        return self

    def withdraw(self, amount, account_index=0):
        account_exists = self.check_account_index(account_index)

        if account_exists:
            self.accounts[account_index].withdraw(amount)

        return self

    def display_account_info(self, account_index=0):
        account_exists = self.check_account_index(account_index)

        if account_exists:
            self.accounts[account_index].display_account_info()

        return self

    def yield_interest(self, account_index=0):
        account_exists = self.check_account_index(account_index)

        if account_exists:
            self.accounts[account_index].yield_interest()
        return self

    def transfer_money(self, amount, other_user, from_account_index=0, to_account_index=0):

        # Check if user has account at that index
        from_account_exists = self.check_account_index(from_account_index)
        to_account_exists = other_user.check_account_index(to_account_index)

        # check if other user and to account exists
        if from_account_exists and isinstance(other_user, AccountHolder) and to_account_exists:

            # check for sufficient funds
            if self.accounts[from_account_index].balance >= amount:

                # update from_account balance
                self.accounts[from_account_index].withdraw(amount)

                # update other user's account balance
                other_user.deposit(amount)
                print(
                    f'Successfully transferred ${amount:.2f} from {self.name} to {other_user.name}\n')
            else:
                print('Insufficient funds for the transfer.\n')
        return self


print('User 1:')
user_1 = AccountHolder('Joe Blow', 'joe@BlowMyHotRods.com', 0.025, 2000)
user_1.display_account_info().yield_interest().withdraw(
    user_1.accounts[0].balance * 0.5).display_account_info().deposit(150).yield_interest().display_account_info()

user_1.add_account(0.3, 4000).display_account_info(1)

user_2 = AccountHolder('Some Person', 'person@WhoToSendMoneyTo.com')

print('User 2:')
user_2.display_account_info()

print('Transfer money: ')
user_1.transfer_money(500, user_2, 0)
user_2.transfer_money(400, user_1, 0, 1)
user_2.transfer_money(400, user_1, 0, 1)
user_2.transfer_money(20, user_1, 0, 2)
