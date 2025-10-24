class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getID(self):
        return self.__id

    def setID(self, id):
        self.__id = id

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12

    def getMonthlyInterest(self):
        return self.__balance * (self.getMonthlyInterestRate() / 100)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Transaction failed. Amount withdrawal larger than current balance!")

    def deposit(self, amount):
        self.__balance += amount


class SavingAccount(Account):
    def __init__(self, id=0, balance=100, annualInterestRate=0, minimumBalance=100, penaltyFee=10):
        super().__init__(id, balance, annualInterestRate)
        self.__minimumBalance = minimumBalance
        self.__penaltyFee = penaltyFee

    def withdraw(self, amount):
        # Perform withdrawal
        new_balance = self.getBalance() - amount
        self.setBalance(new_balance)

        # After withdrawal, check if balance falls below minimum
        if self.getBalance() < self.__minimumBalance:
            # Apply penalty fee
            self.setBalance(self.getBalance() - self.__penaltyFee)


# === Test Cases ===

# Case 1 - from the test case sample
myAcct1 = Account(1122, 20000, 3.5)
myAcct1.withdraw(2500)
myAcct1.deposit(3000)
print("Account information: ")
print(f"id: {myAcct1.getID()}, balance: {myAcct1.getBalance()}")
print(f"monthly interest rate: {myAcct1.getMonthlyInterestRate():.2f}, monthly interest: {myAcct1.getMonthlyInterest():.2f}")
print("---")

# Case 2 - withdraw > balance
myAcct2 = Account(balance=500)
myAcct2.withdraw(1000)
print(f"id: {myAcct2.getID()}, balance: {myAcct2.getBalance()}")
print("---")

# Case 3
myAcct3 = Account()
print(f"id: {myAcct3.getID()}, balance: {myAcct3.getBalance()}")
myAcct3.deposit(500)
print(f"id: {myAcct3.getID()}, balance: {myAcct3.getBalance()}")
print("---")

# Saving Account
mySavingAcct = SavingAccount(1234, 300, 4.5, 200, 15)
mySavingAcct.withdraw(200)
print(mySavingAcct.getBalance())