myList = [1,2,9,5,3,5]
squaredList = []
for item in myList:
    squaredList.append(item*item)

print(squaredList)

# This can be done easily by using List Comprehension
squaredList=[i*i for i in myList]
print(squaredList)