# def greet():
#     yield "Hi"
#     yield "How are you?"
#     yield "Bye"
# greet = greet()
# print(next(greet))
# print(next(greet))
# print(next(greet))
# for msg in greet():
#     print(msg)



# def numbers():
#     for i in range(1,10):
#         yield i

# def squares(nums):
#     for n in nums:
#         yield n * n

# def even(nums):
#     for n in nums:
#         if n % 2 == 0:
#             yield n

# result = even(squares(numbers()))
# for r in result:
#     print(r)


# infinite generators

# def infinite_numbers():
#     i = 0
#     while True:     # runs forever
#         yield i
#         i += 1
# for n in infinite_numbers():
#     print(n)


# send values to a generator
def chat():
    name = yield "Hi, what's your name?"   # yields first message
    yield f"Nice to meet you, {name}!"     # uses the value sent in

gen = chat()
print(next(gen))           # starts generator -> prints: Hi, what's your name?
print(gen.send("Aditya"))  # sends "Aditya" into the generator


def adder():
    total = 0
    while True:
        x = yield total    # waits for a value to be sent
        total += x
gen = adder()
print(next(gen))      # start -> 0
print(gen.send(10))   # total = 10
print(gen.send(5))    # total = 15
print(gen.send(20))   # total = 35


# yield from
def numbers():
    yield 1
    yield 2
    yield 3

def double_numbers():
    yield from numbers()   # take all values from numbers()
    yield 100              # add your own if you want

for n in double_numbers():
    print(n)
