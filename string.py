str1 = "Afhbvsvhs 98#$gdfhbv ggd"
print(str1)
print(str1[0])
print(str1[5])

city = "New York"
temp = 32
w_r = f"The weather in {city} is {temp} degree celsius"
print(w_r)

a = 5
b = 10
print(f"The sum of {a} and {b} is {a+b}")


name = "John"
print(f"First character of {name} is {name[0]}") 


star = "*"
print((star * 5 + "\n") * 5)

txt = "Python"
print(txt[len(txt)-1])      #n
print(txt[::-1])   #reversed string
print(txt[:6])  
print(txt[0:])  
print(txt[:])

# txt([start:end:step])
# start -> inclusive
# end -> exclusive

print(txt.upper())
print(txt.lower())
print(txt.title())
print(txt.capitalize())

txt2 = "   hi   "
print(txt2.strip())
print(txt2.lstrip())
print(txt2.rstrip())
print(txt2.find("i"))

txt3 = "Python is fucked Python is worst"
print(txt3.count("Python"))

# .index is same as .find but if it doesn't found it returns error
print(txt3.find("Java"))
#print(txt3.index("Java"))

# case sensitive
txt4 = "Python is fun"
print(txt4.replace("Python","World"))

txt5 = "Python is english"
print(txt.startswith("Python"))
print(txt.endswith("english"))

# .split()
print(txt5.split(" "))

# .format()
message = "Hello, My name is {} and my age is {} ".format("John",25)
print(message)

print(id(message))


      
      


