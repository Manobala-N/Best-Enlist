#Banking Details

class My_Bank_Account(Deposit,Withdraw):
    def __init__(self):
        self.balance=0
        print(" Welcome to ATM ")
    

class Deposit():
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
        print("\n Balance:",self.balance)

class Withdraw: 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance=self.balance-amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

        
    def display(self):
        print("\n Net Available Balance=",(self.balance))

My_account_details = My_Bank_Account()
My_account_details.deposit()
My_account_details.withdraw()
My_account_details.display()

#OUTPUT
#Welcome to ATM 

#Enter amount to be Deposited: 10000

#Amount Deposited: 10000.0

#Balance: 10000.0

#Enter amount to be Withdrawn: 7500

#You Withdrew: 7500.0

#Net Available Balance= 2500.0
