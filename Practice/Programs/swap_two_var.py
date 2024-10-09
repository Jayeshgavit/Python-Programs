# Pthon program to swap two varoable



num1 = input("Enter the number 1 : ")
num2 = input("Enter the number 2 : ")

print(num1, num2)

# way 1 :
num1, num2 = num2, num1

print("After swapping : num1 = ", num1, " and num2 = ", num2)

# way 2 : 

temp = num1 
num1 = num2
num2 = temp

print("After swapping : num1 = ", num1, " and num2 = ", num2)
