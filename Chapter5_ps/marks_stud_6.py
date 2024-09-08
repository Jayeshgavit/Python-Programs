no = int(input("Enter no. students marks going to be inserted : "))

list = [];

for i in range(no):
    element = input("Enter marks: ")
    list.append(int(element))
print(list)

list.sort();
print("\nSorted list using list.sort(): ", list)


list.sort(reverse=True);
print("\nSorted list using list.sort(reverse=True): ", list)
sorted_list = sorted(list);
print("\nSorted list using sorted(): ", sorted_list)
