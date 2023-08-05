class MyClass:
    a = 5
    
    def hello(self):
       print("Hello! my first class") 

myclass = MyClass()
print (myclass.a)
print(myclass.hello())

class Receipe():
    
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
        
    def contents(self):
        print("The "+ self.dish + " has "+ str(self.items) + \
            " and takes " + str(self.time) + " to prepare "
            )
        
pizza  = Receipe("Pizza" , ["bread", "cheese", "tomato"], 45)
pasta  = Receipe("Pizza" , ["penne", "sauce", "chicken", "salt"], 30)

print(pizza.contents())
print(pasta.contents())

class Payslip:
    def __init__(self, name, payment, amount ) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
    def pay(self):
        self.payment = "yes"
        
    def status(self):
        if( self.payment == "yes"):
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"
        
nathan = Payslip("Nathan", "no", 1000)
rodger = Payslip("rodger", "no", 1000)

print(nathan.status())

print(rodger.status())
nathan.pay()
print("After payment...")
print(nathan.status())