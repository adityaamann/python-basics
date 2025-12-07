a = True
b = False
print(type(a), type(b))
print(a and b) 
print(a or b)
print(not a)
print(not b)

age = 17
is_adult = age>=18
print(is_adult)

print(True == 1)
print(False == 0)

print(int(True))
print(int(False))

# truthy or falsy
print(bool(1))   # truthy
print(bool(0))   # falsy
print(bool(-5))  # truthy
print(bool(0.1)) # truthy
print(bool(0.0)) # falsy
print(bool("Hello")) # truthy
print(bool(""))  # falsy
print(bool([]))  # falsy
print(bool([1, 2, 3]))  # truthy
print(bool({}))  # falsy
print(bool({"a": 1}))  # truthy
print(bool(None))  # falsy


print(True.bit_length())  # 1
print(False.bit_length()) # 0





