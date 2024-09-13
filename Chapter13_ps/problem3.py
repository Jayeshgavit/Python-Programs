from rich import print 

print("\n[bold magenta] 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number. [/bold magenta]\n")

n = int(input(" Enter a Number to print Table :  "))
list = [n *  i for i in range(1,11)]
print(list)