import math
from random import randint
def main():
    var = int (input('Введите номер задания: '))
    def first():
        a = []
        pr = 1
        for i in range(7):
            a.append(randint(0, 10))
            if a[i]>1:
                pr = pr*a[i]
        
        minInd = a.index(min(a))
        maxInd = a.index(max(a))
        print(f'Мин индекс = {minInd}, Макс индекс = {maxInd}, Сумма {sum(a)}, Произведение = {pr}')
    
    def second():
        a = [2.1, 3.2, 4.8, 5.7]
        c = [2, 4, 6, 8]
        b = 18
        pr = 1
        summ = 0
        ans = 0 
        for i in range(4):
            summ = summ+a[i]+math.sqrt(b)
            pr = pr*math.sin(c[i])
        ans = summ + pr
        print(ans)
        

    def thrid():
        B = [2, 5, -6, 8, -3, 7, 12, -45, 106, 4]
        Ko = 0
        Kp = 0
        K = 0
        for i in range(10):
            if B[i]<0:
                Ko = Ko+1
            if B[i]>0:
                Kp = Kp+1
        K = (Ko+Kp)/Ko
        print(K)

    def fourth():
        B = []
        for i in range(7):
            B.append(randint(-3, 10))
        print(B)
        Kp = 0
        a = 7.7
        c = 9.5
        for k in range(7):
            if B[k]>0:
                Kp = Kp+B[k]
            if max(B)>c:
                for j in range(7):
                    print(B[j]/a)
        else:
            for j in range(7):
                print(B[j]*Kp)
    if var == 1:
        return first()
    elif var == 2:
        return second()
    elif var == 3:
        return thrid()
    elif var == 4:
        return fourth()
main()
        

    




