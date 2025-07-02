# create a class for BankAccount
class BankAccount:
    ###constructor
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        print(f"Initial amount is {self.balance}")
        self.balance+=amount
        print(f"{amount} is deposited.New balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient amount!")
        else:
            self.balance-=amount
            print(f"{amount} is withdrwan.new balance is {self.balance}")
            
    def get_balance(self):
        return self.balance
person=BankAccount("vidya",10000)
person.deposit(3000)

person.withdraw(5000)

print(person.get_balance())