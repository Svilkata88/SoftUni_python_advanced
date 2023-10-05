import os
import re

file = open('words.txt ', 'w')
file.write('''
-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here…It is safer.
''')
file.close()

with open('words.txt', 'r') as text_file:
    text_file = text_file.read().lower()

word_input = input().split()
searched_words = []
for word in word_input:
    pattern = rf'\b{word}\b'
    match = re.findall(pattern, text_file)
    if match:
        searched_words.append(f'{match[0]} - {len(match)}')

sorted_searched_words = sorted(searched_words, key=lambda word: -(int(word[-1])))
print(*sorted_searched_words, sep='\n')