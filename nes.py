#coding:utf-8
import sys

"""
Executable File
"""

if __name__ == '__main__':
    ron = b''
    with open(sys.argv[1], 'rb') as f:
        print(f.read())
    