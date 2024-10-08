
''' way: 1 reverse string using for loop'''
def reverse_str(s):
    result = ''
    for i in s:
        result = i + result
    return result

str = 'Hello, World!'
reversed_str = reverse_str(str)
print(reversed_str)

''' way:2 using reversed and join methods'''

revserd_str2 = ''.join(reversed(str))
print(revserd_str2)


'''way:3 using slicing'''

str_slicing = str[::-1]
print(str_slicing)
