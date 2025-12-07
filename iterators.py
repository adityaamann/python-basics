# What is an Iteration ?
# Iteration is a general term for taking each item of something, one after another. 
# Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.

# Example
# num = [1,2,3]
# for i in num:
#     print(i)


# What is Iterator ?
# An Iterator is an object that allows the programmer to traverse through a sequence of data without having to store the entire data in the memory

# Example
# L = [x for x in range(1,10000)]

# for i in L:
#     print(i*2)
    
# import sys

# print(sys.getsizeof(L)/64)

# x = range(1,10000000000)

# for i in x:
#     print(i*2)
    
# print(sys.getsizeof(x)/64)


# What is Iterable ?
# Iterable is an object, which one can iterate over
# It generates an Iterator when passed to iter() method.

# Example
# L = [1,2,3]
# type(L)
# L is an iterable
# type(iter(L))
# iter(L) --> iterator


# Point to remember :

# Every Iterator is also and Iterable
# Not all Iterables are Iterators

# Trick :

# Every Iterable has an iter function
# Every Iterator has both iter function as well as a next function


# make your own for loop

# def apna_iterator(iterable):

#     iterator = iter(iterable)

#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break
    
# a = [1,2,3,4,5]
# b = (6,7,8,9)
# c = {10,11,12,13}
# d = range(20,30)

# apna_iterator(a)
# apna_iterator(b)
# apna_iterator(c)
# apna_iterator(d)


# range using generator

def My_range(start,end):

    for i in range(start,end):
        yield i

for i in My_range(1,10):
    print(i)


# generators -->
# saves memory,
# use in infinite series effieciently, 
# by logically connect we can in complex task (eg = fibonacci series)