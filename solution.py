
#Create a b ank class that has withdrawal and deposit methods 
#create a MinimumBalanceAccount class that inherits from the bank class 


class BankAccount:
    """A bank."""

    def __init__(self):
        """Initializing."""

        self.balance = 0

    def withdraw(self, amount):
        """Taking money out of my account."""

        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Putting money into my account."""

        self.balance += amount 
        return self.balance


class MinimumBalanceAccount(BankAccount):
    """Pre-determined minimum balance."""

    def __init__(self, minimum_balance):
        """Initializing."""
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        """Taking money out of my account."""

        if self.balance - amount < self.minimum_balance:
            print("Sorry minimum balance must be maintained.")
        else:
            BankAccount.withdraw(self, amount)
            print("Successful withdrawal!")




#TEST CASES

a = BankAccount()
b = BankAccount()

print(a.deposit(100))
print(b.deposit(1000))

print(a.withdraw(30))
print(b.withdraw(250))

a_account = MinimumBalanceAccount(30)
b_account = MinimumBalanceAccount(50)

print(a_account.deposit(1000))
print(b_account.deposit(5))

print(a_account.withdraw(30))
print(b_account.withdraw(40))

