# A dictionary in Python is like a real dictionary: it stores key–value pairs.
# Keys = unique identifiers
# Values = data associated with keys
# Written with {}

student = {
    "name" : "John",
    "age" : 25,
    "courses" : ["Math", "CompSci"]
}

print(student)                 # {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student["name"])        # John
print(student.get("age"))     # 25
print(student.get("phone" , "Not Found"))   # Not Found

student["marks"] = 90        # add new key-value
student["age"] = 21          # update existing value
print(student)                # {'name': 'John', 'age': 21, 'courses': ['Math', 'CompSci'], 'marks': 90}

student.pop("marks")         # remove by key
student.popitem()            # remove last inserted key-value
del student["age"]           # delete by key
student.clear()              # remove everything
print(student)               # {}


student = {"name": "Aditya", "age": 20}
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)


students = {
    "101": {"name": "Aditya", "age": 20},
    "102": {"name": "Riya", "age": 21}
}
print(students["101"]["name"])  # Aditya


dict(apple = "red", banana = "yellow" , cherry = "red")  # {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
d = dict([("apple", "red"), ("banana", "yellow"), ("cherry", "red")])  
print(d)  # {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}



students = {"Ram" : 90, "Shyam" : 85, "Mohan" : 92}
key = input("Enter name: ")
print(students.get(key.title(), "Not Found"))


profile = {'name': 'Alice', 'age': 30, 'city': 'New York'}
new_profile = {'age': 31, 'city': 'San Francisco', 'email': 'sF3o6@example.com'}
profile.update(new_profile)
print(profile)  # {'name': 'Alice', 'age': 31, 'city': 'San Francisco', 'email': 'sF3o6@example.com'}


profile = {'name': 'Alice', 'age': 30, 'city': 'New York'}
profile.update([('age', 31), ('city', 'San Francisco')])
print(profile)  # {'name': 'Alice', 'age': 31, 'city': 'San Francisco'}


# Dict operations
stdnt = {"name": "Aditya", "age": 20}
print('name' in stdnt)  # True
print(len(stdnt))       # 2
print(stdnt.keys())     # dict_keys(['name', 'age'])
print(stdnt.values())   # dict_values(['Aditya', 20])
print(stdnt.items())    # dict_items([('name', 'Aditya'), ('age', 20)])

for j in stdnt:
    print(j, stdnt[j])


data = {
    'id' : 101,
    'info' : {
        'name' : 'Aditya',
        'age' : 20,
        'courses' : ['Math', 'CompSci']
    }
}
print(data['info']['courses'][0])  # Math
print(data.get('info').get('age'))  # 20


#Merge Python3.9+
a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
c = a | b
print(c)  # {'x': 1, 'y': 3, 'z': 4}


# Dict comprehension

# {key: value for item in iterable if condition}
squares = {x: x*x for x in range(6)}
print(squares)  
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)
# {1: 'a', 2: 'b', 3: 'c'}

words = ["apple", "banana", "cherry"]
lengths = {word: len(word) for word in words}
print(lengths)
# {'apple': 5, 'banana': 6, 'cherry': 6}

# create multiplication table
res = {i:{ j:i*j for j in range(1,11)} for i in range(1,6)}
print(res)


