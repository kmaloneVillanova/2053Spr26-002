from bank_account import BankAccount

account1 = BankAccount("123454", 10000)
print(account1)

account1.deposit(5000)
print(account1)
balance=account1.get_balance()
print(balance)