import csv
from sys import argv,exit
import tabulate
from tabulate import tabulate
if len(argv)!=2:
    if len(argv)>2:
        exit('Too many command-line arguments')
    if len(argv)<2:
        exit('Too few command-line arguments')
filename = argv[1]
dot = filename.find('.')
if filename[dot:] != '.csv':
    exit('Not a CSV file')
l = []
try:
    with open(filename,'r') as file:
        b = csv.reader(file)
        for a in b:
            l.append([a[0],a[1],a[2]])
except FileNotFoundError:
    exit('File does not exist')
print(tabulate(l,headers = 'firstrow',tablefmt="grid"))

