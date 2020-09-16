from varname import nameof
import random

def getTOSS(num):
    if num == 1:
        return "Heads"
    elif num == 2:
        return "Tails"

r = random.randint(1,2)
fortune = getTOSS(r)

print(fortune)