import os
import string
import shutil

for letter in string.ascii_lowercase:
    os.mkdir(letter)

list_of_files = os.listdir('files')

for item in list_of_files:
    shutil.move('files/' + item, item[0])