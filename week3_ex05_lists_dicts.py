# Question 1: creating and modifying lists
fruits = ["apple", "strawberry", "blueberry"]
fruits.append("mango")
fruits.insert(0, "apple")
fruits.remove("strawberry")
print("Q1 - modified fruits list:", fruits)

# Question 2: list operations
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
total = sum(numbers)
average = total / len(numbers)
print("\nQ2 - original numbers:", numbers)
print("Q2 - squared numbers", squared_numbers)
print("Q2 - sum:", total)
print("Q2 - Average:", average)

# Question 3: creating and modifying dictionaries
countries_capitals = {"South Africa": "Pretoria",
                     "France": "Paris",
                     "Japan": "Tokyo"}
countries_capitals["Brazil"] = "Brasilia"
countries_capitals["South Africa"] = "Cape Town"
print("\nQ3 - countries and capitals:", countries_capitals)
for country, capital in countries_capitals.items():
  print(f"{country} -> {capital}")