
from rich import print   
print("[bold magenta] Store the multiplication tables generated in problem 3 in a file named Tables.txt. [/bold magenta]\n")


n = int(input(" Enter a Number to print Table :  "))
list = [n * i for i in range(1,11)]

try: 
    with open('tables.txt', 'a') as f:
        f.write(f"\n [bold magenta] This is an table of  {n} [/bold magenta]: {str(list)}\n") 
        
    with open('tables.txt', 'r') as f:
        print("\nFile Data:")
        print(f.read())

except Exception as e:
    print("An error occurred while writing to the file: ", e)


finally: 
    print("\n Program finished")