import random,math,os,time
glyphs = '.0&_'
def mapPrint(map):
    for row in map:
        for item in row:
            print(glyphs[item],end=' ')
        print()
def updatemonster(m,p):
    map[m[0]][m[1]] = 0
    recents.append(m)
    recents.pop(0)
    desireable = [0,0,0,0]
    options = [(m[0]-1,m[1]),(m[0]+1,m[1]),(m[0],m[1]-1),(m[0],m[1]+1)]
    for i in range(len(options)):
        desireable[i] = math.sqrt((abs(options[i][0]-p[0])+1)**2 + \
        (abs(options[i][1]-p[1])+1)**2) if map[options[i][0]][options[i][1]] \
        == 0 else 100000
    smallval = 100000
    for i in range(len(desireable)):
        if i == 0 or desireable[i] < smallval:
            if options[i] not in recents:
                small = i
                smallval = desireable[small]
    return options[small]
map = [[0 for i in range(15)] for i in range(15)]
playerpos = 7,7
#monsterpos = random.randrange(15),random.randrange(15)
monsterpos = 0,7
recents = [0 for i in range(3)]
map[playerpos[0]][playerpos[1]] = 1
map[2][7] = 3
map[2][6] = 3
map[2][8] = 3
map[5][4] = 3
map[5][6] = 3
map[5][5] = 3
for i in range(20):
    os.system('cls')
    map[monsterpos[0]][monsterpos[1]] = 2
    mapPrint(map)
    monsterpos = updatemonster(monsterpos,playerpos)
    time.sleep(0.2)
