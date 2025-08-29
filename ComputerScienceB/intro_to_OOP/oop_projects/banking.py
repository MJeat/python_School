
'''
The program belows implements a simple banking system with two classes: Account and SavingsAccount. 
1. The Account class represents a basic bank account with attributes such as id, balance, and annual interest rate. It provides methods to get and set these attributes, calculate monthly interest, and perform withdrawals and deposits.
2. The SavingsAccount class inherits from the Account class and adds additional attributes for minimum balance and penalty fee

I have discovered how to use the super().__init__() function to call from the parent class. This function is used to call all the parameters of the parent class (id, balance, and annualInterestRate). 
However, if you don't include this function, it will be 2 seperate classes.

Moreover, I have added a basic security practice to ensures the arguments for both classes are validated

'''


class Account:
    def __init__(self, id, balance, annualInterestRate):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def account_info(self):
        print("ID:", self.id)
        print(F"Balance: ${self.balance}")
        print(f"Annual Interest Rate: {self.annualInterestRate}%")
        print(f"Monthly Interest Rate: {self.getMonthlyInterestRate():.4f}%") # Learned the format specifier to limit decimal places using f-strings
        print(f"Monthly Interest: ${self.getMonthlyInterest():.2f}")

    def getID(self) -> int:
        return self.id

    def setID(self, id):
        self.id = id

    def getBalance(self)->float:
        return self.balance

    def setBalance(self, balance: float)->float:
        self.balance = balance

    def getAnnualInterestRate(self)-> float:
        return self.annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate: float):
        self.annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self) -> float:
        return self.annualInterestRate / 12 / 100

    def getMonthlyInterest(self)->float:
        return self.balance * self.getMonthlyInterestRate()

    def withdraw(self, balance: float):
        # Security checking to make sure the balance argument is a float or the integer value. Don't confuse with balance: float. This part is to indicate that this function should expect a float value. Integer or float is okay as long as it is a positive number 
        if not isinstance(balance, (int, float)):
            print("Invalid input: Please enter a number.")
            return
        print(f"Withdrawing ${balance}...")
        if balance > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= balance

    def deposit(self, balance: float):
        # Security checking to make sure the balance argument is a float or the integer value. Don't confuse with balance: float. This part is to indicate that this function should expect a float value. Integer or float is okay as long as it is a positive number 
        if not isinstance(balance, (int, float)):
            print("Invalid input: Please enter a number.")
            return
        print(f"Depositing ${balance}...")
        self.balance += balance
        return self.balance


class SavingsAccount(Account):
    def __init__(self,id: int, balance: float, annualInterestRate: float, minimumBalance: float, penaltyFee: float):
        super().__init__(id, balance, annualInterestRate) # Use super() to call the parent class constructor. Basically, if you need to use some of the parent class's parameters, then you need to call super().__init__()
        self.minimumBalance = minimumBalance
        self.penaltyFee = penaltyFee
    def savings_account_info(self):
        print("ID:", self.id)
        print(f"Balance: ${self.balance}")
        print(f"Annual Interest Rate: {self.annualInterestRate}%")
        print(f"Minimum Balance: ${self.minimumBalance}")
        print(f"Penalty Fee: ${self.penaltyFee}")

    def savingAccount_withdrawal(self, balance: float):
        # Security checking to make sure the balance argument is a float or the integer value. Don't confuse with balance: float. This part is to indicate that this function should expect a float value. Integer or float is okay as long as it is a positive number 
        if not isinstance(balance, (int, float)):
            print("Invalid input: Please enter a number.")
            return

        print(f"Withdrawing ${balance}...")
        amount = self.balance - balance
        if amount > 0:
            if amount < self.minimumBalance:
                print(f"Your balance is below the minimum balance. A penalty fee of ${self.penaltyFee} has been applied.")
                self.balance -= self.penaltyFee # Applying penalty fee
                self.balance -= balance # Updating balance after penalty fee
                print(f"Your Current Balance is: ${self.balance}")
                
            else:
                self.balance -= balance # Updating balance if there is no penalty fee
                print(f"Your Current Balance is: ${self.balance}")
        else:
            print("Invalid Input. Please Input Only Positive Number, Numbers, or Insufficient Balance")

    def savingAccount_deposit(self, balance: float):
        # Security checking to make sure the balance argument is a float or the integer value. Don't confuse with balance: float. This part is to indicate that this function should expect a float value. Integer or float is okay as long as it is a positive number 
        if not isinstance(balance, (int, float)):
            print("Invalid input: Please enter a number.")
            return

        self.balance += balance
        print(f"Depositing ${balance}...")
        return self.balance # returning back the balance value to the caller function
        

print("\n===Main Account Details===")        
mainAccount = Account(1122, 20000, 3.5)
mainAccount.account_info()
# These two functions below should not run at the same time. In real life, you cannot withdraw and deposit at the same time. This is merely a showcase.
mainAccount.withdraw(2500)
#mainAccount.deposit(3000) 

print("\n===Main Account After Withdrawal and Deposit===")
mainAccount.account_info()

# ====
print("\n==============================\n")
# ====

print("===Saving Account Details===")   
savingAccount = SavingsAccount(1234, 5000, 4.5, 200, 15)
savingAccount.savings_account_info()
# These two functions below should not run at the same time. In real life, you cannot withdraw and deposit at the same time. This is merely a showcase.
savingAccount.savingAccount_deposit(3000)
#savingAccount.savingAccount_withdrawal(7850) 

print("\n===Saving Account After Withdrawal and Deposit===")
savingAccount.savings_account_info()


