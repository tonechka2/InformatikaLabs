from random import randint
row,col = 4,4
b = []
a = [[randint(-3,6) for i in range (col)] for i in range (row)]
for i in range (col):
    for j in range(row):
        print(f'{a[i][j]}', end ='')
    print()
for i in range(col):
    for j in range(row):
        if a[i][j]>=0:
            b.append(a[i][j])
sum = sum(b)/len(b)
print(f'{b}{sum}')
