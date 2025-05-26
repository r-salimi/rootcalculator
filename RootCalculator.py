import math

'''
The purpose is finding the root of functions by using bisection and Newton methods;
The root of f(x) is between a and b; n is the minimum repetition of bisection method that calculate by log.
'''

a = float(input("Enter value for a (left bound): "))
b = float(input("Enter value for b (right bound): "))
r = int(input("Enter desired decimal precision (e.g. 3): "))
ε = 5*(10**(-r-1))
n = math.log2((b-a)/ε)
print("Minimum iterations for bisection method:", n)
m = int(input("Enter max number of iterations: "))

def f(x):
    return x**4 + 3*x**3 - 9*x**2 - 23*x - 12

def bisect(f, a, b, ε, m):
    if f(a) * f(b) > 0:
        print("try again! func(a)*func(b) > 0")
    
    for i in range(m):
        mid = (a + b)/2.0
        if f(mid) == 0 or abs(f(mid)) < ε:
            return mid
        if f(mid) * f(a) < 0:
            b = mid
        else:
            a = mid

x = bisect(f, a, b, ε, m)
print('Bisection Method Root:',x)

y_0 = x
df = lambda x: 4*x**3 + 9*x**2 - 18*x - 23
    
def my_newton(f, df, y, ε):
      if abs(f(y)) < ε:
          return y
      else:
          return my_newton(f, df, y - f(y)/df(y), ε)
    
newton_algorithm = my_newton(f, df, y_0, ε)
print('Newton Method Root:', newton_algorithm)
