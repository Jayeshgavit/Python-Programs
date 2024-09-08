
def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n 
    
l = ["Harry", "Jayesh", "an", "Rohan", "Shubham"]
print("Output : ", rem(l, "an"))