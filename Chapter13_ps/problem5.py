
from rich import print   
print("[bold magenta] Store the multiplication tables generated in problem 3 in a file named Tables.txt. [/bold magenta]\n")
n = int(input(" Enter a Number to print Table :  "))
list = [n *  i for i in range(1,11)]

try: 
    f = open('table.txt', 'a+')                     # a + w = r+ for write or append / a+ append and read
    f.write(f"\nThis is a table of {n} :\n")
    for i in list:
        f.write(str(i) + '\n')

     # Move the file pointer to the beginning before reading
    f.seek(0)

    # Read and print the file content
    print("\nFile Data:")
    print(f.read())

except Exception as e:
    print("An error occurred while writing to the file: ", e)


finally: 
    print("\n Program finished")