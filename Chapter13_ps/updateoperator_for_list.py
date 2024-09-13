print("Update operator for dictionaries (|=)".center(80, '-'))

print("\n")

dict1 = {"Name": 'Jay', "Age": 18}
dict2 = {"Name": 'Jayesh', "Age":23}
print(" Dictionaries 1  and 2 are : ", dict1, dict2)
print("\n")

dict1 |= dict2

print("After using |= operator : ", dict1)




'''
The contents of dict2 are merged into dict1, and the original dict1 is modified in-place.

'''


'''
Merge dictionaries and get a new dictionary: merged_dict = dict1 | dict2
Update an existing dictionary: dict1 |= dict2

'''