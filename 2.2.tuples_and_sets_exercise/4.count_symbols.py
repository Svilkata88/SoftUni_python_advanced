input_text = [ch for ch in input()]
unique_letters = sorted(set(input_text))

for ch in unique_letters:
    count = input_text.count(ch)
    print(f'{ch}: {count} time/s')


