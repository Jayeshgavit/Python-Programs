
list_num = [1,2,3,4,5]
list_char = ['a','b','c','d','e']
list_words = ['apple','banana','cherry','date','elderberry']
list_alpha = ['a','b','c','d','e','f','g','h','i',1,2,4,4,5]



print("\nOriginal List: ", list_num)
print("\nFirst item : ", list_num[0])


for index,item in enumerate(list_num):
    print(f"\nCurrent item {index}: ", item)


if 'apple' in list_words:
    print("\n'apple' is in the list_words")
else:
    print("\n'apple' is not in the list_words")


print("\nPrinting result using slicing : ", list_num[2:5])

print("\nPrinting result using negative index : ", list_alpha[1:13:3])


list_words.insert(2,'Grapes')
print("\nUpdated list_words: ", list_words)