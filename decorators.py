def my_decorators(func):
    def wrapper():
        print("World before Hello World")
        func()
        print("World after Hello World")
    return wrapper


@my_decorators
def greet():
    print("Hello World")

greet()
