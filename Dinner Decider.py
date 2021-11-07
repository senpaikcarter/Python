import random

mylist = ['Stir Fry',
'Breakfast',
'Enchiladas',
'Sausage and Potatos ',
'Tacos',
'Burgers and fries',
'Pulled Pork',
'BBQ Chicken',
'Spaghetti',
'Curry',
'Jambalaya',
'Chili',
'Ramen',
'Salmon',
'Veggie Kebabs',
'Pork Chops',
'Chicken Noodle Soup',
'Tuscan Chicken Soup',
'Random Recipe from Cookbook',
'Big Salad']
random.shuffle(mylist)

random_index = random.randrange(len(mylist))

#print(mylist[random_index])

print(random.sample(mylist,4))
