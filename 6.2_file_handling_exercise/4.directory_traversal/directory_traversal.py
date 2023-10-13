import os

files = {}

directory = input()

for dir in os.listdir(directory):
    file = os.path.join(directory, dir)
    if os.path.isfile(file):
        ext = '.' + dir.split('.')[-1]
        if ext not in files:
            files[ext] = []
        files[ext].append(dir)
    if os.path.isdir(file):
        for element in os.listdir(file):
            sub_file = os.path.join(file, element)
            if os.path.isfile(sub_file):
                ext = '.' + element.split('.')[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(element)

with open(os.path.join(directory, 'report.txt'), 'w') as f:
    content = ''
    for key, value in sorted(files.items()):
        content += key + '\n'
        content += '\n'.join([f'- - - {el}' for el in sorted(value)])
        content += '\n'
    f.write(content)
