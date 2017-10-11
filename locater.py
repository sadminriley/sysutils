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
    for root, dirs, files in os.walk(dir):
        if string in os.path.join(root,string):
            output.append(os.path.join(root,string))
    for item in output:
        print item


if __name__ == '__main__':
    multi_process = multiprocessing.Process(target=main, args=(sys.argv[1], sys.argv[2]))
    multi_process.start()
    multi_process.join()


