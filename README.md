# Root Finding with Bisection and Newton's Method

This is a simple Python project to find the root of a polynomial function using two classical numerical methods:

- **Bisection Method**
- **Newton's Method**

The goal is to demonstrate basic techniques in numerical analysis for solving equations of the form _f(x) = 0_.

##  How It Works

- The function to solve is: f(x) = x⁴ + 3x³ - 9x² - 23x - 12

- You input the interval `[a, b]` for bisection and precision `r` (number of decimal digits).
- The program calculates:
- The number of iterations needed using `log2((b - a) / ε)`
- The root of the function using both methods (if applicable)

###  Libraries Used

- `math` – for mathematical operations
- `tkinter.messagebox` – for displaying results via GUI pop-ups



