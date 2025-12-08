rent = int(input("Enter the monthly rent amount: "))
food = int(input("Enter the monthly food expenses: "))
electricity = int(input("Enter the monthly electricity bill: "))
water = int(input("Enter the monthly water bill: "))
internet = int(input("Enter the monthly internet bill: "))
person = int(input("Enter the number of person living in room/flat: "))

total_expenses = (rent + food + electricity + water + internet) // person
print("Total monthly expenses per person: ", total_expenses)




