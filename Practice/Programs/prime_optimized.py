
import math
def is_prime(num):
    if num < 2: 
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


num = int(input(" Enter the Number " ))

if is_prime(num):
    print("Prime")
else:
    print("Not prime")
    