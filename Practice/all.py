memo = {}
def factorial_memory(n):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = n * factorial_memory(n - 1)
    return memo[n]

print(factorial_memory(2))
print(memo)

def flatten(nested_list):
    newlist = []
    
    for char in nested_list:
        if isinstance(char, list):
            newlist.extend(flatten(char))  # Recursive call to flatten inner list
        else:
            newlist.append(char)  # Append non-list items
    
    return newlist  # Correctly indented return statement

print(flatten([1, 2, [4, 5], 6]))  # Expected output: [1, 2, 4, 5, 6]



def fabonacci(n, cache={}):
    if n in cache:
        cache[n]
    if  n <=2:
        return 1
    cache[n] = fabonacci(n-1, cache) + fabonacci(n-2,cache)
    return cache[n]


rs = fabonacci(10)
print(rs)

def fb(n):
    a,b=0,1
    for i in range(n):
        print(a, end=" ")
        a,b = b, a+b

fb(10)
    


