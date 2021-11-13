#import pandas
#df = pandas.read_csv('Dinner.csv')
#print(df)
#f = open("Dinner.csv", "r")
#print(f.read())
#import numpy as np

#arr = np.array(open("Dinner.csv", "r"))
#print(arr)
import csv
import random
value = input("please enter the number of Dinners you need decided:\n")
value = int(value)
#value2 = input("You wanted to have {value} Dinners decided is that right? Press Enter to Continue")
print(f'Calculating {value} Dinners')
#below imports the csv and makes it a list to clean up the code base and allows for easier reading
with open('Dinner.csv', newline='')as f:
    reader = csv.reader(f)
    mylist = list(reader)

random.shuffle(mylist)
random_index = random.randrange(len(mylist))

#print(mylist[random_index])

print(random.sample(mylist,value))#the number after the comma is how many dinners you would like to figure out. 
