# File Handling
# mode 'r' - read (default)
# mode 'w' - write (creates a new file or truncates an existing file)
# mode 'a' - append (creates a new file or appends to an existing file)
# mode 'b' - binary (used with other modes for binary files)

# open file
file = open('example.txt','r')

# read a file
file = open('example.txt','r')
content = file.read() # reads the entire file
print(content)
file.close()

# read line by line
file = open('example.txt','r')
content = file.readline()
print(content)
file.close()

# read line in list
file = open('example.txt','r')
content = file.readlines()
print(content)
file.close()

 
# write to a file
file = open('example_2.txt','w')
file.write("Hello, World!\n")
file.write("This is a new file.\n")
file.close()

# append to a file
file = open('example_2.txt','a')
file.write("This line is appended.\n")
file.close()

# close a file

# using with statement to automatically close the file
with open('example_2.txt','r') as file:
    print(file.read())


# writelines
L = ["This is line1\n", "This is line2\n","This is line3\n"]
f = open('example_3.txt','w')
f.writelines(L)
f.close()

# print upto n char
with open('example_3.txt','r') as f:
    print(f.read(10))
    print(f.read(10))

# seek and tell function
with open('example_3.txt','r') as f:
    print(f.read(10))
    print(f.tell())
    f.seek(0)
    print(f.read(10))
    print(f.tell())

# seek during write
with open('sample.txt','w') as f:
  f.write('Hello')
  f.seek(0)
  f.write('Xa')

# working with binary file
with open('image.jpeg','rb') as f:
    with open('image_copy.jpeg','wb') as wf:
        wf.write(f.read())