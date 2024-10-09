
def positive_or_negative(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
    
n = float(input("Enter the number : "))
rs = positive_or_negative(n)

print(f"\nThe number {n} is {rs}.")