list_of_chores = ["Take out Trash", "Wash Dishes", "Cut Grass", "Dust Coffee Table"]

print("List of chores =", list_of_chores) 

for chore in list_of_chores[1:3]:
    chore = chore + " (10 minutes)"
    print(chore + " - Done!")

print("All the chore are not done!")