"""Included in the exercise is a zipfile, 'files.zip'. It contains 200 files with random character strings for names, all lowercase. First, unzip this file into a directory named 'original_files'.

Your job is to write a program, ex1.py, that does the following things:

Create 26 directories in the current directory, one for each letter of the alphabet: ./a/ ./b/ ./c/ etc.

Loop through all the files in the original_files directory, and organize each of those files into the directory that their name starts with.
"""

import os
import string
import shutil

for letter in string.ascii_lowercase:
    os.mkdir(letter)

list_of_files = os.listdir('files')

for item in list_of_files:
    shutil.move('files/' + item, item[0])