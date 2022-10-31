import random as rng
import time as t
import mapgen as mg
import monsterfunctions as mf
import os
import math
import getch
import platform
class bcolors:
    GRAY = '\033[97m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    SMALLSEED = '\033[32m'
    POWERSEED = '\033[31m'
    HEALTHSEED = '\033[91m'
    MONEYSEED = '\033[93m'
    BIGSEED = '\033[92m'
    GIANTSEED = '\033[95m'
    monsterColors = [
        YELLOW,
        SMALLSEED,
        CYAN
    ]
    plantColors = [
        SMALLSEED,
        POWERSEED,
        HEALTHSEED,
        MONEYSEED,
        BIGSEED,
        GIANTSEED
    ]
class WumpusGame():
    def __init__(self, outerSize, farmSize):
        self.wumpusboard = mg.mapGen(outerSize,farmSize)
        self.overlay = [[0 for i in range(len(self.wumpusboard))] \
        for i in range(len(self.wumpusboard[0]))]
        #self.inventory = [0 for i in range(6)]
        self.inventory = [1,2,3,4,5,6]
        self.walkable = [1,2,3]
        playerR = int(len(self.wumpusboard)//2)
        playerC = int(len(self.wumpusboard[0])//2)
        self.coords = [playerR, playerC]
        self.playing = True
        self.monsterCount = 0
        self.config()
        self.createMonster(1)
        self.recents = [0 for i in range(3*self.monsterCount)]
        self.clear = 'clear' if platform.system != "Windows" else 'cls'
        os.system(self.clear)
    def config(self):
        self.mapGlyphs = ' _..'
        self.monsterGlyphs = ' &%'
        self.plantGlyphs = ',</|'
        self.held = 0
        self.itemNames = {
        0:'Nothing',
        1:'Small Seed',
        2:'Power Seed',
        3:'Health Seed',
        4:'Money Seed',
        5:'Big Seed',
        6:'GIANT SEED',
        7:'Damaged Battle Hoe',
        8:'Battle Hoe',
        9:'Flaming Battle Hoe',
        10:'Super Battle Hoe',
        }
    def display2d(self):
        for r in range(len(self.wumpusboard)):
            for c in range(len(self.wumpusboard[0])):
                if r == self.coords[0] and c == self.coords[1]:
                    print(bcolors.PURPLE,end='')
                    print('O',end=' ')
                elif self.overlay[r][c] == 0:
                    item = self.wumpusboard[r][c]
                    print(bcolors.GRAY,end='')
                    print(self.mapGlyphs[item],end=' ')
                else:
                    if self.overlay[r][c] < len(self.monsterGlyphs):
                        item = self.overlay[r][c]
                        print(bcolors.monsterColors[item-1],end='')
                        print(self.monsterGlyphs[item],end=' ')
                    else:
                        item = self.overlay[r][c] - len(self.monsterGlyphs)
                        print(bcolors.plantColors[(item//4)-1],end='')
                        print(self.plantGlyphs[item%len(self.plantGlyphs)],end=' ')
            print()
    def displayinv(self):
        itemGlyphs = ' ....o0/|||'
        print('SLOT : SPRITE : NAME')
        for i in range(len(self.inventory)):
            item = self.inventory[i]
            if item != 0:
                print(f'{i} : {itemGlyphs[item]} : {self.itemNames[item]}')
    def addToInv(self, itemID):
        try:
            itemID = int(itemID)
            for item in range(len(self.inventory)):
                if self.inventory[item] == 0:
                    self.inventory[item] = int(itemID)
                    print('DONE')
                    break
        except ValueError:
            print('ItemID must be INT!')
    def createMonster(self, type):
        self.monsterCount += 1
        wumpusR = int(len(self.wumpusboard)/2)
        wumpusC = int(len(self.wumpusboard[0])/2)
        while self.wumpusboard[wumpusR][wumpusC] != 2:
            wumpusR = rng.randrange(0,len(self.wumpusboard))
            wumpusC = rng.randrange(0,len(self.wumpusboard[1]))
        self.overlay[wumpusR][wumpusC] = type
    def newFloor(self, outerSize, farmSize):
        farmTiles = [1,3]
        newboard = mg.mapGen(outerSize,farmSize)
        for row in range(len(self.wumpusboard)):
            for col in range(len(self.wumpusboard[0])):
                if newboard[row][col] in farmTiles:
                    pass
                else:
                    self.overlay[row][col] = 0
        self.wumpusboard = newboard
        self.createMonster(2)
        self.createMonster(1)
    def plant(self, plant):
        mGl = len(self.monsterGlyphs)
        plantStage = (plant*4)+mGl
        if self.wumpusboard[self.coords[0]][self.coords[1]] == 1:
            self.overlay[self.coords[0]][self.coords[1]] = plantStage
    def growPlants(self):
        for r in range(len(self.overlay)):
            for c in range(len(self.overlay[0])):
                item = self.overlay[r][c]
                if item > len(self.monsterGlyphs)-1:
                    growth = rng.randrange(1,4)
                    if growth == 3 and \
                    (self.overlay[r][c]-len(self.monsterGlyphs))%4 != 3:
                        self.overlay[r][c] += 1
    def main(self):
        while self.playing:
            os.system(self.clear)
            self.display2d()
            #inp = input('Input: ')
            inp = getch.getch()
            if inp == 'a':
                self.coords[1] -= 1 if self.coords[1] > 0 and \
                self.wumpusboard[self.coords[0]][self.coords[1]-1] \
                in self.walkable else 0
            if inp == 'd':
                self.coords[1] += 1 if self.coords[1] < \
                len(self.wumpusboard[1])-1 and \
                self.wumpusboard[self.coords[0]][self.coords[1]+1] \
                in self.walkable else 0
            if inp == 'w':
                self.coords[0] -= 1 if self.coords[0] > 0 and \
                self.wumpusboard[self.coords[0]-1][self.coords[1]] \
                in self.walkable else 0
            if inp == 's':
                self.coords[0] += 1 if self.coords[0] < \
                len(self.wumpusboard)-1 and \
                self.wumpusboard[self.coords[0]+1][self.coords[1]] \
                in self.walkable else 0
            if inp == 'i':
                os.system(self.clear)
                print("INVENTORY:")
                self.displayinv()
                input('Continue...')
            if inp == 'h':
                os.system(self.clear)
                print(f'Current held item: {self.itemNames[self.inventory[self.held]]}')
                print('Hold what? (ENTER NUMBER)')
                self.displayinv()
                item = input('Enter SLOT Number: ')
                try:
                    item = int(item)
                    if self.inventory[item] != 0:
                        self.held = item
                    else:
                        print('SLOT must have an item in it')
                except ValueError:
                    print('SLOT must be INT!')
            if inp == 'p':
                if self.inventory[self.held] in [1,2,3,4,5,6]:
                    self.plant(self.inventory[self.held])
                    self.inventory[self.held] = 0
            if inp == '#':
                inp = input("What Command? ")
                if inp == 'nf':
                    self.coords[0] = int(len(self.wumpusboard)//2)
                    self.coords[1] = int(len(self.wumpusboard[0])//2)
                    self.monsterCount = 0
                    self.newFloor(16,5)
                if inp == 'gi':
                    item = input('ItemID: ')
                    self.addToInv(item)
                    t.sleep(1)
                if inp == 'q':
                    print('game quit with q')
                    self.playing = False
            self.AI()
            self.growPlants()
            t.sleep(0.1)
    def AI(self):
        for row in range(len(self.wumpusboard)):
            for col in range(len(self.wumpusboard[0])):
                if self.overlay[row][col] == 1:
                    self.wumpusAI(row,col)
                if self.overlay[row][col] == 2:
                    self.goblinAI(row,col)
    def wumpusAI(self,row,col):
        distancefromplayer = math.sqrt((abs(row-self.coords[0])+1)**2 + \
        (abs(col-self.coords[1])+1)**2)
        thought = rng.randrange(1,101)
        # WUMPUS MOVEMENT
        if thought <= 70:
            self.overlay[row][col] = 0
            # WANDERING
            if distancefromplayer > 7:
                mf.wanderMove(1,1,self.wumpusboard,self.overlay,row,col)
            # CHASING PLAYER
            else:
                self.recents.append((row,col))
                self.recents.pop(0)
                desireable = [0,0,0,0]
                options = [
                    (row-1,col),
                    (row+1,col),
                    (row,col-1),
                    (row,col+1)
                ]
                for i in range(len(options)):
                    desireable[i] = \
                    math.sqrt((abs(options[i][0]-self.coords[0])+1)**2 + \
                    (abs(options[i][1]-self.coords[1])+1)**2) if \
                    self.wumpusboard[options[i][0]][options[i][1]] \
                    == 2 else 100000
                smallval = 100000
                for i in range(len(desireable)):
                    if i == 0 or desireable[i] < smallval:
                        if options[i] not in self.recents:
                            small = i
                            smallval = desireable[small]
                try:
                    self.overlay[options[small][0]][options[small][1]] = 1
                except UnboundLocalError:
                    self.overlay[row][col] = 1
    def goblinAI(self,row,col):
        distancefromplayer = math.sqrt((abs(row-self.coords[0])+1)**2 + \
        (abs(col-self.coords[1])+1)**2)
        thought = rng.randrange(1,101)
        # 1 TILE GOBLIN MOVEMENT
        if thought <= 30:
            self.overlay[row][col] = 0
            # WANDERING
            if distancefromplayer > 7:
                mf.wanderMove(1,2,self.wumpusboard,self.overlay,row,col)
            # CHASING PLAYER
            else:
                self.recents.append((row,col))
                self.recents.pop(0)
                desireable = [0,0,0,0]
                options = [
                    (row-1,col),
                    (row+1,col),
                    (row,col-1),
                    (row,col+1)
                ]
                for i in range(len(options)):
                    desireable[i] = \
                    math.sqrt((abs(options[i][0]-self.coords[0])+1)**2 + \
                    (abs(options[i][1]-self.coords[1])+1)**2) if \
                    self.wumpusboard[options[i][0]][options[i][1]] \
                    == 2 else 100000
                smallval = 100000
                for i in range(len(desireable)):
                    if i == 0 or desireable[i] < smallval:
                        if options[i] not in self.recents:
                            small = i
                            smallval = desireable[small]
                try:
                    self.overlay[options[small][0]][options[small][1]] = 2
                except UnboundLocalError:
                    self.overlay[row][col] = 2
        # 2 TILE GOBLIN MOVEMENT
        if thought <= 60 and thought > 30:
            self.overlay[row][col] = 0
            # WANDERING
            if distancefromplayer > 7:
                mf.wanderMove(2,2,self.wumpusboard,self.overlay,row,col)

if __name__ == '__main__':
    wumpusGame = WumpusGame(16,5)
    wumpusGame.main()
