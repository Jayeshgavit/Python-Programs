

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote");
elif age >= 16:
    print("You are eligible to drive, but not vote");
elif age < 0 :
    print("Invalid age");
elif age == 0:
    print(" age 0 means invalid age");
else:
    print("You are not eligible to vote or drive");