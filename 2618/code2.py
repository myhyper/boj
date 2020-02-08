import sys
sys.setrecursionlimit(100000)
DEBUG = True
# DEBUG = False
PATROL_CAR_A = 1
PATROL_CAR_B = 2
if DEBUG:
    f = open("input.txt", 'r')
else:
    f = sys.stdin
def calc_dist(from_, to_):
    x1, y1 = from_
    x2, y2 = to_
    return abs(x1-x2) + abs(y1-y2)
def distance(n, prev_pick_A, prev_pick_B):
    if n>=E:
        return 0
    if memo[prev_pick_A][prev_pick_B]!=-1:
        return memo[prev_pick_A][prev_pick_B]
    if prev_pick_A == 0:
        A_coord = P1
    else:
        A_coord = events[prev_pick_A-1]
    if prev_pick_B == 0:
        B_coord = P2
    else:
        B_coord = events[prev_pick_B-1]
    #recursive calculation
    #--A
    np = max(prev_pick_A,prev_pick_B) + 1
    pick_A = calc_dist(events[n], A_coord) + distance(n+1, np, prev_pick_B)
    #--B
    pick_B = calc_dist(events[n], B_coord) + distance(n+1, prev_pick_A, prev_pick_B+1)
    #judge the answer
    if pick_A <= pick_B:
        memo[prev_pick_A][prev_pick_B] = pick_A
        return pick_A
    else:
        memo[prev_pick_A][prev_pick_B] = pick_B
        return pick_B
def search(n, prev_pick_A, prev_pick_B):
    if n>=E:
        return 0
    #recursive calculation
    #--A
    np = max(prev_pick_A, prev_pick_B) + 1
    pick_A = memo[np][prev_pick_B]
    #--B
    pick_B = memo[prev_pick_A][np]
    #judge the answer
    if pick_A <= pick_B:
        print(PATROL_CAR_A)
        search(n+1, prev_pick_A+1, prev_pick_B) + calc_dist
    else:
        print(PATROL_CAR_B)
        search(n+1, prev_pick_A, prev_pick_B+1)
while True:
    line = f.readline()
    if not line:
        break
    N = int(line.strip())
    E = int(f.readline())
    memo = [[-1 for _ in range(E+1)] for _ in range(E+1)]
    choices = [-1 for _ in range(E)]
    events = [list(map(int, f.readline().split())) for _ in range(E)] 
    #Patrol car initial coord.
    P1 = [1,1]
    P2 = [N,N]
    #Execute a simulation
    print(distance(0, 0, 0))
    search(0, 0, 0)
f.close()