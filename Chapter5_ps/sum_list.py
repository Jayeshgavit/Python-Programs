
no  = int(input("Enter the number of elements in the list: "))

list = []

for i in range(no):
    element = input("Enter element : ")
    list.append(int(element))

print("Original List: ", list)
print("Sum of elements: ", sum(list))

sum1 = 0
for j in list:
    #sum1 += j 
    sum1 = sum1 + j
print("Sum of elements using (sum1 = sum1 + j): ", sum1)