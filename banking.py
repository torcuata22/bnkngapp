class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
        
    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin
        print("Your pin has been changed to: ", pin)

    def change_password(self, password):
        self.password = password
        print("Your new password is: ", password)
        
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        
    def show_balance(self):
        print (self.name, "has an account balance of ", self.balance)
    
        
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
            print("You have ", self.balance, "left")
        else:
            print("\n Insufficient balance  ")
    
    
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    
    
    
        
        
        
        
        
        
        
        
# Test code for User:
#user1 = User("Bob", "1234", "password")
#print(user1.name, user1.pin, user1.password)
#Test code for change_name, change_pin, change_password
#user1.change_name("Bobby")
#user1.change_pin("4321")
#user1.change_password("newpassword")
#print(user1.name, user1.pin, user1.password)

#Test code for BankUser:
#bankuser1 = BankUser("Bob", "1234", "password")
#print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)

#Test code for BankUser methods:
bankuser1 = BankUser("Mary", "4321", "mypassword")
print(bankuser1.show_balance())
print(bankuser1.deposit())
print(bankuser1.withdraw())