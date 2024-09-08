
cities = {'Nashik', 'Pune','Mumbai'}
print("\nCities in the set:", cities)

num_set = {1,2,3,4,5,6,7,8,9,10}
print("\nNumbers in the set:", num_set)

print("\nPrint set using a loop: ")
for i in num_set:
    print(i, end=" ")

#  add element to the set
cities.add('Dindori')
print("\n\nCities in the set after adding 'Dindori':", cities)

#  remove element from the se
cities.remove("Pune")
cities.discard("Mumbai")

print("\nCities in the set after removing 'Pune' and 'Mumbai':", cities)

#update sets

# cities.update(num_set)
# print("\n Update set using update() method:", cities)


#joins

set = {1,2,3,4,5}
set2 = {1,3,5,7,6}

print("\nOriginal sets1 : ", set , "\n set2 : ", set2)


new_set = set.union(set2);
print(f"\nUnion of {set} and {set2} : ", new_set)

new_set2 = set.intersection(set2);
print(f"\nIntersection of {set} and {set2} : ", new_set2)

new_set3 = set.symmetric_difference(set2);
print(f"\nSymmetric_difference of {set} and {set2} : ", new_set3)

new_set4 = set.difference(set2);
print(f"\nDifference of {set} and {set2} : ", new_set4)

#Methods
print("\nLength of set1 : ", len(set))
print("\n isdisjoint : ", set.isdisjoint(set2)) #false means they have at least one common element

print("\nIssubset : ", set.issubset(set2)) #true means set1 is a subset of set2

print("\nIssuperset : ", set.issuperset(set2)) #true means set2 is a superset of set1


print("\n")