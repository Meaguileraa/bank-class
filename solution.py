
#Create a b ank class that has withdrawal and deposit methods 
#create a MinimumBalanceAccount class that inherits from the bank class 


class BankAccount:
    """A bank."""

    def __init__(self):
        """Initializing."""

        self.balance = 0

    def withdrawal(self, amount):
        """Taking money out of my account."""

        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Putting money into my account."""

        self.balance += amount 
        return self.balance

#TEST CASES

a = BankAccount()
b = BankAccount()

print(a.deposit(100))
print(b.deposit(1000))

print(a.withdrawal(30))
print(b.withdrawal(250))
