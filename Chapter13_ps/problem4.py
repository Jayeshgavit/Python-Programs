from rich import print  

print("[bold magenta] 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’. [/bold magenta] ")



try: 
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number : "))

    result = a / b

    print(f"The result of {a} / {b} is {result}")

except ZeroDivisionError:

    print("Error: Division by zero is not allowed.")














