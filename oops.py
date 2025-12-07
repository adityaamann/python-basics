# class - blueprint or template
# __init_ - constructor, initializes the object
# self - refrence or connection build between class and object
class Students: 
    def __init__ (self, name, age, grade, team):    # method
        self.name = name      # attribute
        self.age = age        # attribute
        self.grade = grade    # attribute
        self.team = team      # attribute


    def student_info(self):
        print(f"{self.name} is {self.age} years old and in grade {self.grade}.")


team1 = 1
team2 = 2

# object - instance of a class
s1 = Students("John", 20, "A", team1)   # object
s1.student_info()

s2 = Students("Jane", 22, "B", team2)   # object
s2.student_info()


print(s1.__dict__)   # to see the attributes of the object
print(s2.__dict__)   # to see the attributes of the object


# modify object propertie
s1.age = 21
s1.grade = "A+"
s1.student_info()

# delete object properties
del s2.grade
print(s2.__dict__)   # to see the attributes of the object after deletion

# del object
del s2
# print(s2)   # this will raise an error because s2 is deleted



# 4 features of OOP
# 1. Encapsulation - binding data and methods that manipulate the data within one unit
# 2. Abstraction - hiding the complex implementation details and showing only the necessary parts
# 3. Inheritance - a mechanism where a new class inherits properties and behavior (methods) from another class
# 4. Polymorphism - the ability to present the same interface for different data types


# Abstraction

