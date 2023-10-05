import os

working_directory = os.path.dirname(os.path.abspath(__name__))
file_path = os.path.join(working_directory, 'text.txt')
file = open(file_path, 'r')

print(sum([int(el) for el in file.read(100).split()]))