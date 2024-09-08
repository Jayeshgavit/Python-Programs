a = " welcome to python Jusrnoey "

# write  
f = open("text.txt", "w")
f.write(a)
f.close()

# read file  

r = open("text.txt", "r")
print (r.read())