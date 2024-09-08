
dict = {'Thank you' : 'Dhanywad', 'Run' : 'Dudna', 'Sit': 'Baithna' , 'Sing': 'Gana Gau'}

print(dict)


input = input("Enter string : ")

if input in (dict.keys()):
    print(dict[input])
else:
    print("Not found")

translations = {'Thank you': 'Dhanywad', 'Run': 'Dudna', 'Sit': 'Baithna', 'Sing': 'Gana Gau'}

print(translations[input])