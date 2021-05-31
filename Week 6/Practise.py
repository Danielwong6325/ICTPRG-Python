SB=[]
i=7
import random
N = random.randint(1,20)
print("Hey there! Lets play a little guessing game")
print("Guess the number between 1 and 20")
while i>0 :
    i=i-1
    num = int(input("Enter Guess:"))
    if num < N:
        print("Nope it is greater than that ")
        print("You have",i,"Guesses remain")
    if num > N :
        print("Nope it is less than that")
        print("You have",i,"Guesses remain")
        break
    if (num == N):
        break
    else:
        SB.append(num)
if num == N:
    print("Damn. You won")
    print("The number was indeed:",N)
    print("Your guess log:",SB)
else: 
    print("AHHAHA YOU LOOSE!")
    print("The number was",N,"You fool.")
    print("Your guess log:",SB)
