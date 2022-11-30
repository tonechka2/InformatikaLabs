p = [[-3, 10, 15],
    [32, 12, -5]]
x = [-3.5, 120.4, -3.9, 6.11]
min_num = min(p[0])
max_num = max(x)
c = 0
for elem in range(len(x)):
    if x[elem]>=0:
        c += 1
print(f'{(min_num+max_num)/c}')