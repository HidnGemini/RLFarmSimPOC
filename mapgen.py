import random as rng
def mapGen(l, f):
    map = [[0 for i in range(l+f)] for i in range(l+f)]
    mapCenter = (l+f)//2
    # PLACES FARM ROOM
    half = f//2
    for r in range(l+f):
        for c in range(l+f):
            if abs(r - mapCenter) < half and \
            abs(c - mapCenter) < half:
                map[r][c] = 1
            if (abs(r - mapCenter) == half and \
            abs(c - mapCenter) <= half) or \
            (abs(r - mapCenter) <= half and \
            abs(c - mapCenter) == half):
                map[r][c] = 3
    # GENERATES LOCATION OF DUNGEON ROOMS
    setLocations = (3*len(map)//16, 13*len(map[0])//16)
    roomLocations = []
    offsetBound = int(l/4)
    for r in setLocations:
        for c in setLocations:
            offc = rng.randrange(0,offsetBound) - int(offsetBound/2)
            offr = rng.randrange(0,offsetBound) - int(offsetBound/2)
            roomLocations.append([(r+offr),(c+offc)])
    # GENERATES HALLWAYS
    doneHalls = []
    hall = rng.randrange(1,6)
    for i in range(3):
        dir = rng.randrange(1,5)
        while dir in doneHalls:
            dir = rng.randrange(1,5)
        doneHalls.append(dir)
        if dir < 3:
            if dir == 1:
                avg = int((roomLocations[0][0] + roomLocations[1][0]) / 2)
                if hall == 1 or 5:
                    for i in range(avg, int(l/2)):
                        map[i][mapCenter] = 2
                for i in range(roomLocations[0][1],roomLocations[1][1]):
                    map[avg][i] = 2
            if dir == 2:
                avg = int((roomLocations[2][0] + roomLocations[3][0]) / 2)
                if hall == 2:
                    for i in range(int((l/2)+f), avg):
                        map[i][mapCenter] = 2
                for i in range(roomLocations[2][1],roomLocations[3][1]):
                    map[avg][i] = 2
        if dir >= 3:
            if dir == 3:
                avg = int((roomLocations[0][1] + roomLocations[2][1]) / 2)
                if hall == 3 or 5:
                    for i in range(avg, int(l/2)):
                        map[mapCenter][i] = 2
                for i in range(roomLocations[0][0],roomLocations[2][0]):
                    map[i][avg] = 2
            if dir == 4 or 7:
                avg = int((roomLocations[1][1] + roomLocations[3][1]) / 2)
                if hall == 4:
                    for i in range(int((l/2)+f), avg):
                        map[mapCenter][i] = 2
                for i in range(roomLocations[1][0],roomLocations[3][0]):
                    map[i][avg] = 2
    # GENERATES DUNGEON ROOMS
    for room in roomLocations:
        roomSizeRN = rng.randrange(-4, -2)
        roomSizeRP = rng.randrange(2, 4)
        roomSizeCN = rng.randrange(-4, -2)
        roomSizeCP = rng.randrange(2, 4)
        for rawR in range(roomSizeRN,roomSizeRP):
            for rawC in range(roomSizeCN,roomSizeCP):
                r = rawR + room[0] if rawR + room[0] > 0 and \
                rawR + room[0] < len(map) else 0
                c = rawC + room[1] if rawC + room[1] > 0 and \
                rawC + room[1] < len(map) else 0
                map[r][c] = 2
    return map
def printMap(baseMap):
    glyphs = ' _..$'
    for r in range(len(baseMap)):
        for c in range(len(baseMap[0])):
            print(glyphs[baseMap[r][c]], end=' ')
        print()
if __name__ == '__main__':
    map = mapGen(16, 5)
    printMap(map)
