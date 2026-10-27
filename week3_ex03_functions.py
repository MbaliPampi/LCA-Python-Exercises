def greet():
    print("Hello, World!")
    greet()

def personalized_greeting(name) :
    print(f"Hello, {name}!")
    personalized_greeting("Mbali Pampi")

def square (number):
    return number*number
    print(square(5))

def rectangle_area(length, width):
    return length * width
    print (rectangle_area(4, 6))

def apply_operation(func, number):
    return func(number)
    print (apply_operation(square, 5))
