from random import randint
import numpy as np
row, col = 3, 3
a = [[randint(-5, 5) for _ in range(col)] for _ in range(row)]
sum = 0
min = []
for i in range(row):
    for j in range(col):
        min.append(a[i][j])
        if a[i][j] > 0: sum = sum + a[i][j]
        print(a[i][j], end=' ')
    print()
min.sort()
wer = min[0]
print(f'sum: {sum}')
print(f'min: {min.pop(0)}')
print(wer*sum)