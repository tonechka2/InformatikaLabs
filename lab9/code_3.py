from random import randint
row_count, col_count = 4, 4
rowmax = []
a = [[randint(1, 100) for j in range(col_count)] for i in range(row_count)] 
for i in range(row_count):
    for j in range(col_count):
        print(a[i][j], end = ' ')
    print()
for j in range(col_count):
    for i in range(row_count):
        if(a[i][j] == max(a[i])):
            rowmax.append(a[i][j])
for i in range(row_count):
    print(f'Максимальный элемент строки {i} : {rowmax[i]}')
maxmin = min(rowmax)
print(f'Максимальные элементы строк : {rowmax} \nМинимальный из них : {maxmin}')

