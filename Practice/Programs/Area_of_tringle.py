'''Calculate the Area of a Triangle'''

height = float(input("Enter the Height : "))
base = float(input("Enter the Base : "))

def calculate_area_triangle(height, base):
    return (height * base) / 2   # 0.5 or 2 is generate same output

area = calculate_area_triangle(height, base)

print(f"Area of triangle is {area:.2f}")



'''
of Triangle Area Calculation Program:
Purpose: The program calculates the area of a triangle using the formula:
 Area = (base * height) / 2

Input: h : 12.5 b: 5.5 output : 34.38

The program prompts the user to enter the height and base of the triangle.
Both inputs are converted to floating-point numbers for accurate calculations.
Function:

A function named calculate_area_triangle is defined, which takes height and base as parameters and returns the calculated area using the formula.
'''