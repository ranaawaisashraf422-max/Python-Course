with(
    open("Chapter 12/file1.txt") as f1,
    open("Chapter 12/file2.txt") as f2
):
    print(f1.read())
    print(f2.read())