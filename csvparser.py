#!/usr/bin/python
import csv

csvdoc = raw_input('What CSV file would you like to parse?\n')
delim = raw_input('What delimiter would you like to use while parsing?\n(examples would be , or .)\n')
with open(csvdoc) as file:
    reader = csv.reader(file, delimiter=delim, quotechar='|')
    for item in reader:
        print ' '.join(item)
