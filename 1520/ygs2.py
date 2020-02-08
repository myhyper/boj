import sys

#Global variables
#DEBUG = True
DEBUG = False
OUT_OF_BORDER = -1
UNKNOWN = 0
ROOT = -9

#Check if it belongs to valid territory
def check_valid(y, x):
    return land_map[y][x] != OUT_OF_BORDER

#DFS Chart Function
def toChart(y, x):
    if numberOfWays_map[y][x] != UNKNOWN:
        return numberOfWays_map[y][x]
    else:
        for y1 in range(-1, 2):
            for x1 in range(-1, 2):
                if (abs(x1)^abs(y1) == True) and (check_valid(y + y1, x + x1) == True):
                    if (y + y1 == height) and (x + x1 == width):
                        numberOfWays_map[y + y1][x + x1] = 1
                        return 1
                    else:
                        if land_map[y + y1][x + x1] < land_map[y][x]:
                            numberOfWays_map[y][x] = numberOfWays_map[y][x] + toChart(y + y1, x + x1)                    
        return numberOfWays_map[y][x]

#BFS Chart Function
def toChart_NonRecursive(y, x):
    #Initialization
    node = list()
    parent = list()
    junc = dict()
    junctions, x_temp, y_temp, x_temp_next, y_temp_text, x_temp_previous, y_temp_previous, add = 0, 0, 0, 0, 0, 0, 0, 0
    
    #root insertion
    node.append([y, x])
    parent.append([ROOT, ROOT])

    while len(node) > 0:
        junctions = 0
        add = 0
        coor_y,coor_x = node[len(node) - 1]
        for y1 in range(-1, 2):
            for x1 in range(-1, 2):
                if (abs(x1)^abs(y1) == True):
                    if (check_valid(coor_y + y1, coor_x + x1) == True):
                        if (land_map[coor_y + y1][coor_x + x1] < land_map[coor_y][coor_x]):
                            junctions += 1
                            if ((coor_x + x1 == width) and (coor_y + y1 == height)) or (numberOfWays_map[coor_y + y1][coor_x + x1] > 0):
                                if numberOfWays_map[coor_y + y1][coor_x + x1] > 0:
                                    add = add + numberOfWays_map[coor_y + y1][coor_x + x1]
                                else:
                                    add = add + 1
                            else:
                                #print(" => (x={}, y={})".format(coor_x, coor_y))
                                node.append([coor_y + y1, coor_x + x1])
                                parent.append([coor_y, coor_x])
            
        print(" PUT => (y={}, x={})".format(coor_y, coor_x))
        junc[(coor_y, coor_x)] = junctions #Record sum of junctions
        
        if add > 0:
            x_temp, y_temp = coor_x, coor_y
            x_temp_previous, y_temp_previous = UNKNOWN, UNKNOWN
            numberOfWays_map[y_temp][x_temp] += add
            while True: 
                print(" GET => (y={}, x={})".format(y_temp, x_temp))
                junc[(y_temp, x_temp)] -= 1
                x_temp_next, y_temp_next = parent[node.index([y_temp, x_temp])]
                if x_temp_previous != UNKNOWN:
                    numberOfWays_map[y_temp][x_temp] += numberOfWays_map[y_temp_previous][x_temp_previous]
                if junc.get((y_temp, x_temp)) <= 0:
                    del parent[node.index([y_temp, x_temp])]
                    del node[node.index([y_temp, x_temp])]
                    if x_temp_next == ROOT:
                        break
                    x_temp_previous, y_temp_previous = x_temp, y_temp   
                    x_temp, y_temp = x_temp_next, y_temp_next
                else:
                    break

    return numberOfWays_map[y][x]

#Load data from input.txt
if DEBUG:
    #os.chdir("/home/geonsang/Documents/Python/Algorithm/DecendingRoad_#1520/")
    f = open("input.txt", 'r')
else:
    f = sys.stdin

while True:
    line = f.readline()
    if not line:
        break
    
    #Assign width and height from input
    height, width = map(int, line.split())
    # if height <= 0 or width <= 0:
    #     break

    #Initialize a list to load map data (including 1 margin space)
    land_map = [[OUT_OF_BORDER for _ in range(0, width + 2)] for _ in range(0, height + 2)]
    numberOfWays_map = [[UNKNOWN for _ in range(0, width + 2)] for _ in range(0, height + 2)]
    Count = 0
    
    #Assign input height data from input
    for h in range(1, height + 1):
        width_buffer = list(map(int, f.readline().split()))
        for w in range(1, width + 1):
            land_map[h][w] = width_buffer[w - 1]
    
    #Go to search
    # #Recursive call
    # Count = toChart(1, 1)

    #Non-Recursive Call
    Count = toChart_NonRecursive(1, 1)
    print(Count)
    break

f.close()