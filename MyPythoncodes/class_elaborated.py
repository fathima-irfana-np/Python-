#LESSON 2 continues
#lets create something new as class Animal :mammals and it's owner

class Animal():
    def __init__(self,animal_name,person,owner_gender):
        self.name=animal_name
        self.gender=owner_gender
        self.ownername=person

    def mammal(self):
        print(f"MAMMAL: i am a mammal,{self.name}")
        print(f"MAMMAL: my owner is {self.ownername}")
        print(f"MAMMAL: my owner is a {self.gender}")
    
    def owner(self):
        print(f"OWNER: hey i am the owner of {self.name}, my name is {self.ownername}")

object1=Animal("Platipus","John","Male")
object2=Animal("Kangaroo","Mary","Female")

object1.mammal()
object1.owner()

object2.mammal()
object2.owner()

#here is an another code, ithil, super() keyword used anu
class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance, interest_rate):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Interest Amount: ${interest:.2f}")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance, minimum_balance):
        super().__init__(account_holder, account_number, balance)
        self.minimum_balance = minimum_balance

    def impose_penalty(self):
        if self.balance < self.minimum_balance:
            penalty = 50
            self.balance -= penalty
            print(f"Balance below minimum. Penalty of ${penalty:.2f} imposed. New balance: ${self.balance:.2f}")
        else:
            print("No penalty. Balance is sufficient.")


# Create objects and demonstrate functionality
savings = SavingsAccount("Alice", "SA12345", 2000, 3.5)
current = CurrentAccount("Bob", "CA67890", 500, 1000)

# Savings Account operations
print("\n[Savings Account]")
savings.display_details()
savings.calculate_interest()
savings.deposit(500)
savings.withdraw(3000)

# Current Account operations
print("\n[Current Account]")
current.display_details()
current.impose_penalty()
current.deposit(1000)
current.impose_penalty()
current.withdraw(700)
