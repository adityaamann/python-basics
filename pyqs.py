
# wds = ["red", "blue", "green"]
# glue = ";"
# s= glue.join(wds)
# print(s)
# print(wds)
# print("***". join(wds))
# print("". join(wds))

# from functions import func


# def decorl(func):
#     def inner():
#         x = func()
#         return x**0.5
#     return inner

# def decor(func):
#     def inner():
#         x = func()
#         return 3*x
#     return inner

# @decorl
# @decor
# def num():
#     return 27
# print(num())

# @decor
# @decorl 
# def num2():
#     return 100
# print(num2())

# class Product:
#     total_products = 0   # class variable

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         Product.total_products += 1

#     @staticmethod
#     def get_total_products():
#         return Product.total_products


# # Create products
# product1 = Product("Laptop", 1500)
# product2 = Product("Smartphone", 800)

# # Print total products
# print(f"Total products: {Product.get_total_products()}")

# # Print each product details
# print(f"Product 1: {product1.name}, Price: ${product1.price}")
# print(f"Product 2: {product2.name}, Price: ${product2.price}")


# class BankAccount:
#     total_accounts = 0   # class variable (shared by all accounts)

#     def __init__(self, owner):   # constructor
#         self.owner = owner
#         BankAccount.total_accounts += 1   # increase count when new account is made

#     def get_owner(self):   # instance method
#         return self.owner

#     def account_count(self):   # instance method
#         return BankAccount.total_accounts


# # create two accounts
# account1 = BankAccount("Alice")
# account2 = BankAccount("Bob")

# # print details
# print(account1.get_owner())         # "Alice"
# print(account1.account_count())     # 2
# print(BankAccount.total_accounts)   # 2


def summarize_arguments(*args, **kwargs):

    print("No of positional arguments: ", len(args))
    print("Positional arguments: ", args)

    print("No of keyword arguments: ", len(kwargs))
    print("Keyword arguments: ", kwargs)


    summarize_arguments(10, 20, 30, name="Alice", age=25)
