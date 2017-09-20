#!/usr/bin/python
import csv
import sys

def main():
    csvdoc = raw_input('What CSV file would you' +
                       'like to parse?\n')
    delim = raw_input('What delimiter would you like' +
                      'to use while parsing?\n(examples would be , or .)\n')
    try:
        with open(csvdoc) as file:
            reader = csv.reader(file, delimiter=delim, quotechar='|')
            for item in reader:
                print ' '.join(item)
    except IOError as e:
            print('Please enter a valid .csv file! Closing..')
            sys.exit()

if __name__ == '__main__':
    main()
