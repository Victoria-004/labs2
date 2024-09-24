import math

a = 1.1
b = 2
h = 0.1
d = 0.001

def series_function(x, d): #функція обчислює суму ряду для заданого значення x з точністю до похибки d
    total_sum = 0 #Змінна, що накопичує суму ряду
    k = 1
    term = 1 #початкове знач члена ряду


    while abs(term) > d:
        term = (1 / (2 ** k)) * math.sin(x / (2 ** k))  #oбчислення чергового члена ряду
        total_sum += term
        k += 1


    return total_sum

x = a
while x <= b:
    print(f"x = {x}, сума = {series_function(x, d)}")

    x += h
