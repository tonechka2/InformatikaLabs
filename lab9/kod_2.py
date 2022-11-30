import math
row_count, col_count = 3, 3
a = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
sum = sum(a[0])+sum(a[2])
for i in range(row_count):
    for j in range(col_count):
        print(a[i][j], end=' ')
print(a)
print (f'Сумма элементов первой и последней строки: {sum}')