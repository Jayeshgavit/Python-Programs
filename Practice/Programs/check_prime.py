# Python program to check number is prime or not 


def is_prime(n):
        if n == 1: 
             return f"{n} is Not prime."
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    return f"{n} is Not prime."
                else:
                    return f"{n} is prime."


n = int(input("Enter the Number : "))
print(is_prime(n))