
''' def greatest(n1,n2,n3):
    if n1 > n2:
        if n1 > n3:
            print ("n1 is greatest")
    elif n2 > n3:
        print(" n2 is greatest")

    else:
        print("n3 is greatest")


greatest(6,9,3) '''



def greatest_num(n1,n2,n3):
    if(n1 > n2) and (n1 > n2):
        return n1
    elif(n2 > n1) and (n2 > n3):
        return n2 
    elif(n3 > n1) and (n3 > n1):
        return n3
    
print(greatest_num(1,2,4))