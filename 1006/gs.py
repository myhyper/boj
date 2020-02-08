import sys, os
sys.setrecursionlimit(1000000)
DEBUG = True
#DEBUG = False
if DEBUG:
    f = open('input.txt', 'r')
else:
    f = sys.stdin
def init_memo():
    #Memoization array
    aType = [0 for _ in range(N+1)] #the memoization array to store the least number of group count in Type a
    bType = [0 for _ in range(N)] #the memoization array to store the least number of group count in Type b
    cType = [0 for _ in range(N)] #the memoization array to store the least number of group count in Type c
    return aType, bType, cType
def toGroup_ohneCircular(start_index):
    for i in range(start_index, N):
        #1. None of adjacent areas
        aTypeMemo[i+1] = min(bTypeMemo[i]+1, cTypeMemo[i]+1)
        #2. Occupy one more adjacent area
        if EnemyMap[0][i]+EnemyMap[1][i] <= W:
            aTypeMemo[i+1] = min(aTypeMemo[i+1], aTypeMemo[i]+1)
        if i > 0 and (EnemyMap[0][i-1]+EnemyMap[0][i] <= W) and (EnemyMap[1][i-1]+EnemyMap[1][i] <= W):
            aTypeMemo[i+1] = min(aTypeMemo[i+1], aTypeMemo[i-1]+2)
        #3. Calculate bType & cType
        if i < N-1:
            #to count bType for index
            bTypeMemo[i+1] = aTypeMemo[i+1]+1
            if EnemyMap[0][i]+EnemyMap[0][i+1] <= W:
                bTypeMemo[i+1] = min(bTypeMemo[i+1], cTypeMemo[i]+1)
            #to count cType for index
            cTypeMemo[i+1] = aTypeMemo[i+1]+1
            if EnemyMap[1][i]+EnemyMap[1][i+1] <= W:
                cTypeMemo[i+1] = min(cTypeMemo[i+1], bTypeMemo[i]+1)
T = int(f.readline().strip())
while(T > 0):
    T-=1
    N, W = map(int,f.readline().split())
    EnemyMap = [list(map(int, f.readline().split())) for _ in range(2)]
    ANSWER = 20200110
    #----------------------------------Type spec----------------------------------#
    #aType.[n+1] : Assign troups to all location between Row[0]/Col[0~n] and Row[1]/Col[0~n]
    #bType.[n]   : Assign troups to all location between Row[0]/Col[0~n] and Row[1]/Col[0~n-1]
    #cType.[n]   : Assign troups to all location between Row[0]/Col[0~n-1] and Row[1]/Col[0~n]
    #----------------------------------##########---------------------------------#
    #Memo initialization
    aTypeMemo, bTypeMemo, cTypeMemo = init_memo()
    #Base case for ohneCircular map
    aTypeMemo[0] = 0
    bTypeMemo[0] = 1
    cTypeMemo[0] = 1
    #Get answer for ohneCircular map
    toGroup_ohneCircular(0)
    ANSWER = min(ANSWER, aTypeMemo[N])
    #---------------------------3 Images in case of Circular Type-----------------#
    #Type 1.     : node at Row[0]/Col[0] & note at Row[0]/Col[n-1] are connected
    #Type 2.     : node at Row[1]/Col[0] & note at Row[1]/Col[n-1] are connected
    #Type 3.     : Both 2 nodes stated above Type1 and Type2 are all respectively connected
    #----------------------------------##########---------------------------------#
    #Circular_Scenario_Type 1.
    if N>1 and EnemyMap[0][0]+EnemyMap[0][N-1] <= W:
        #initialization
        #Memo initialization
        aTypeMemo, bTypeMemo, cTypeMemo = init_memo()
        #Base case
        aTypeMemo[1] = 1
        bTypeMemo[1] = 2
        if EnemyMap[1][0]+EnemyMap[1][1] <= W:
            cTypeMemo[1] = 1
        else:
            cTypeMemo[1] = 2
        #Get answer for ohneCircular map
        toGroup_ohneCircular(1)
        ANSWER = min(ANSWER, cTypeMemo[N-1]+1)
    #Circular_Scenario_Type 2.
    if N>1 and EnemyMap[1][0]+EnemyMap[1][N-1] <= W:
        #initialization
        #Memo initialization
        aTypeMemo, bTypeMemo, cTypeMemo = init_memo()
        #Base case
        aTypeMemo[1] = 1
        if EnemyMap[0][0]+EnemyMap[0][1] <= W:
            bTypeMemo[1] = 1
        else:
            bTypeMemo[1] = 2
        cTypeMemo[1] = 2
        #Get answer for ohneCircular map
        toGroup_ohneCircular(1)
        ANSWER = min(ANSWER, bTypeMemo[N-1]+1)
    #Circular_Scenario_Type 3.
    if N>1 and EnemyMap[0][0]+EnemyMap[0][N-1] <= W and EnemyMap[1][0]+EnemyMap[1][N-1] <= W:
        #initialization
        #Memo initialization
        aTypeMemo, bTypeMemo, cTypeMemo = init_memo()
        #Base case
        aTypeMemo[1] = 0
        bTypeMemo[1] = 1
        cTypeMemo[1] = 1
        #Get answer for ohneCircular map
        toGroup_ohneCircular(1)
        ANSWER = min(ANSWER, aTypeMemo[N-1]+2)
    print(ANSWER)
f.close()