#! /usr/bin/python
# -*- coding:utf-8 -*-

import locale

locale.setlocale(locale.LC_ALL, '')

def load_file(filename):
    f = open(filename, 'r')
    content = f.readlines()

    return content

def main():
    content = load_file('magyar_szavak')
    new_content = ''
    wordList = []

    for string in content:
        new_content += string

    l = new_content.split(' ')
    for i in l:
        print i
    
    f = open('output', 'w')
    for i in l:
        f.write(i)
        f.write('\n')

if __name__ == '__main__':
    main()
