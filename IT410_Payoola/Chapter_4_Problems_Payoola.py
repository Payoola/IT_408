#Problem 4-1
favorite_place = ["cedar point", "six flags", "the zoo", "henry ford"]

for place in favorite_place:
    print(place + " is a nice place to vist.")

#Problem 4-2
for number in range(90, 101):
    print(number)

#Problem 4-3
numbers = list(range(100000, 1000001)) 

total_sum = sum(numbers)

print("The sum of all the numbers is:", total_sum)

#Problem 4-4
import random
random_numbers = random.sample(range(1,50), 20)
print(random_numbers)

largest_number = max(random_numbers)
smallest_nmuber = min(random_numbers)

print("the largest number is:", largest_number)
print("the smallest number is:", smallest_nmuber)

#Problem 4-5
multiples_of_5 = list(range(0,101,5)) 

print(multiples_of_5)

#Problem 4-6
base_values = list(range(20,30))

print("base values:" , base_values)

doubled_values = [number * 2 for number in base_values]

print("doubled values:", doubled_values)

#Problem 4-7 
print("the first 2 values in the list:", random_numbers[:2])

print("the items 5-10 in the list:", random_numbers[4:10])

print("the last 4 items in the list:", random_numbers[-4])

#Problem 4-8
favorite_artist = ["Drake", "Kendrick Lamar", "Yeat"]

copied_artist = favorite_artist.copy()

favorite_artist.append("J Cole")

print("the original list of favorite artist:", favorite_artist)
print("copied list of favorite artist:", copied_artist)

#Problem 4-9
grades = ("1st", "2nd", "3rd", "4th", "5th")

grades[0] = "First"
print("Error:", e)
print("Grades tuple:", grades)