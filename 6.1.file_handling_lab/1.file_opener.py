import os

try:
    working_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(working_directory, 'text.txt')
    file = open(file_path, 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')

