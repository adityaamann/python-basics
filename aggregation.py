class Customer:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

class Address:
    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state

add = Address("Jaipur",300307,"Rajasthan")
cust_1 = Customer("Ankit",24,add)

print(cust_1.name)
print(cust_1.age)
print(cust_1.address.city)
print(cust_1.address.pincode)
print(cust_1.address.state)