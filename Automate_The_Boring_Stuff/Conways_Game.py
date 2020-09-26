import sys,random,os,platform,time, copy
from varname import nameof

# "alive" or "dead"
# living alive has 2 or 3 living neighbors it continues to live
# dead square has exactly 3 living neighbors it comes alive next step
width = 60
height = 20

print(nameof(width),":",width,sep="\t")
print(nameof(height),":",height,sep="\t")

# Create a list of cells
nextcells = []

for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0,1) == 0:
            column.append("#")
        else:
            column.append(" ")
    nextcells.append(column)
#try:
while True:
    print("\n\n\n\n")
    currentcells = copy.deepcopy(nextcells)

    for y in range(height):
        for x in range(width):
            print(currentcells[x][y], end="")
        print()

    for x in range(width):
        for y in range(height):
            leftcoord = (x-1)%width
            rightcoord = (x+1)%width
            abovecoord = (y-1)%height
            belowcoord = (y+1)%height

            numneighbours = 0
            if currentcells[leftcoord][abovecoord] == "#":
                numneighbours += 1
            if currentcells[x][abovecoord] == "#":
                numneighbours += 1
            if currentcells[leftcoord][y] == "#":
                numneighbours += 1
            if currentcells[rightcoord][abovecoord] == "#":
                numneighbours += 1
            if currentcells[rightcoord][y] == "#":
                numneighbours += 1
            if currentcells[leftcoord][belowcoord] == "#":
                numneighbours += 1
            if currentcells[x][belowcoord] == "#":
                numneighbours += 1
            if currentcells[rightcoord][belowcoord] == "#":
                numneighbours += 1
            if currentcells[x][y] == "#" and (numneighbours == 2 or numneighbours == 3):
                nextcells[x][y] = "#"
            elif currentcells[x][y] == " " and numneighbours == 3:
                nextcells[x][y] = "#"
            else:
                nextcells[x][y] = " "
    time.sleep(1)
#except KeyboardInterrupt:
#    print("END!!")
 #   sys.exit(1)
