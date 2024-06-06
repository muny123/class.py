#create a class fo the acc creation and methods
class Account:
    def __init__(self, acc_name, acc_number, acc_type, balance=0.0):
        self.acc_name = acc_name
        self.acc_number = acc_number
        self.acc_type = acc_type
        self.balance = balance
        
#deposit method that add total to the balance
    def deposit(self, amount):
        # check the amount is graeter than the required amount
        if amount > 0:
            #add the amountto the balance
            self.balance  += amount
        else:
            print("Amount must be greater than o")
            
# withdraw funcion(method) that substract from the balance
    def withdraw(self, amount):
        # check the amount is greater than 0
        if amount > 0:
            # check the balance is greater than ther amount
            if self.balance >= amount:
                #deduct the amount from the balance
                self.balance -= amount
                print(f"{self.balance} has been deducted from your account")
            else:
                print("Insufficient balance")
        else:
            print("Amount must be greater than 0")
            
# Transfer function that withdraw from one account and deposit to another account
    def transfer(self, deposit_acc, amount):
        # check if acc number exist
        if self and deposit_acc:
            # check balance for withdrawal amount is more than specified
            if self.balance >= amount:
            # withdraw amount from the account
               self.withdraw(amount)
               # deposit amount to deposit account
               deposit_acc.deposit(amount)
            else:
                print("Insufficient balance")
        else:
            print("Accout do not exist")
    
    
    # create  a string mettod to able the functions perform there task well 
    def __str__(self):
        return f"{self.acc_name} with account number: {self.acc_number} {self.acc_type} has a balance of {self.balance}"
    
# testing of the class Account
account1 = Account("Munira", 123456789, "savings", 3000)
print(account1)
account1.deposit(20000)
print(account1)
account1.withdraw(10000)
print(account1)
            
        
        
        