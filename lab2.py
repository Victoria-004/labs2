from math import log, cos, sin

def log_base_5(x):
    return log(3 * x + 1) / log(5)

def cos_over_x(x):
    return cos(x) / x

def csc_ln_x(x):
    return 1 / sin(log(x))

a = 0.1
b = 0.7
h = 0.05

x = a
while x <= b:
    if x < 0.2:
        y = log_base_5(x)
    elif 0.2 <= x < 0.4:
        y = cos_over_x(x)
    else:
        y = csc_ln_x(x)

    print("x = " + str(x) + ", y = " + str(y))
    x += h



