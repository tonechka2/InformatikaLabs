from random import randint
import math
import numpy as np
row_count, col_count = 5, 10
rowmax = []
a = [[randint(0, 9) for j in range(col_count)] for i in range(row_count)] 
for i in range(row_count):
    for j in range(col_count):
        print(a[i][j], end = ' ')
    print()
arr_matrix = np.array(a[i][j])
arr_transpose = np.transpose(arr_matrix)
for j in range(col_count):
    for i in range(row_count):
        if(a[i][j] == max(a[i])):
            rowmax.append(a[i][j])
for i in range(row_count):
    print(arr_matrix)
    print(arr_transpose)
for i in range(row_count):
    maxmin = max(rowmax)
print(f'Максимальный из них : {a[i].index(maxmin)}')
