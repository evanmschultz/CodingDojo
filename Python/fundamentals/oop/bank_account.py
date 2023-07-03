class BankAccount():
    accounts = []

    def __init__(self, balance, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited: {amount}, Balance: {round(self.balance, 2)}\n')
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= 5
            print(
                f'Insufficient funds: Charging a $5 fee. New balance: {round(self.balance, 2)}\n')
            return self

        self.balance -= amount
        print(f'Withdrew: {amount}, Balance: {round(self.balance, 2)}\n')

        return self

    def display_account_info(self, yield_interest=False, interest_accrued=0):
        if yield_interest:
            print(
                f'You earned {round(interest_accrued, 2)} in interest payments. Your new balance is {round(self.balance, 2)}\n')
        else:
            print(f'Balance: {round(self.balance, 2)}\n')

        return self

    def yield_interest(self):
        interest_accrued = self.balance * (self.interest_rate)
        self.balance += interest_accrued

        self.display_account_info(True, interest_accrued)

        return self

    @classmethod
    def all_accounts(cls):
        for account in cls.accounts:
            print(
                f'''Account memory location: {account}\nAccount balance: {round(account.balance, 2)}\nAccount interest rate: {account.interest_rate}\n''')


account_1 = BankAccount(213.03, 0.01)
account_2 = BankAccount(4027.86, 0.03)

account_1.display_account_info().withdraw(
    200).deposit(10).withdraw(90).yield_interest()
account_2.yield_interest().yield_interest().yield_interest().yield_interest()

BankAccount.all_accounts()
