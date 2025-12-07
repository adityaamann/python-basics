age = int(input("Enter your age: "))
if age >=18:
    print("You are an adult.")
print("You are not an adult.") 



is_rain = input("Is it raining? (True/False): ").strip().lower()
if is_rain == "true":
    print("It is raining.")
else:
    print("It is not raining.")



age = int(input("Enter your age: "))
if age >= 18:
    password = input("Enter your password: ")       
    if len(password) >= 8:
        print("Strong password.")
    else:
        print("Weak password.")

print("You are not eligible to set a password.")



x = int(input("Enter a number: "))
if x % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")


score =  86
if score >= 90:
    grade = 'A'

elif score >= 80:
    grade = 'B'

elif score >= 70:
    grade = 'C'

elif score >= 60:
    grade = 'D' 

else:
    grade = 'F'

print(f"Your grade is {grade}")



number = int(input("Enter a number: "))
if number <= 0 :
    print("Negative or zero")

elif number >= 1 and number <= 9:
    print("Positive single digit")

elif number >= 9:
    print("Positive double digit or more")

else:
    print("Invalid input")


has_fever = True
has_cough = True
has_rash = False

if has_fever :
    if has_cough:
        print("You may have the flu.")
    elif has_rash:
        print("You may have measles.")
    else:
        print("You may have a common cold.")
else:
    print("You seem to be healthy.")



a = int(input("Enter a number between 1 and 10: "))
if a == 6 or a == 7 or a == 9:
    print("Lucky")
else:
    print("Unlucky")


# Ternary Operator -->

age = 18
status = "adult" if age >= 18 else "minor"
print(status)


number  = 17
divisor = 7
result = number / divisor if divisor != 0 else "Undefined (division by zero)"
print(result)


