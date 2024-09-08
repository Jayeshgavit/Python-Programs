

f = open("text.txt")
# lines = f.readlines()
# print(lines)



line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()
