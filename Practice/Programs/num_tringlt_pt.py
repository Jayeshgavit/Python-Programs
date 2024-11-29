#1: Simple Number Triangle Pattern

rows = 6 

for num in range (1,6):
    for i in range(num):
        print(num - i, end=' ')
    print(" ")



'''
[Running] python -u "d:\Python\Python-Programs\Practice\Programs\num_tringlt_pt.py"
1  
2 1  
3 2 1  
4 3 2 1  
5 4 3 2 1  

'''
