# create a bank account class 

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
        print("Initial Balance: ",balance)

    def deposit(self,balance):
        if balance>0:
            self.__balance+=balance
            print(f"Rs. {balance} deposited in your account.")

    def withdraw(self,balance):
        if 0<balance<=self.__balance:
            self.__balance-=balance
            print(f"Rs. {balance} withdraw from your account.")
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Current Balance:",self.__balance)

c1=BankAccount("Sumit",50000)
c1.deposit(10000)
c1.withdraw(1000)
c1.display_balance()                
