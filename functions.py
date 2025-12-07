# defining a function
def greet():
    print("Hello, World!")
greet()


def add(a, b):
    print(a + b)
add(2, 3)


def multiply(a, b):
    print(a * b)
multiply(4, 5)


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    print(a / b)
divide(10, 2)


def subtract(a, b):
    print(a - b)
subtract(5, 3)


def intro(name="Unknown", age='', city="Unknown"):
    print(f"My name is {name}, I'm {age} years old and I live in {city}.")
intro()
intro("Alice", 30, "New York")


def sum_power(a,b):
    return (a+b)**2
result = sum_power(2, 3)
print(result)


def add2(a,b):
    return a+b
print(add2(5, 7))


def calc(a, b):
    return a+b, a-b, a*b        # return multiple values
result = calc(5, 3)             
print(result)  


def sum_of_events(li):
    total = 0                    # initialize total to 0
    for i in li:                 # go through each number in the list
        if i % 2 == 0:           # check if the number is even
            total += i           # add the even number to the total
    return total                 # return the total sum of even numbers

print(sum_of_events([1, 2, 3, 4, 5]))    # Output: 6 (2 + 4 = 6)


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
print(divide(b=10, a=2))  # keyword arguments



# you can declare multiple things it becomes a tuple  ex: return 1,2,3,4,5,6  [output: (1, 2, 3, 4, 5, 6)]
# you can unpack the tuple ex: a,b,c,d,e,f = return 1,2,3,4,5,6
# you can also return a list or dictionary
# you can also pass a list or dictionary as an argument to a function

print(print.__doc__)  # to see the docstring of a function
# docstring is a string that describes the function, its parameters, and its return value
# it is a good practice to write docstrings for your functions

print(abs.__doc__)  # to see the docstring of a function


# args use to take multiple arguments
def sum_of_three(*nums):
    total = 0
    for i in nums:
        total += i
    return total
print(sum_of_three(1, 2, 3, 4, 5))
  

# kwargs use to take multiple keyword arguments
def build_in_profile(**things):
    print("Build in profile")
    for i,j in things.items():
        print(f"{i} : {j}")
build_in_profile(name="John", age=30, city="New York")

# you can use both args and kwargs in a function
def func(msg, *args, **kwargs):
    print("Message:",msg)
    print("Args:", args)
    print("Kwargs:", kwargs)
func("msg",1, 2, 3, name="John", age=30)


def add(x,y,z):
    return x+y+z
vals = (1,2,3)  # tuple
print(add(*vals))  # unpacking the tuple. # 1, 2, 3


parms = {'x':1, 'y':2, 'z':3}  # dictionary
print(add(**parms))  # unpacking the dictionary



# function scope

a = 1    # global scope
def func():
    a = 2  # local scope
    print(a) 
func()  # Output: 2
print(a)  # Output: 1



counter = 0
def increment():
    global counter # declare that we want to use the global variable
    counter += 1
    print(f"counter: {counter}")

increment()  # Output: counter: 1
increment()  # Output: counter: 2
increment()  # Output: counter: 3
print(f"counter: {counter}")  # Output: 3


# nonlocal keyword
def outer():
    x = 10
    
    def inner():
        nonlocal x  # refers to outer function's x
        x = 20      # modifies outer x
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()



# type conversion functions
print(int("10"))        # converts string to integer
print(float("10.5"))   # converts string to float
print(str(10))         # converts integer to string
print(list("hello"))   # converts string to list of characters
print(tuple([1, 2, 3]))# converts list to tuple
print(set([1, 2, 2, 3]))# converts list to set
print(dict(a=1, b=2))  # creates a dictionary
print(bool(1))         # converts integer to boolean
print(bool(0))         # converts integer to boolean
print(bool(""))        # converts empty string to boolean
print(bool("hello"))   # converts non-empty string to boolean

# math functions
print(abs(-10))        # returns absolute value
print(round(10.5))     # rounds to nearest integer
print(round(10.4))     # rounds to nearest integer
print(pow(2, 3))       # returns 2 raised to the power of
print(max(1, 2, 3))    # returns maximum value
print(min(1, 2, 3))    # returns minimum value
print(sum([1, 2, 3]))  # returns sum of all elements in

# sequence functions
print(len("hello"))    # returns length of string
print(len([1, 2, 3]))  # returns length of list
print(len((1, 2, 3)))  # returns length of tuple
print(len({1, 2, 3}))  # returns length of set
print(len({'a': 1, 'b': 2})) # returns length of dictionary

# enumerate function
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
# Output:
# 0 a
# 1 b
# 2 c   

# zip function
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = zip(a, b)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


# isinstance function
print(isinstance(10, int))        # Output: True
print(isinstance(10.5, float))    # Output: True
print(isinstance("hello", str))   # Output: True
print(isinstance([1, 2, 3], list))# Output: True
print(isinstance((1, 2, 3), tuple))# Output: True
print(isinstance({1, 2, 3}, set)) # Output: True
print(isinstance({'a': 1}, dict)) # Output: True
print(isinstance(10, (int, float))) # Output: True
print(isinstance(10.5, (int, float))) # Output: True
print(isinstance("hello", (int, float))) # Output: False

# map
# map(function, iterable)
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

words = ["hello", "world"]
result = map(str.upper, words)
print(list(result)) # Output: ['HELLO', 'WORLD']


# filter
# filter(function, iterable)
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4]


def long_word(word):
    return len(word) > 3
words = ["hi", "python", "map", "filter"]
result = filter(long_word, words)
print(list(result))  # Output: ['python', 'filter']


# reduce
from functools import reduce
# reduce(function, iterable)

def add(x, y):
    return x + y
nums = [1, 2, 3, 4]
result = reduce(add, nums)
print(result)  # Output: 10 (1+2+3+4=10)



def multiply(x, y):
    return x * y
nums = [1, 2, 3, 4]
result = reduce(multiply, nums)
print(result)  # Output: 24 (1*2*3*4=24)



# lambda function
'''
lambda arguments: expression
👉The expression is automatically returned.
👉 You don’t need return or a function name.
Single expression only (no statements allowed)
No name (anonymous function)
Can be assigned to a variable
Often used for short, simple operations
Return the result of the expression automatically 

'''

# def add(x, y):
#     return x + y
# print(add(5, 3))   # 8

add = lambda x, y: x + y
print(add(5, 3))   # 8

square = lambda x: x * x
print(square(4))   # 16

greet = lambda: "Hello"
print(greet())   # Hello


# lambda with map
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)   # [1, 4, 9, 16]

# lambda with filter
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6]

# lambda with reduce
from functools import reduce
nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, nums)
print(result)   # 24



# Function as First-Class objects
'''
👉 Functions can be treated like any other object in Python.
👉 They can be passed as arguments to other functions.
👉 They can be returned from other functions.
👉 They can be assigned to variables.

'''

