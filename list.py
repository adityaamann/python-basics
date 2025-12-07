# Lists in Python
# A list is an ordered collection of items which can be of different types.
# Lists are mutable, meaning you can change their content without changing their identity.
# Lists are defined using square brackets [].
# Example: Creating and manipulating lists

fruits = ["apple", "banana", "mango", 10]
print(fruits)         # ['apple', 'banana', 'mango', 10]
print(fruits[0])      # apple (indexing starts at 0)
fruits.append("kiwi") # adding new item
print(fruits)         # ['apple', 'banana', 'mango', 10, 'kiwi']

number = [1,2,3,4]
print(number[0])      # 1
print(number[-1])     # 4 (negative indexing starts at -1)
print(number[1:3])    # [2,3] (slicing)
print(number[:2])     # [1,2] (from start to index 2, exclusive)
print(number[2:])     # [3,4] (from index 2 to end)
print(number[:])      # [1,2,3,4] (copy of the whole list)

print(number.append(5))       # [1,2,3,4,5]
print(number.insert(1, 10))    # [1,10,2,3,4,5]
print(number.extend([6, 7]))  # [1,10,2,3,4,5,6,7]

print(number.pop())           # removes last item and returns it
print(number.remove(10))      # removes first occurrence of value 10
print(number.clear())        # removes all items    

# Updating list item
number = [1, 2, 3]
number[1] = 20      # [1,20,3]
print(number)

print(3 in number)    # True
print(number.index(3))# 2 (position of 3)
print(number.count(3))# how many times 3 appears

numbers = [3, 1, 4, 2]
print(numbers.sort())        # [1,2,3,4]
print(numbers.reverse())     # [4,3,2,1]


nums = [10, 20, 30, 40, 50]
print(nums[1:4])   # [20,30,40]
print(nums[:3])    # [10,20,30]
print(nums[::-1])  # [50,40,30,20,10] (reversed)
print(nums[::2])   # [10,30,50] (every second item)
print(nums[1::2])  # [20,40] (every second item starting from index 1)
print(nums[-3:-1]) # [30,40] (from index -3 to -1, exclusive)

empty_list = []
print(empty_list)  # []

nums = [5, 2, 8]
print(min(nums))  # 2
print(max(nums))  # 8
print(sum(nums))  # 15


veg = ["carrot", "broccoli", "spinach"]
del veg[1:3]    
print(veg)  # ['carrot']
print('carrot' in veg)  # True


# Shallow vs Deep Copy
a = [1, 2, 3]
b = a          # b references the same list as a (shallow copy)
b.append(4)
print(a)      # [1,2,3,4]
print(b)      # [1,2,3,4]

c = [5,6,7]
d = c[:]  # d is a new list with the same content as c (deep copy)
d.append(8)
print(c)  # [5,6,7]
print(d)  # [5,6,7,8]

a = [[1, 2], [3, 4]]
print(a[1])    # [3,4]
print(a[1][0]) # 3
b = a[:]       # shallow copy of a
b[0][0] = 10
print(a)  # [[10,2],[3,4]] (inner list modified)
print(b)  # [[10,2],[3,4]]


a = [1,2,3]
b = [4,5]
result = a + b  # concatenation 
print(result)    # [1,2,3,4,5]
print(a * 2)    # [1,2,3,1,2,3] (repetition)


a = [1,2,3]
a.sort(reverse=True)
print(a)  # [3,2,1]
print(a.count(2))  # 1
print(a.index(3))  # 0

fruits = ["apple", "banana", "cherry", "apple", "apple"]
count_apple = fruits.count("apple")
print(count_apple)  # 3
for i in range(len(fruits)):
    print(fruits[i])


nums = [4,24,5,3,1,21]
min_num = nums[0]
for i in nums:
    if min_num > i:
        min_num = i
print(min_num)  # 1


a = [1,2,3]
b = [1,2,3]

print(a is b)       # False (different objects)
print(a == b)       # True (same content)


# List Comprehensions
li = [1,2,3,4,5,6,7]
squares = [x**2 for x in li]
print(squares)  

res = [x**2 for x in li if x%2==0]
print(res)  # [4,16,36]

