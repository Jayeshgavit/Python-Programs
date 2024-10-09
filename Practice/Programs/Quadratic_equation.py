# Solve Quadratic Equation
'''
To solve a quadratic equation, we need to find the values of the variable that satisfy the equation. A quadratic equation is generally written in the form:
    ax^2+bx+c=0

where:
    . a, b, and c are constants (with a != 0),

    . x is the variable to solve for.
'''

import cmath

a = int(input('a!=0, Enter the quadratic equation Value of a : '))
b = int(input('Enter Number b : '))
c = int(input('Enter Number c : '))

# !formula for discriminant d = b^2 - 4ac  help to determine nature of roots
d = (b**2) - (4*a*c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)


print(f" The roots are : {root1:.1f} and {root2:.1f}")

    





'''
!1. The `cmath` module is imported, which provides support for complex numbers and their mathematical operations.

2. The user is prompted to enter the values of constants `a`, `b`, and `c` for the quadratic equation `ax^2 + bx + c = 0`. The input values are converted to integers using the `int()` function.

3. The discriminant `d` is calculated using the formula `(b**2) - (4*a*c)`.
        ! d=b^2 - 4ac
4. The roots of the quadratic equation are calculated using the quadratic formula:
   - `root1 = (-b - cmath.sqrt(d)) / (2*a)`
   - `root2 = (-b + cmath.sqrt(d)) / (2*a)`
   
5. The roots are printed with a precision of 1 decimal place using the `f-string` formatting.

This script can be used to solve quadratic equations by providing the values of `a`, `b`, and `c`.
'''
