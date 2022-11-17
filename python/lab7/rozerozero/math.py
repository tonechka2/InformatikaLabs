import math
import random
def math_func():
    var = []
    p_eq = []
    def import_var():
        for i in range(6):
            #var.append(int(input()))
            var.append(random.randint(-100,100))
        return var

    def calculation():
        f_eq_1 = 0
        temp = 0
        f_eq_1_1 = (((var[1] + var[2])**2 + 1.08 * 10**3)**1/2) - var[3]
        f_eq_1_2 = (((var[4] + var[2])**2 + 1.08 * 10**3)**1/2) - var[3]
        f_eq_1_3 = (((var[5] + var[2])**2 + 1.08 * 10**3)**1/2) - var[3]
        while temp < 50:
            temp += 5
            if temp <= 11.4: f_eq_1 = f_eq_1_1
            elif ((temp > 11.4) or (temp <= 37.8)) : f_eq_1 = f_eq_1_2
            elif temp >  37.8: f_eq_1 = f_eq_1_3
            f_eq_2 = 1250/((((temp + var[2])**2 + 1.08 * 10**3)**1/2) - (var[3] - 1))
            p_eq.append(math.exp(var[0] * (2.68 * (1 - f_eq_2 / f_eq_1) - 1)))
            print('temp:', temp, ' pressure:', p_eq[-1])
        return p_eq 
    import_var()
    calculation()
    print(p_eq)
math_func()