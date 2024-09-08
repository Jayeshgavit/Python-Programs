num = int(input(" No of Elements: "))

num_list = []
i = 1

for i in range(num):
    list_input = int(input("Enter number: "))  
    num_list.append(list_input)

sum_even = 0


for number in num_list:
    if number % 2 == 0:
        print(f"The number {number} is even.")
        sum_even += number
    else:
        print(f"The number {number} is odd.")


print(f"The sum of even numbers is: {sum_even}")




