
str = "Hello, World!"

print("Length is : ",len(str))
print("str.endswith  : ", str.endswith("!"))
print("str.startswith  : ", str.startswith("!"))
print("str.capitalize  : ", str.capitalize())
print("str.lower  : ", str.lower())
print("str.upper  : ", str.upper())
print("str.title  : ", str.title())
print("str.strip()  : ", str.strip) #remove whitespace after and before of string
print("str.rstrip()  : ", str.rstrip("!")) #remove whitespace after and before of string
print("str.lstrip()  : ", str.lstrip("H")) #remove whitespace after and before of string
print("str.replace('Hello', 'Hi')  : ", str.replace('Hello', 'Hi'))
print("str.find('World')  : ", str.find('World'))
print("str.split(' ')",str.split(' ')) #split string into list)
print("str.split(' , ')",str.split(' , ')) #split string into list)
print("str.split(' | ')",str.split(' | ')) #split string into list)

print("str.count('o')  : ", str.count('o')) #count number of 'l' in string

print("str.index('o')", str.index('o')) #find index of 'o' in string

print("str.center(10)  : ", str.center(50, '.')) #center string in

print("str.isalpha()  : ", str.isalpha()) #check if all characters

print("str.isdigit()  : ", str.isdigit()) #check if all characters are digits

print("str.isalnum()  : ", str.isalnum()) #check if all characters are alphanumeric