import sys, os
sys.setrecursionlimit(1000000)

#Global variables
DEBUG = True
#DEBUG = False
OUT_OF_BORDER = -1
UNKNOWN = 0
ROOT = -9

#Check if it belongs to valid territory
def check_valid(x, y):
    return land_map[x][y] != OUT_OF_BORDER

#DFS Chart Function
def toChart(x, y):
    if numberOfWays_map[x][y] > UNKNOWN:
        return numberOfWays_map[x][y]
    else:
        for x1 in range(-1, 2):
            for y1 in range(-1, 2):
                if (abs(x1)^abs(y1) == True) and (check_valid(x + x1, y + y1) == True):
                    if (close_map[x][y] == UNKNOWN):
                        if (x + x1 == height) and (y + y1 == width):
                            numberOfWays_map[x][y] += 1
                        else:
                            if land_map[x + x1][y + y1] < land_map[x][y]:
                                numberOfWays_map[x][y] += toChart(x + x1, y + y1)   
                                #print("\t{}, {} = {}".format(x,y,numberOfWays_map[x][y]))           
        return numberOfWays_map[x][y]



#BFS Chart Function
def toChart_NonRecursive(x, y):
    #Initialization
    node = list()
    parent = list()
    junc = dict()
    junctions, x_temp, y_temp, x_temp_next, y_temp_text, x_temp_previous, y_temp_previous, add = 0, 0, 0, 0, 0, 0, 0, 0
    
    #root insertion
    node.append([x, y])
    parent.append([ROOT, ROOT])

    while len(node) > 0:
        all_j = 0
        junctions = 0
        add = 0
        coor_x,coor_y = node[len(node) - 1]
        for x1 in range(-1, 2):
            for y1 in range(-1, 2):
                if (abs(x1)^abs(y1) == True) and (check_valid(coor_x + x1, coor_y + y1) == True) and (land_map[coor_x + x1][coor_y + y1] < land_map[coor_x][coor_y]):
                    all_j += 1
                    if ((coor_x + x1 == height) and (coor_y + y1 == width)) or (numberOfWays_map[coor_x + x1][coor_y + y1] > 0):
                        if numberOfWays_map[coor_x + x1][coor_y + y1] > 0:
                            add = add + numberOfWays_map[coor_x + x1][coor_y + y1]
                        else:
                            add = add + 1
                    else:
                        junctions += 1                                                        
                        node.append([coor_x + x1, coor_y + y1])
                        parent.append([coor_x, coor_y])     
        junc["{0},{1}".format(coor_x, coor_y)] = junctions #Record sum of junctions

        if (add > 0) or (junctions == 0):
            x_temp, y_temp = coor_x, coor_y
            x_temp_previous, y_temp_previous = UNKNOWN, UNKNOWN
            numberOfWays_map[x_temp][y_temp] += add
            while True:              
                x_temp_next, y_temp_next = parent[node.index([x_temp, y_temp])]
                if x_temp_previous != UNKNOWN:
                    junc["{0},{1}".format(x_temp, y_temp)] -= 1
                    numberOfWays_map[x_temp][y_temp] += numberOfWays_map[x_temp_previous][y_temp_previous]
                if junc.get("{0},{1}".format(x_temp, y_temp)) <= 0:
                    del parent[node.index([x_temp, y_temp])]
                    del node[node.index([x_temp, y_temp])]
                    if x_temp_next == ROOT:
                        break
                    x_temp_previous, y_temp_previous = x_temp, y_temp   
                    x_temp, y_temp = x_temp_next, y_temp_next
                else:
                    junc["{0},{1}".format(x_temp, y_temp)] -= 1
                    break

    return numberOfWays_map[x][y]

#Load data from input.txt
if DEBUG:
    #os.chdir("/home/geonsang/Documents/Python/Algorithm/DecendingRoad_#1520/")
    f = open("input5.txt", 'r')
else:
    f = sys.stdin

while True:
    line = f.readline()
    if not line:
        break
    
    #Assign width and height from input
    height, width = map(int, line.split())

    #Initialize a list to load map data (including 1 margin space)
    land_map = [[OUT_OF_BORDER for _ in range(0, width + 2)] for _ in range(0, height + 2)]
    close_map = [[UNKNOWN for _ in range(0, width + 2)] for _ in range(0, height + 2)]
    numberOfWays_map = [[UNKNOWN for _ in range(0, width + 2)] for _ in range(0, height + 2)]
    Count = 0
    
    #Assign input height data from input
    for h in range(1, height + 1):
        width_buffer = list(map(int, f.readline().split()))
        for w in range(1, width + 1):
            land_map[h][w] = width_buffer[w - 1]
    
    #Go to search
    # #Recursive call
    Count = toChart(1, 1)

    #Non-Recursive Call
    #Count = toChart_NonRecursive(1, 1)
    print(Count)

f.close()