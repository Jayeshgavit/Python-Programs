

def fibonacci(n):
    a,b = 0,1
    list1 = []
    for i in range(n):
        print(a, end='  ')
        a , b = b, a+b
    
n = int(input(" Enter the Value of  n : ",  ))
fibonacci(n)


def no_rp(s):
    dict = {}

    for char in s:

        dict[char] = dict.get(char, 0)+ 1

    for char in s:
        if dict[char] == 1:
            print(char)
            

a = no_rp('swifts')
print(a, end=' ')