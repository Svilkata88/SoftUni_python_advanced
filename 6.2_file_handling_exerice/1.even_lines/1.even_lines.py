symbols = ["-", ",", ".", "!", "?"]
with open('text_file.txt', 'r') as f:
    for index, line in enumerate(f.readlines()):
        if index % 2 == 0:
            for char in symbols:
                line = line.replace(char, "@")
            print(*reversed(line.split()))