
def factorial(num):
    if (num ==1 or num ==0):
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Number  : "))
print(f"\n\nNumber is : {num}")
print("Factorial is : ", factorial(num))
          