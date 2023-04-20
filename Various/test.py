rows = [0,1,2]
r = {i:[] for i in rows}

cols = [[1, 5, 2, 3], [4, 6, 10, 7], [8, 0, 9, 11]]

idealOrder = {"11": (2,3), "7": (1,3), "3": (0,3), "10": (2,2), "9": (2,1), "8": (2,0), "6": (1,2), "2": (0,2), "1": (0,1), "5": (1,1), "4": (1,0), "0": (0,0) }

# Find position based on number

def searchPos(lst, item):
    for i in range(len(lst)):
        part = lst[i]
        for j in range(len(part)):
            if part[j] == item: return (i, j)
    return None

# A tile can have a number, a position and a status.

class generalTile:
        
    def __init__(self, number, currentPlace, idealPlace):
        self.number = number
        self.currentPlace = currentPlace
        self.status = "move"
        self.idealPlace = idealPlace

        initList = list(currentPlace)
        u, d, r, l = initList, initList, initList, initList
        u[0] = initList[0]-1
        self.uPos = tuple(u)
 
        d[0] = initList[0]+1
        self.dPos = tuple(d)
        r[1] = initList[1]+1
        self.rPos = tuple(r)
        l[1] = initList[1]-1
        self.lPos = tuple(l)
 
# List of 11 tiles
listOfTiles = [generalTile(i, searchPos(cols, i), idealOrder[str(i)]) for i in range(1, 12)]

listOfLocked = []

for tile in listOfTiles:
  if tile.currentPlace == (2,2):
    print(tile.number)

  listOfLocked.append(tile.status)
