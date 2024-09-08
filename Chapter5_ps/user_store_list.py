no = int(input("Enter a number of elements to be insert : "))

list = [];

for i in range(no):
    element = input("Enter element : ")
    list.append(element)
print(list)

print("Length of list : ", len(list))
print("index of '0' : ", list[0])
print("Count of '1' : ", list.count('1'))