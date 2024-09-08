list = [1, 2, 3, 4, 5, 'a', 'b', 'c']

i=0;
print("\nPrinting list elements using while loop:")

while i< len(list):
    print(list[i], end=', ')
    i+=1;

print("\n\nPrinting list using for and in : ")
for j in list:
    print(j, end=', ')



print("\n\nPrinting list elements using range function: ")
for i in range(len(list)):
    print(list[i], end=', ')



print("\n\nPrinting list elements in reverse order using range function with step -1: ")
for i in range(len(list)-1, -1, -1):
    print(list[i], end=', ')
print("\n")