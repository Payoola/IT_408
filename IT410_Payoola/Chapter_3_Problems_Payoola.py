#Problem 3-1
last_books = ["harry potter", "animal farm", "the twilight", "lord of the rings"]

print("I just read: " + last_books[0].title())
print("I just read: " + last_books[1].title())
print("I just read: " + last_books[2].title())
print("I just read: " + last_books[3].title())

#Problem 3-2
favorite_shows = ["suits", "house of cards", "stranger things", "2 and half men"]
favorite_shows[3] = "the witcher"

favorite_shows.append("family guy")
favorite_shows.insert(2, "Breaking bad")

favorite_shows.pop()
del favorite_shows[0:3]

print(favorite_shows)

#Problem 3-3
favorite_candybars = ["Snickers", "Hersheys", "Kit Kat", "Twix", "Reese's"]

print("Number of candy bars in the list:" , len(favorite_candybars))

favorite_candybars.sort()
print("Favorite candy bars in alphabetical order:", favorite_candybars)

sorted_candybars = sorted(favorite_candybars, reverse=True)
print("Favorite candy bars in reverse order:", sorted_candybars)                 

sorted_candybars.reverse()
print("sorted candybars reversed:", sorted_candybars)

#Problem 3-4
muscle_cars = ["Challenger", "Camaro", "Mustang"]
#select last muscle car on the list
print(muscle_cars[3]) #this is the answer with the error

#print(muscle_cars[2]) #the correct code will generate the last car as mustang
