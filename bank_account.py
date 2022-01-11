class BankAccount:
    all_accounts = []
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Chargina $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}, Interest rate {self.interest_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self

vogard = BankAccount(.03, 500)
elan = BankAccount(.1, 2000)

vogard.deposit(200).deposit(150).deposit(600).withdraw(50).yield_interest().display_account_info()
elan.deposit(5000).deposit(300).withdraw(500).withdraw(150).withdraw(200).withdraw(1500).yield_interest().display_account_info()