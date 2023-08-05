from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass
    
class Donation(Employee):
    def donate(self):
        a= input("How much ypu like to donate: ")
        return  a
        
amount =[]
john = Donation()
j = john.donate()
amount.append(j)

peter = Donation()
p= peter.donate()
amount.append(p)

print("Total amount", amount)