numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

#add method
# Add one element to a set.
numbers = {1, 2, 2, 3, 3, 4}
numbers.add(5)
print(numbers)

#update Method
#Adds multiple elements from another iterable such as a list, tuple, or set.
numbers = {1, 2, 2, 3, 3, 4}
numbers.update([10,9,7])
print(numbers)

#if another set
numbers = {1, 2, 2, 3, 3, 4}
numbers_2 = {5,11,12,13}
numbers.update(numbers_2)
print(numbers)

#Remove Method
'''
Removes a specified element from the set. If the element does not exist, 
it raises a KeyError
'''
numbers = {1, 2, 2, 3, 3, 4}
numbers.remove(3)
print(numbers)

#discard Method
'''Removes a specified element. Unlike remove(), it does not give an error if
 the element is not present.'''
numbers = {1, 2, 2, 3, 3, 4}
numbers.discard(7)
print(numbers)

#pop Method
#Removes and returns an arbitrary element from the set.
numbers = {1, 2, 2, 3, 3, 4}
print(numbers.pop())
print(numbers)

#clear Method
#Removes all elements from the set.
numbers = {1, 2, 2, 3, 3, 4}
numbers.clear()
print(numbers)


#union Method
#Returns a new set containing all unique elements from both sets.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.union(B))
print(A|B)   # "|" alse used as union


#Intersection Method
#Returns the elements that are common to both sets.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.intersection(B))
print(A&B)  # "&" also used as intersection


#difference()
#Returns elements that are present in the first set but not in the second set.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.difference(B))
print(A-B)

#symmetric_difference()
#Returns elements that are in either set, but not in both.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.symmetric_difference(B))
print(A ^ B)

#These methods modify the original set instead of creating a new set.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.intersection_update(B)
print(A)
A.difference_update(B)
print(A)
A.symmetric_difference_update(B)
print(A)


#isdisjoint Method
#Checks whether two sets have no common elements.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.isdisjoint(B))

#issubset Method
#Checks whether all elements of one set are present in another set.
A=  {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.issubset(B))

#Copy Method
#Creates a shallow copy of the set.
A = {1, 2, 3}
B = A.copy()

B.add(5)
print(A)
print(B)

