# This is a guess the number game.
import random, sys
from varname import nameof


randfrom = random.randint(1,3)
randto = random.randint(8,10)

secretnum = random.randint(randfrom,randto)

debugmode = {
    "Status":"Active"
}
print("Enter Y for DEBUG Mode N for Normal (Default: Active):",end=" ")
try:
    inputvar1 = input()
except KeyboardInterrupt:
    print("Ending due to Interrupt!")
    sys.exit(2)

if inputvar1 == "Y" or inputvar1 == "y":
    debugmode["Status"] = "Active"
elif inputvar1 == "N" or inputvar1 == "n":
    debugmode["Status"] = "Off"
else:
    print("BAD Choice.... Ending")
    sys.exit(2)

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



