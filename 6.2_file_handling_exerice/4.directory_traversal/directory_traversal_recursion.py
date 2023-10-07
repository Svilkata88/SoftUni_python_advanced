import os


def check_files(folder, level):
    if level < 0:
        return
    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            ext = '.' + element.split('.')[-1]
            if ext not in files:
                files[ext] = []
            files[ext].append(element)
        else:
            check_files(f, level - 1)


files = {}
directory = input()  # input should be ',/' to be sure program will check files in example folder!
check_files(directory, 1)  # level = 1 for 1 level files check below example dir!


with open(os.path.join(directory, 'report.txt'), 'w') as f:  # writing in the report file!
    content = ''
    for key, value in sorted(files.items()):
        content += key + '\n'
        content += '\n'.join([f'- - - {el}' for el in sorted(value)])
        content += '\n'
    f.write(content)
