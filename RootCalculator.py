
import math
from tkinter import messagebox

'''
The purpose is calculating the root of functions by using bisection and Newton method;
The root of f(x) is between a and b, n is the minimum repetition of bisection method that calculate by log.
'''
a = float(input('please enter a: '))
b = float(input('please enter b: '))
r = int(input('pleae enter r (rD):'))
ε = 5*(10**(-r-1))
n = math.log2((b-a)/ε)
print(n)
m = int(input('please enter N(repetition): '))
 
def f(x):
    return x**4+3*x**3-9*x**2-23*x-12

def bisect(func, a, b, ε, m):
    if func(a) * func(b) > 0:
        print("try again! func(a)*func(b) > 0")
    
    for i in range(0, m):
        mid = (b + a)/2.0
        if func(mid) == 0 or abs(func(mid))< ε:
            return mid
            break
        if func(mid) * func(a) < 0:
            b = mid
        else:
            a = mid
    return f"Method failed after {m} iterations"
x = bisect(f, a, b, ε, m)

try:
    y_0 = x
    df = lambda x: math.cos(x) - 2*x
    def my_newton():
        if abs(f(y_0)) < ε:
            return y_0
        else:
            return my_newton(f, df, y_0 - f(y_0)/df(y_0), ε)
    newton_algorithm = my_newton()
    messagebox.showinfo('Newton method:   y = ', round(newton_algorithm, r))
except:
    messagebox.showinfo('error')
