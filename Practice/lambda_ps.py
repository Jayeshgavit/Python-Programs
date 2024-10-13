double = lambda x : x * x 
print(double(4))


sumn = lambda x, y : x + y
print(sumn(12,12))


suml = lambda: [1,2,3,4,5,6,7,8,9,10] + [1,2,3,4,5,6]

print(suml())


Number = [1,2,3,4,5,6,7,8,9,10]

even = filter(lambda x: (x % 2 ==0), Number)
print(list(even))

