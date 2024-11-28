pizza_prefs = [{'name': 'sandeep', 'toppings': 'mushrooms', 'pizza_type': 'round'},
               {'name': 'prize', 'toppings': ['ham', 'pineapple'], 'pizza_type': 'square'},
               {'name': 'john', 'toppings': ['bacon', 'pepperoni'], 'pizza_type': 'square'},
               {'name': 'doe', 'toppings': ['sausage', 'jalepenos'],'pizza_type': 'square'}]

print(pizza_prefs)

for person in pizza_prefs:
   
   mushrooms_found = False

   if type(person['toppings']) is str:
      if(person['toppings']) == "mushrooms":
         mushrooms_found = True
   elif type(person['toppings']) is list:
      if("mushrooms" in person['toppings']):
         mushrooms_found = True
   if mushrooms_found:
      pizza_prefs.remove(person)

print(pizza_prefs)