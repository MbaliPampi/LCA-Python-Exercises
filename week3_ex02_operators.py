x = 10
y = 5
x += 3
y *= 2
result = x / y
print(f"Q1 result: {result}")

a = 15
b = 10
c = 12
condition_a_gt_b = a > b
condition_b_even = b % 2 == 0
condition_c_le_a = c <= a
final_condition = condition_gt_b or (condition_b_even and condition_c_le_a)
print(f"Q2 result: {final_condition}")

score = int(input("enter test score (0-100): "))
if 90 <= score <= 100:
  grade = "A"
elif 80 <= score <= 89:
  grade = "B"
elif 70 <= score <=79:
  grade = "C"
elif 60 <= score <= 69:
  grade = "D"
else:
  grade: = "F"
print(f"Grade: {grade}")

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
operation = input("enter operation (+, -, *, /): ")

if operation == "+":
    print(f"result: {num1 + num2}")
elif operation == "-":
    print(f"result: {num1 - num2}")
elif operation == "/":
    if num2 == 0:
    print("error: cannot divide by zero")
else:
    print(f"result: {num1 / num2}")
else: 
    print("invalid operation")

