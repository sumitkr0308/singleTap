# Create a class AccountHolder with method get_details().
# Create another class BankBranch with method get_branch_info().
# Create a third class Account that inherits from both and adds method get_account_info().
# Call all methods using Account class object.

class AccountHolder:
    def get_details(self):
        print("Name : ABC")
class BankBranch:
    def get_branch_info(self):
        print("Branch Name: XYZ")

class Account(AccountHolder,BankBranch):
    def get_account_info(self):
        print(""" 
              Acc. No.: 125674
              Balance: Rs. 500000
                """)

a1=Account()
a1.get_details()
a1.get_branch_info()
a1.get_account_info()

