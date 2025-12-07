class User:
    def login(self):
        print("Login")

    def register(self):
        print("Register")

#Inheritance
class Student(User):
    def enroll(self):
        print("Enrolled")

    def review(self):
        print("Review")

s1 = Student()
s1.enroll()
s1.login()
s1.register()
s1.review()


