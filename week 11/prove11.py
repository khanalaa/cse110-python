
import csv

# year = int(input("Enter the year of interest: "))

with open("life-expectancy.csv", 'r') as data:
    read = csv.reader(data)

    for line in read:
        print(line)
    

