# Question 1: Variable Assignment and String Manipulation
name = input("enter your name:")
age = input("enter your age:")

print (f"Hello {name}, you are {age} years old!")

# Question 2: Integer Operations 
length = int(input("enter the length of the rectangle:"))
width = int(input("enter the width of the rectangle:"))
area = length * width
print (f"The area of the rectangle is {area}")

# Question 3: Working with Floats
celsius = float(input("enter the temperature in celsius:"))
farenheit = (celsius * 9/5) + 32
print (f"{celsius} degrees Celsius is {round(farenheit, 2)} degrees Farenheit")
