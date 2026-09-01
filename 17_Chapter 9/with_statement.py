f=open("file.txt")
print(f.read())
f.close()

#same can be done with; with statement
with open("file.txt") as f:
    print(f.read())

#not need to close the file