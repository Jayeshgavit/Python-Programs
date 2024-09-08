


info = {'name': 'jayesh', 'age': 27, 'email': 'jayesh08@gmail.com'}

print("\nOriginal dictionary : ", info)

print("\nPrint all keys :", info.keys())

print("\nPrint all values :", info.values())

print("\nPrint using info.grt('email') : ",info.get('email'))

# adda items
info['DOB'] = '2002-05-01'
info['Address'] = 'Nashik, Maharashtra'

print("\n\tAfter adding items : ", info)

#update items
info['age'] = 23
print("\n\tAfter updating age : ", info)

info.update({'age': 22})
print("\n\tAfter update() using age : ", info)


# remove items
info.pop('email')
print("\n\tAfter popping item using info.pop('email') : ", info)

dict = {1:'jayesh', 2:'Aniket', 3:'Devzz'}
dict.popitem()
print("\n\tDelete last pair using popitem() : ", dict)

dict.clear()
print("\n\tClear() dict : ", dict)

dict = {1:'jayesh', 2:'Aniket', 3:'Devzz'}
del info['Address']

print("\n\tAfter deleting item using del info['address'] : ", info)

# copy dicts 

info_copy = info.copy()
print("\n\tCopy of info dict : ", info_copy)

dict_copy = dict.copy()
print("\n\tCopy of dict dict : ", dict_copy) 


















print("\n")