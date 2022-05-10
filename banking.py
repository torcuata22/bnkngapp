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
        
        
        
        
        
        
        
        
        
# Test code for User:
#user1 = User("Bob", "1234", "password")
#print(user1.name, user1.pin, user1.password)
#Test code for change_name, change_pin, change_password
#user1.change_name("Bobby")
#user1.change_pin("4321")
#user1.change_password("newpassword")
#print(user1.name, user1.pin, user1.password)