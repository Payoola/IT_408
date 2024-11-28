#Problem 7-1
favorite_resurant = input("what is your favorite resturant? ")

print("let me help you find the closest", favorite_resurant + ".")


#Problem 7-2
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

result = num1* num2

print("the result of multiplying", num1, "and" , num2, "is:", result)


#Problem 7-3
dinner_item = []

while True:
    item = input("what are you having for dinner? (type 'done' to finish) ")
    if item.lower() == 'done':
        break
    dinner_item.append(item)
print("you are having the following items for dinner:")
for food in dinner_item:
    print("-", food)

#Problem 7-4
while True:
    ride = input("which ride would you like to go on? (type 'exit' to leave) ")
    if ride.lower() == 'exit':
        break
    if ride.lower() == 'ferris wheel':
        print("that will be $2.00.")
    elif ride.lower() == 'tilt-a-twirl':
        print("that will be $3.00.")
    elif ride.lower() == 'pirate ship':
        print("that will be $3.50.")
    else:
        print("sorry, that ride was not found.")

#Problem 7-5
grocery_list = ['milk', 'eggs', 'bread', 'apples', 'milk', 'chicken breast' , 'cereal']

item_to_remove = 'milk'

print("original grocery list:", grocery_list)

while item_to_remove in grocery_list:
    grocery_list.remove(item_to_remove)
print("updated grocery lsit:", grocery_list)




