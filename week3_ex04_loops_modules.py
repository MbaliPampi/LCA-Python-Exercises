import random
import math_operations

# Question 1: using a for loop with a list
fruits = ["kiwi", "mango", "watermelon", "strawberry", "apple"]
for fruit in fruits:
    print(fruit)

# Question 2: using a while loop for countdown
count = 5
while count >= 1:
    print(count)
    count -= 1

# Question 3: using a for loop with range
for i in range (1, 11):
  print(i * i)

# Question 4: using the random module 
colours = ["pink", "yellow", "blue", "white", "red"]
for i in range(3):
    print(random.choice(colours))

# Question 5: calculator
while true:
    print("\nsimle calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter choice (1-5): ")
    if choice == "5":
        print("Goodbye!")
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == "1":

print(math_operations.add(num1, num2))
  elif choice == "2":
print(math_operations.subtract(num1, num2))
  elif choice == "3":
print(math_operations.multiply(num1, num2))
  elif choice == "4":
print (math_operations.divide(num1, num2))
  else:
 print("Invalid choice")