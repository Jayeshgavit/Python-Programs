strr = input(" Enter data : ")

with open('handleing.txt', 'a') as f:
    f.write(f"\n{strr}");

with open('handleing.txt', 'r') as f:
    print(f.read())
    print("\n\tFile data read successfully")



file = open('handleing.txt');
print(file.readline())
    
