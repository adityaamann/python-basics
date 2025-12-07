print("Hello")

x = 'John'
y = 4
z = True
a = 40.5


print(x)
print(y)
print(z)
print(a)
print(x, ',', y, ',', z, ',', a)

print(type(x))
print(type(y))
print(type(z))
print(type(a))


student_name = input("Enter your name: ")
student_marks1 = int(input("Enter Maths marks: "))
student_marks2 = int(input("Enter Science marks: "))
student_marks3 = int(input("Enter English marks: "))

percentage = ((student_marks1 + student_marks2 + student_marks3)/300)*100

print(f"Hello {student_name} Your percentage is {percentage}%")

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")

    