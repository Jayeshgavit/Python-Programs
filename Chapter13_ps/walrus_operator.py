

if (n := len([1,2,3,4])) > 3:
    print(f" Then length of list is {n} and is greater tan expected n < 3")

print("\n");

# walrus operator in while loops
print("walrus operator in while loops".center(50, '-'))
count = 0 

while(user := input(" Enter the number (0 for quite) : ") ) != '0':

    count += 1

print(f"Total number of entered numbers is {count}")


print("\n");


# walrus operator in lisr comprehension

values = [2,4,6,8,10]

suared  = [square for v in values 
           if (square := v ** 2) > 10]
print("suared : ", suared) 