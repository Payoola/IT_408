#Problem 5-1
#example
color = "blue"
print(color == "blue")

#This expression should be true
age = 24
print(age >= 18) 

#This expression should be false
name = "Prize"
print(name == "Jeff")

#This expression should be True
numbers = [5, 2, 3, 8, 9]
print(9 in numbers)

height = "6 foot"
print(height == "5,11 foot")

#This expression should be true
temperature = 50
print(temperature > 20)

#This expression should be false
score = 100
print(score == 95)

#Problems 5-2,3
number = 7
another_number = 8

if number % 2 != 0:
    print(f"the number {number} is odd.")
else:
    number += 1
    print(f"the number is even. But after adding one it is: {number}")    
if another_number %2 != 0:
    print(f"the other number {another_number} is odd.")
else:
    another_number += 1
    print(f"the other number is even. But after adding one it is: {another_number}")


#Problem 5-4
favorite_fruits = ["grapes", "blueberries", "strawberries", "bananas"]

if len(favorite_fruits) == 2:
    print("I like two fruits.")
elif len(favorite_fruits) == 3:
    print("I like three fruits.")
elif len(favorite_fruits) == 4:
    print("I like four fruits.")
elif len(favorite_fruits) >= 5:
    print("I like several fruits.")

#Problem 5-5
numbers_list = list(range(1, 56))

number1 = 25
number2 = 62

if number1 in numbers_list:
    print(f"the number {number1} was found in the list.")
else:
    print(f"the number {number1} was not found in the list.")

if number2 in numbers_list:
    print(f"the number {number2} was found in the list.")
else:
    print(f"the number {number2} was not found in the list.")


#Problem 5-6
favorite_stores = ["Meijers", "Best buy", "Walmart", "Kohl's", "Home depot"]

stores_with_sales = ["Best buy", "Kohl's", "Target", "Macy's"] 

for stores in favorite_stores:
    if stores in stores_with_sales:
       print(f"Take advantage of the sale at your favorite store: {stores}!")
    else:
        print(f"{stores} isn't currently running a sale.")