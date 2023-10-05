import os

#with open('my_first_file.txt', 'r') as file:
    #print(file.read(100))

try:
    os.remove('my_first_file.txt')
except FileNotFoundError:
    print('File already deleted!')