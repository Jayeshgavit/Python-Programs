tuple_data = (1, 2, 3, 0, 4, 7, 0, 5)

count = 0;
print("\n Original tuple: ", tuple_data)
for i in tuple_data:
    if i == 0:
        count=count+1
print("\n\tNumber of zeros in the tuple using (xount = count  1): ", count)



# Counting the number of zeros in a tuple using list comprehension
zeros = [i for i in tuple_data if i == 0]
print("\n\tNumber of zeros in the tuple using xomprehension: ", len(zeros))


# Counting the number of zeros in a tuple using count() function
print("\n\tNumber of zeros in the tuple using count() : ", tuple_data.count(0))

print("\n\n")