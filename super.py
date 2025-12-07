class Phone:
    def __init__(self,price,model,brand):
        print("Parent Constructor")
        self.price = price
        self.model = model
        self.brand = brand
    
    def buy(self):
        print("Parent Buy")

class Smartphone(Phone):
    def __init__(self,price,model,brand,ram,os):
        print("Pahle Yahan")
        super().__init__(price,model,brand)   # Calling parent class constructor
        self.ram = ram
        self.os = os
        print("Child Constructor")

    def buy(self):
        print("Child Buy")
        super().buy()       # Calling parent class method


s = Smartphone(80000,15,"Apple","4GB","iOS")
s.buy()

print(s.os)
print(s.brand)


