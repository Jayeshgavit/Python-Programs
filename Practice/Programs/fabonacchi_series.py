

def fibonacci(n):
    a,b = 0,1
    list1 = []
    for i in range(n):
        print(a, end='  ')
        a , b = b, a+b
    
n = int(input(" Enter the Value of  n : ",  ))
fibonacci(n)