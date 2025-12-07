# '''
# x = 0
# while condition:
#     # code block to be executed
# '''

# x = 0
# while x <= 5:
#     print("Hello World")
#     x += 1
#     if x == 3:
#         break

# '''
# for variable in sequence:
#     # code block to be executed
# '''

# for i in range(5):            # Looping from 0 to 4
#     print(i)
    

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# for x in "banana":
#     print(x)


# name = "John"
# for x in name:             # Looping through each character in the name
#     print(x.upper())


# for i in range(2,5):      # Looping from 2 to 4
#     print(i)


# for i in range(2, 10, 2):      # Looping from 2 to 9 with step of 2
#     print(i)


# fruits = ["apple", "banana", "cherry", "mango"]
# for i in range(len(fruits)):
#     print(fruits[i])

# print(list(enumerate(fruits)))  

# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}: {fruit}")



# for number in range(10):               
#     if number  == 5:
#         continue
#     print(number)


# for number in range(10):              
#     if number  == 5:
#         break
#     print(number)


# for number in range(10):
#     if number  == 5:
#         pass
#     print(number)


# for i in range(11):
#     if i % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")


num = int(input("Enter your number: "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

orders = ["Aman", "Aadi", "John", "Nikki"]
for i in orders:
    print(f"order ready for: {i}")

menu = ["Lassi", "Mithai", "Biscuits", "Paratha"]
for idx, items in enumerate(menu, start=1):
    print(f"{idx} : {items}")
    
    
num_tasks = ["Project", "Assignment", "H.W.", "C.W."]
for idx,items in enumerate(num_tasks , start=1):
    print(f"{idx} : {items}")
    
    
names = ["Aditya", "Rohan", "Samaira", "Kanchan"]
bills = [100,200,310,1055,1021]
for names,amount in zip (names,bills):
    print(f"{names} paid {amount} rupees")

