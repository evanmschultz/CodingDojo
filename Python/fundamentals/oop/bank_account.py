class BankAccount():
    accounts = []

    def __init__(self, interest_rate=0.01, balance=0):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited: ${amount}, Balance: ${self.balance:.2f}\n')
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= 5
            print(
                f'Insufficient funds: Charging a $5 fee. New balance: ${self.balance:.2f}\n')
            return self

        self.balance -= amount
        print(f'Withdrew: ${amount}, Balance: ${self.balance:.2f}\n')

        return self

    def display_account_info(self, yield_interest=False, interest_accrued=0):
        if yield_interest:
            print(
                f'You earned ${interest_accrued:.2f} in interest payments. Your new balance is ${self.balance:.2f}\n')
        else:
            print(f'Balance: ${self.balance:.2f}\n')

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
                f'''Account memory location: {account}\nAccount balance: ${account.balance:.2f}\nAccount interest rate: {account.interest_rate * 100}%\n''')


if __name__ == '__main__':  # the code below only runs when this python file is run
    account_1 = BankAccount(0.01, 213.03)
    account_2 = BankAccount(0.03, 4027.86)

    account_1.display_account_info().withdraw(
        200).deposit(10).withdraw(90).yield_interest()
    account_2.yield_interest().yield_interest().yield_interest().yield_interest()

    BankAccount.all_accounts()
