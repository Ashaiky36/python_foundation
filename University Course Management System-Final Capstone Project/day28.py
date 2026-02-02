#bank simualtor using OOPs concept
class Account:
    def __init__(self, acc_no, owner, balance):
        self.acc_no = acc_no
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.deposit = deposit
        self.balance += deposit
        print(f"Deposit Amount: {deposit}, Balance: {self.balance}")

    def withdraw(self, withdraw):
        self.withdraw = withdraw
        self.balance -= withdraw
        if self.balance >= 0:
            print(f"Account: {self.acc_no} owned by {self.owner} | Withdrawel Amount: {withdraw} | Balance: ${self.balance}" )
        else:
            self.balance -= 50
            print("Due to insuffient balance for withdrawel,an overdraft fee of $50 was charged")
            print(f"current balance after charging overdraft fee: {self.balance}")
            print("Amount would be subtracted during future deposits")
            

    def __str__(self):
        return f"Account: {self.acc_no} owned by {self.owner} | Balance: ${self.balance}"        
           
class SavingsAccount(Account):
    def __init__(self, acc_no, owner, balance, interest_rate):
        super().__init__(acc_no, owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self): 
        interest_rate = self.balance * (interest_rate/100)
        self.balance += interest_rate
    def __str__(self):
        return f"Account: {self.acc_no} owned by {self.owner} | Balance with added interest: ${self.balance}" 

class CheckingAccount(Account):
    def __init__(self, acc_no, owner, balance):
        super().__init__(acc_no, owner, balance)

    def __str__(self):
        return f"Account: {self.acc_no} owned by {self.owner} | Balance: ${self.balance}"       





t1 = SavingsAccount(112, "John Doe", 124)  
t1.add_interest(10)
print(t1)

