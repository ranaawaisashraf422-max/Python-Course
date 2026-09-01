# Write a program to mine a log file and find out whether it contains ‘python’
with open("log.txt") as f:
    content = f.read()

if ("python" in content):
    print("Yes, Python is present in content")

else:
     print("No! Python is not present in content")