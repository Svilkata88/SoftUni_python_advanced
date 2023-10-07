
new_lines = []

with open('text_file.txt', 'r') as f:
    for number_line, line in enumerate(f.readlines()):
        punc_chars = [ch for ch in line if not ch.isalnum() and not ch.isspace()]
        alpha_chars = [ch for ch in line if ch.isalpha()]
        new_lines.append(f'Line {number_line + 1}: {line.strip()} ({len(alpha_chars)})({len(punc_chars)})\n')

with open('result_file.txt', 'w') as result_file:
    result_file.write(''.join(new_lines))
