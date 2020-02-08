import sys
sys.setrecursionlimit(100000)
DEBUG = True
#DEBUG = False
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
def distance(prev_pick_A, prev_pick_B):
    if prev_pick_A>=E or prev_pick_B>=E:
        return 0
    if ((prev_pick_A, prev_pick_B) in memo):
        return memo[(prev_pick_A,prev_pick_B)]
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
    n = max(prev_pick_A,prev_pick_B)+1
    pick_A = calc_dist(events[n-1], A_coord) + distance(n, prev_pick_B)
    #--B
    pick_B = calc_dist(events[n-1], B_coord) + distance(prev_pick_A, n)
    #judge the answer
    if pick_A <= pick_B:
        memo[(prev_pick_A,prev_pick_B)] = pick_A
        return pick_A
    else:
        memo[(prev_pick_A,prev_pick_B)] = pick_B
        return pick_B
def distance2(n, prev_pick_A, prev_pick_B):
    if n>=E:
        return 0
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
    pick_A = calc_dist(events[n], A_coord) + distance2(n+1, n+1, prev_pick_B)
    #--B
    pick_B = calc_dist(events[n], B_coord) + distance2(n+1, prev_pick_A, n+1)
    #judge the answer
    if pick_A <= pick_B:
        choices[n] = PATROL_CAR_A
        return pick_A
    else:
        choices[n] = PATROL_CAR_B
        return pick_B
while True:
    line = f.readline()
    if not line:
        break
    N = int(line.strip())
    E = int(f.readline())
    memo = dict()
    choices = [-1 for _ in range(E)]
    events = [list(map(int, f.readline().split())) for _ in range(E)] 
    #Patrol car initial coord.
    P1 = [1,1]
    P2 = [N,N]
    #Execute a simulation
    print(distance(0, 0))
    (distance2(0, 0, 0))
    for i in choices:
        print(i)