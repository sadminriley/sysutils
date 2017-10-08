#!/usr/bin/python
import multiprocessing
import os
import sys

def main(string, dir):
    '''
    Locates a file using os.walk via multiprocessing
    using user inputted search string and search directory
    '''
    output = []
    for item in os.walk(dir):
        output.append(item)
        for item in output:
            if string in output:
                for item in string:
                    print('Found %s' % item )
            else:
                print('Nothing found!')


if __name__ == '__main__':
    multi_process = multiprocessing.Process(target=main, args=(sys.argv[1], sys.argv[2]))
    multi_process.start()
    multi_process.join()


