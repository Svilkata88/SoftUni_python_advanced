
def numbers():
    numbers = [int(el) for el in input().split()]
    negatives = []
    positives = []
    for num in numbers:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)
    print(sum(negatives))
    print(sum(positives))
    if sum(positives) > abs(sum(negatives)):
        print('The positives are stronger than the negatives')
    else:
        print('The negatives are stronger than the positives')


numbers()