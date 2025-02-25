class BankAccount:
    bank_name = "Fred's Bank"
    num_account = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.num_account += 1

    def deposit(self, amount):
        self.balance += 5

    def withdraw(self, amount):
        self.balance -= 10

    @classmethod
    def display_bank_info(cls):
        print(f"Bank Name:{input("Bank Name: ")}, Number of Account:{input("Number in Account: ")}")


bank_account_1 = BankAccount("Charlie", 100)
bank_account_2 = BankAccount("Susie", 200)
BankAccount.display_bank_info()