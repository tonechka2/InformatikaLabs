import math
from random import randint
def main():
    var = input("Введите номер задачи: ")
 
    def first():
        f = [randint(0,10) for _ in range(10)]
        f_max, f_min, i_max, i_min,s,p = f[0], f[0], 0, 0,0,1
        for i in range(len(f)):
            if f[i] > f_max:
                f_max, i_max = f[i], i
            if f[i] < f_min:
                f_min, i_min = f[i], i
            s += f[i]
            p *= f[i]
        print(f'Min: f[{i_min}] = {f_min}; Max: f[{i_max}] = {f_max};\n Sum: {s}; Prod: {p}')
 
    def second():
        a= [2.1,3.2,4.8,5.7]
        c= [2,4,6,8]
        x,y,z=1,0,1
        sum,pr,b=0,1,18
        for i in a:
            sum+=x*(i+(b**0.5))
            x+=1
        for i in c:
            pr*=z*(math.sin(i))
            z+=1
        y=sum+pr
        print(y)
 
 
    def third():
        f = [randint(-10, 10) for _ in range(10)]
        lst=[]
        lst1=[]
        for i in f:
            if i<0:
                lst.append(i)
            else:
                lst1.append(i)
        k=(10/len(lst))
        print(k)
 
 
    def fourth():
        f = [randint(-3,10) for _ in range(7)]
        f_max=0
        c=9.5
        a=7.7
        lst=[]
        for i in range(len(f)):
            if f[i] >= f_max:
                f_max = f[i]
        if f_max > c:
            f = [i/a for i in f]
        else:
            for i in f:
                lst.append(i)
                f = [i*len(lst) for i in f]    
        print(f)
 
 
    if var == "один":
        return first()
    elif var == "два":
        return second()
    elif var == "три":
        return third()
    elif var == "четыре":
        return fourth()
 
main()