import os

def create_file(filename):
    try:
        with open(filename , 'x') as f:
            print(f"File created{filename}successfully")

    except FileExistsError:
        print("File already exists")

    except Exception as e:
        print("An error occured")


def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found")
    else:
        print("File Found")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename} deleted successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:          
        print("An error occurred")  

def write_to_file(filename, content):
    try:
        with open(filename, 'a') as f:
            f.write(content + '\n')
            print(f"Content written to {filename} successfully")
    except Exception as e:
        print("An error occurred")      


def main():
    while True:
        print("\nFile Management System")
        print("1. Create File")
        print("2. View All Files")
        print("3. Delete File")
        print("4. Read File")
        print("5. Write to File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter filename to create: ")
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter filename to delete: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter filename to read: ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter filename to write to: ")
            content = input("Enter content to write: ")
            write_to_file(filename, content)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")