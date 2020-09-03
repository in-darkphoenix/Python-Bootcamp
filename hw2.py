class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Name: {self.owner} \nAvailable Balance: Rs.{self.balance}."

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} deposit accepted. \nAvailable Balance: Rs.{self.balance}.")

    def withdrawl(self, amount):
        if amount > self.balance:
            print(f'Withdrawl amount exceeds your current balance: Rs.{self.balance}')
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawl from the account. \nAvailable Balance: Rs.{self.balance}")
    

acc = Account("Phoenix", 10000000)
print(acc.owner)
print(acc.balance)
print(acc)
acc.withdrawl(5000000)
acc.withdrawl(4000000)
acc.deposit(5000)
acc.deposit(420)
acc.withdrawl(5000000)
print(acc)