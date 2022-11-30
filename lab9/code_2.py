from random import randint


row_count, col_count = 3, 3
row, col = 3, 3
a = [[randint(1, 10) for j in range(col)] for i in range(row)]
for i in range(row_count):
    for j in range(col_count):
        print(a[i][j], end=' ')
    print()
print (f'Сумма элементов первой и последней строки: {sum(a[0])+sum(a[2])}')