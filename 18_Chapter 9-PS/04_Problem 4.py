'''
A file contains a word “Donkey” multiple times. You need to write a program which
replaces this word with ##### by updating the same file.
'''
word ="Imran"

with open("file.txt","r") as f:
    content=f.read()


ContentNew=content.replace(word,"#####")

with open("file.txt","w") as f:
    f.write(ContentNew)



