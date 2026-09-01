#Append Method
friends=["apple","orange",6,34.975,"akash","rohan"]
print(friends)

friends.append("Harry")
print(friends)

#Sort Method
l1= [1,56,82,11,34,9,67]
l1.sort()
print(l1)

#Reverse Method
l1= [1,56,82,11,34,9,67]
l1.reverse()
print(l1)

#Insert Method
l1= [1,56,82,11,34,9,67]
l1.insert(3,9)
print(l1) 

#pop method
l1= [1,56,82,11,34,9,67]
l1.pop(3)
print(l1)

#remove method
l1=[23,45,18,98,67,456]
l1.remove(18)
print(l1)

#entend method
l1= [1,56,82,11,34,9,67]
l1.extend(([30,40]))
print(l1)

#clear method
l1= [1,56,82,11,34,9,67]
l1.clear()
print(l1)

#index method
l1= [1,56,82,11,34,9,67] #index() return index not list so li.index() not alone
print(l1.index(82))

#count method
l1= [1,56,82,11,82,34,67,34,9,67] #count return index not list so count() not alone
print(l1.count(82))

#copy method
l1= [1,56,82,11,82,34,67,34,9,67]
l2=l1.copy()
print(l1)
print(l2)



