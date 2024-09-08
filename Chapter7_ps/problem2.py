# p1 = "Make lot of money"
# p2 = "Earn a lot of money"
# p3 = "Join my club"
# p4 = "Donate money"
# p5 = "Invest money"
# p6 = "click here"

# inputstr = input("Enter a COMMENT : ")

# if inputstr == p2 or inputstr == p1 or inputstr == p3 or inputstr == p4 or inputstr == p5 or inputstr == p6:
#     print(" This is Spam commenet..")
# else:
#     print("This is Genuine Comment ")




# List of predefined spam phrases
spam_phrases = ["Make lot of money", "Earn a lot of money", "Join my club", "Donate money", "Invest money", "click here"]

# Get user input
inputstr = input("Enter a COMMENT: ")

# Check if the input matches any spam phrase
if inputstr in spam_phrases:
    print("This is a Spam comment.")
else:
    print("This is a Genuine Comment.")


