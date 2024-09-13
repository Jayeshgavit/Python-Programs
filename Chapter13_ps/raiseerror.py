

def check_valu(n):
    if n < 0:
        raise ValueError("n must be positive");


n = int(input(" Enter the number : "))
check_valu(n)