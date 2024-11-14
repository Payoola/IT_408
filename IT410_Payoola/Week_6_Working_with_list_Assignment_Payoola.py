#Problem 1-5
college_courses = ["system analysis design", "network and operating systems", "server virtual and performance engine", "management", "business communications", "db design and developemnt", "principle of software engineering", "fundementals of cybersecurity"]

college_courses.sort()

for course in college_courses:
    print(f"I have taken {course.upper()} at college." )


upcoming_courses = ["advance programming", "security op and awareness"]

college_courses.extend(upcoming_courses)

college_courses.sort()

print("This is my course of study with upcoming courses added:")

for course in college_courses:
    print(course.upper())

removed_courses = []
for course in college_courses [:]:
    if course in college_courses:
        removed_courses.append(course)
        college_courses.remove(course)    

print("I do not have to take these courses:")
for course in removed_courses:
    print(course.upper())

print("\nRemaining courses to take:")
for course in college_courses:
    print(course.upper())

#Problem 6-11
divisible_by_6 = list(range(6, 1001, 6))

print("here are twenty number divisble by 6:")

for number in divisible_by_6[0:20]:
    print(number)

max_number = max(divisible_by_6)

print("the maximum number in the list of numbers divisble by 6 is:", max_number)


values_to_sum = divisible_by_6[9:50]

sum_of_value = sum(values_to_sum)

print("here is the sum of several values in the list:", sum_of_value)

college_courses = divisible_by_6

print(college_courses)
