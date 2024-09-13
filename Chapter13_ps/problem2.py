from rich import print   

print("\n")
print("[bold magenta] 2. Write a program to print third, fifth and seventh element from a list using enumerate function. [/bold magenta]\n")

list = [1,2,3,4,5,6,7,8,9,10,11]

for index, items in enumerate(list):
    if index== 3 and index==5 and index==7:
        print(f" index {index} items is {items}")
   