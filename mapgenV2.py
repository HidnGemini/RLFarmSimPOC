import random as rng
def mapgen(grid_size, farm_size):
    total_size = grid_size + farm_size
    map = [[0 for i in range(total_size)] for i in range(total_size)]
    map = addCenteredFarm(map, farm_size)
    return map
def addCenteredFarm(map, farm_size):
    center = len(map) // 2 # CENTER OF MAP
    half_size = farm_size // 2 # HALF OF FARM SIZE
    # ADDS OUTLINE TO FARM
    for i in range(farm_size):
        map[center+i-half_size][center-half_size] = 3
        map[center+i-half_size][center+half_size] = 3
        map[center-half_size][center+i-half_size] = 3
        map[center+half_size][center+i-half_size] = 3
    # ADDS FARMABLE TILES
    for r in range(farm_size-2):
        for c in range(farm_size-2):
            map[r-1+center][c-1+center] = 1
    return map
def printMap(baseMap):
    glyphs = '/_..$'
    for r in range(len(baseMap)):
        for c in range(len(baseMap[0])):
            print(glyphs[baseMap[r][c]], end=' ')
        print()
if __name__ == '__main__':
    map = mapgen(16, 5)
    printMap(map)