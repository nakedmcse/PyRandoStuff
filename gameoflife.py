# Game of life
import random

# Cell class
class GOLCell:
    def __init__(self,x,y,live):
        self.x = x
        self.y = y
        self.live = live

    # Get live neighbor cells
    def liveNeighborCount(self,arr):
        yStart = self.y if self.y-1 < 0 else (self.y - 1)
        yEnd = self.y if self.y+1 > len(arr) else (self.y + 1)
        xStart = self.x if self.x-1 < 0 else (self.x -1)
        xEnd = self.x if (self.x+1) > len(arr[self.y]) else (self.x+1)

        lives = -1 if self.live else 0
        for i in range(yStart,yEnd):
            lives += sum(1 for x in arr[i][xStart:xEnd] if x.live)
        return lives
    
    # Spawn next generation of this cell
    def spawnNext(self,arr):
        liveNeighbors = self.liveNeighborCount(arr)

        if (not self.live and liveNeighbors == 3):
            # Dead + 3 live neighbors => resurrected
            return GOLCell(self.x,self.y,True)
        
        if (self.live):
            match(liveNeighbors):
                case 1:
                    #1 neighbor only - cell dies
                    return GOLCell(self.x,self.y,False)
                case 2 | 3:
                    #2-3 neighbors - cell lives
                    return GOLCell(self.x,self.y,True)
                case _:
                    #>3 neighbors - cell dies
                    return GOLCell(self.x,self.y,False)
                
        #catch all for no matching rules - cell continues as is
        return GOLCell(self.x,self.y,self.live)

# Render array to console
def renderGeneration(arr):
    for i in arr:
        outline = ''.join('*' if curelt.live else '-' for curelt in i)
        print(outline)

# Check to see if colony dead
def colonyDead(arr):
    for i in arr:
        if any(e.live for e in i):
            return False
    return True

# Init system
currentGeneration = []
generationNumber = 1

for x in range(20):
    currentRow = []
    for y in range(20):
        currentRow.append(GOLCell(x,y,random.random()>0.5))
    currentGeneration.append(currentRow)

# Loop
while True:
    print(f"Generation: {generationNumber}")
    renderGeneration(currentGeneration)

    # Generate next generation
    nextGen = []
    for currentRow in currentGeneration:
        nextGen.append([cell.spawnNext(currentGeneration) for cell in currentRow])
    generationNumber += 1
    currentGeneration = nextGen

    # Exit loop if colony dies
    if colonyDead(currentGeneration):
        print("COLONY DEAD")
        break;