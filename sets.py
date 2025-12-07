# unordered, unindexed, mutable, no duplicates, heterogeneous
# Set elements must be immutable (e.g., tuple, string, number); mutable types like list are not allowed.
# union, intersection, difference, symmetric difference
# fast membership testing
# add, remove, discard, pop, clear
# set(), {}
# frozenset()
# set comprehension
# union with other methods use only union() method

from turtle import update


numbers = {1, 2, 3, 4, 5}
strings = {"apple", "banana", "cherry"}
mixed = {1, "apple", 3.14, (1, 2)}
print(numbers)    # {1, 2, 3, 4, 5}
print(strings)
print(mixed)
print(type(numbers))
print(type(strings))
print(type(mixed))

# empty set
empty_set = set()
print(empty_set)
print(type(empty_set))
print(len(empty_set))     #0

num2 = {4, 5, 6, 7, 8, 4, 5, 6, 7, 8}
print(num2)

list_data =[1,2,3,4,5]
set_from_list = set(list_data)
print(set_from_list) 
print(type(set_from_list))
print(len(set_from_list))     #5

text = "hello world"
set_from_string = set(text)
print(set_from_string)      

s = set(range(1, 11))
print(s)     

# Set operations
my_set = {1, 2, 3}
my_set.add(4)    # adding an element
print(my_set)
my_set.remove(2) # raises KeyError if element not found
print(my_set)
my_set.discard(5)  # no error if element not found
print(my_set)
popped_element = my_set.pop()  # removes and returns an arbitrary element
print(popped_element)
print(my_set)
my_set.clear()  # removes all elements
print(my_set)

# using update to add multiple elements
my_set.update({5, 6, 7})
print(my_set)
my_set.update("abc")
print(my_set)
my_set.update([8, 9, 10], {11, 12}, (13, 14), "de", range(15, 18))
print(my_set)

# set operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("a:", a)
print("b:", b)
print("Union:", a | b)  # or a.union(b).      all elements from a and b
print("Intersection:", a & b)  # or a.intersection(b)       common elements of a and b
print("Difference (a - b):", a - b)  # or a.difference(b).            remove common elements of b from a
print("Difference (b - a):", b - a)  # or b.difference(a).            remove common elements of a from b
print("Symmetric Difference:", a ^ b)  # or a.symmetric_difference(b).     elements in a or b but not in both


# membership testing
print(3 in a)
print(10 in a)
print(10 not in a)


# subset, superset, disjoint
x = {1, 2, 3}
y = {1, 2, 3, 4, 5}
z = {6, 7, 8}
print(x.issubset(y))  # True     or <=.  or < for proper subset
print(y.issubset(x))  # False    or <=.  or < for proper subset
print(x.issuperset(y))  # False  or >=.  or > for proper superset
print(y.issuperset(x))  # True   or >=.  or > for proper superset
print(x.isdisjoint(z))  # True     checks if two sets have no elements in common
print(y.isdisjoint(z))  # True     checks if two sets have no elements in common

# Empty sey is subset and disjoint with any set but not a superset


# Copying a set
original_set = {1, 2, 3}
shallow_copy = original_set.copy()
original_set.add(4)
print(original_set)
print(shallow_copy)
print(original_set is shallow_copy)  # False, different objects

deep_copy = set(original_set)
print(deep_copy)
print(original_set is deep_copy)  # False, different objects


# Iteration
c = {1, 2, 3, 4, 5}
for item in c:
    print(item)


# frozenset - immutable version of set
# cannot add or remove elements
# can be used as dictionary keys or elements of another set
fs = frozenset([1, 2, 3, 4, 5])
print(fs)
print(type(fs))
# fs.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(2)  # AttributeError: 'frozenset' object has no attribute 'remove'
print(3 in fs)  # True
print(10 in fs) # False
print(len(fs))  # 5
print(fs.union({6, 7, 8}))
print(fs.intersection({3, 4, 5, 6}))
print(fs.difference({4, 5, 6}))
print(fs.symmetric_difference({5, 6, 7}))