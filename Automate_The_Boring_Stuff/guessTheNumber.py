# This is a guess the number game.
import random, sys
from varname import nameof

secretnum = random.randint(1,20)
randfrom = random.randint(1,3)
randto = random.randint(8,10)
print("I am thinking of a number from ",nameof(randfrom),":",randfrom," to ",nameof(randto),":",randto," .")

print("How many times would you like to guess:")
guess = 0
numberofguesses = int(input())
for guessesmade in range(numberofguesses):
    print("Take a guess: ")
    guess = int(input())
    if guess > secretnum:
        print("Your number is higher..")
    elif guess < secretnum:
        print("Your number is lower...")
    else:
        break
if guess == secretnum:
    print("Good Job ",nameof(guessesmade)," : ",guessesmade)
    sys.exit(1)
else:
    print("Try Again ",nameof(secretnum)," : ",secretnum)
    sys.exit(2)



