from varname import nameof
import random,sys

def getTOSS(num):
    if num == 1:
        return "Heads"
        #sys.exit(1)
    elif num == 2:
        return "Tails"
        #sys.exit(1)

r = random.randint(1,2)
fortune = getTOSS(r)

print(fortune)