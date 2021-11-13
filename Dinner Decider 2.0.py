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

#below imports the csv and makes it a list to clean up the code base and allows for easier reading
with open('Dinner.csv', newline='')as f:
    reader = csv.reader(f)
    mylist = list(reader)

random.shuffle(mylist)

random_index = random.randrange(len(mylist))

#print(mylist[random_index])

print(random.sample(mylist,4))#the number after the comma is how many dinners you would like to figure out. 
