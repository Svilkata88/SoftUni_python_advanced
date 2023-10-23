from collections import deque

portions = [int(el) for el in input().split(', ')]  # last portion
stamina = deque([int(el) for el in input().split(', ')])  # 1st stamina
peak = 1
climbed_peaks = []
mapper_peaks = {
    1: [80, 'Vihren'],
    2: [90, 'Kutelo'],
    3: [100, 'Banski Suhodol'],
    4: [60, 'Polezhan'],
    5: [70, 'Kamenitza']
}

for climbings in range(7):

    current_portion = portions.pop()
    current_stamina = stamina.popleft()

    sum_result = current_stamina + current_portion
    current_peak_climbing_dif_level = mapper_peaks[peak][0]
    if sum_result >= current_peak_climbing_dif_level:
        climbed_peaks.append(mapper_peaks[peak][1])  # adding the peak to the list of the climbed peaks.
        peak += 1  # peak is climbed and both current portion and current stamina are removed! We go to next peak.
    if peak > 5:
        break

if peak > 5:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if climbed_peaks:
    print('Conquered peaks:')
    print(*climbed_peaks, sep='\n')
