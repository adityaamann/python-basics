# Length of a string without using len() function ->

# s = input("Enter a string: ")
# count = 0
# for i in s:
#     count += 1
# print("Length of the string is:", count)


# Extract username from email ->

# email = input("Enter your email: ")
# pos = email.index('@')
# print(email[0:pos])

# Count frequency of a particular char ->

# s = input("Enter your string: ")
# term = input("What would you like to search: ")
# count = 0
# for i in s:
#     if i==term:
#         count += 1
# print(f"{term} has occurred {count} times in the string.")


# Remove particular char from string ->

# s = input("Enter your string: ")
# term = input("What would you like to search: ")
# result = ''
# for i in s:
#     if i != term:
#         result += i
# print("String after removal:", result)


# Check whether a string is palindrome or not ->

# s = input("Enter your string: ").lower()
# flag = True
# for i in range(0,len(s)//2):
#     if s[i] != s[len(s)-i-1]:
#         flag = False
#         print("Not a Palindrome")
#         break

#     if flag:
#         print("Palindrome")


# Convert integer to string ->

# number = int(input("enter your number: "))

# digits = '0123456789'
# result = ''
# while number != 0:
#    result = digits[number % 10] + result
#    number = number//10

# print(result)
# print(type(result))





