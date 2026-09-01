import random
n = random.randint(1,100)
a = -1
guesses = 1
while (a!=n):
    a= int(input("Guess the Number :"))
    if(a > n):
        print("Please! Enter a Lower Number")
        guesses +=1

    elif(a < n):
         print("Please! Enter a Higher Number")
         guesses+=1

print(f"You have guessed the number {n} correctly in {guesses} attempts")

