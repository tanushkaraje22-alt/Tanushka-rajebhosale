class bankAccount:
    def __init__(self,account_number,inital_balance=0):
        self.account_number=account_number
        self.inital_balance = inital_balance


    def deposit (self,amount):
        if amount>0:
            self.balance+=amount 
            print(f"₹{amount}deposited successfully.")
        else:
            print("deposit amount must be positive.")

    def withdraw(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print(f"₹{amount}withdraw successfully.")
            else:
                print("insufficient balance.")
        else:
            print("withdrawal amount must be positive.")

    def check_balance(self):
        print(f"current balance: ₹{self.balance}")




    account = bankAccount(101,5000)


    account.check_balance()
    account.deposit(2000)
    account.withdraw(1500)     
    account.check_balance()               
           


