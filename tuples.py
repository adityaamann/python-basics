# tuple is an ordered, immutable collection of items.
# Tuples are defined by enclosing the items in parentheses () and separating them with commas.
# Tuples can contain items of different data types, including numbers, strings, and even other tuples.

# Creating a tuple
my_tuple = (1, 2, 3, "hello", (4, 5))
print(my_tuple)  # Output: (1, 2, 3, 'hello', (4, 5))
a = (1,) # single element tuple
print(a)
b = (1) # not a tuple

tuple_from_string = tuple("hello")
print(tuple_from_string)  # Output: ('h', 'e', 'l', 'l', 'o')

tuple_from_list = tuple([1, 2, 3])
print(tuple_from_list)  # Output: (1, 2, 3)

empty_tuple = ()
print(empty_tuple)  # Output: ()

d = 1, # tuple packing
print(type(d))  # Output: <class 'tuple'>
print(d)  # Output: (1,)

tuple() # empty tuple

# immutiability applies to the tuple structure itself, not to the objects contained within it.
t = (1,[2,3])
t[1].append(4)
print(t) # (1, [2, 3, 4])

# Immutable tuples can be used as keys in dictionaries or as elements of sets, while lists cannot.

original_tuple = (1, 2, 3)
new_tuple = original_tuple + (4, 5)
print(new_tuple)  # Output: (1, 2, 3, 4, 5)

# Unpacking tupels

point = (10, 20)
x, y = point
print(x)  # 10
print(y)  # 20

a, b, c = (1, 2, 3)
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

a,*b = (1, 2, 3, 4, 5)
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4, 5]


person = ("Aditya", 20, "Engineer")
name, age, job = person
print(name)  # Aditya
print(age)   # 20
print(job)   # Engineer


data = ("Aditya", (20, "Engineer"))
name, (age, job) = data
print(name)  # Aditya
print(age)   # 20
print(job)   # Engineer


a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5


person = ("Aditya", 20, "Engineer")
name, _, job = person
print(name, job)  # Aditya Engineer


# Iterating through a tuple

t = (10, 20, 30, 40)
for item in t:
    print(item)

t = (10, 20, 30)
for i in range(len(t)):
    print("Index:", i, "Value:", t[i])


t = ("apple", "banana", "mango")
for index, value in enumerate(t):
    print(index, value)


t = ((1,2), (3,4), (5,6))
for x, y in t:   # tuple unpacking
    print(x, y)


# concatenation and repetition

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)   # (1, 2, 3, 4, 5, 6)

t = (10, 20)
t2 = t * 3
print(t2)   # (10, 20, 10, 20, 10, 20)


# methods in tuples
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))   # 3  (because 2 appears 3 times)

t = (10, 20, 30, 20)
print(t.index(20))   # 1  (first time 20 appears at index 1)

t = (5, 1, 8, 3)
print(len(t))   # 4
print(max(t))   # 8
print(min(t))   # 1
print(sum(t))   # 17


