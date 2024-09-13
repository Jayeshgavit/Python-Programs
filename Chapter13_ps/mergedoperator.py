
print(" Merged Operator (dict1 | dict2)".center(50, '-'))

dict1 ={'Name': 'Jayesh', 'age': 23}
dict2 ={'Address': 'Nashik', 'Pincode': 422215}
print(f"dictionary1 : {dict1} , dictionary2 : {dict2} \n")

merged_dict = dict1 | dict2
print("merged_dict : ", merged_dict)