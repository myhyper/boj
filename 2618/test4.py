import sys;sys.setrecursionlimit(10000)
f = open('input.txt','r')
#f = sys.stdin

### INPUT ###
dp = [ [None for _ in range(1001)] for _ in range(1001) ]
n = int(f.readline()) # size of the city map
w = int(f.readline()) # a number of incidents
car1_pos = [[1,1]] + [[0,0] for _ in range(w+1)]
car2_pos = [[n,n]] + [[0,0] for _ in range(w+1)]
for _ in range(1,w+1): car1_pos[_] = car2_pos[_] = list(map(int, f.readline().split()))

### FUNCTIONS ###
def get_dist(arr,src,dst): # distance between two positions
    return abs(arr[src][0] - arr[dst][0]) \
             + abs(arr[src][1] - arr[dst][1])

def get_min_dist(car1,car2): # select the shortest distance to the next position
    if w == car1 or w == car2:  dp[car1][car2]=0;return 0
    if dp[car1][car2] != None:       return dp[car1][car2]
    
    next_idx    = max(car1,car2) + 1
    dist1       = get_dist(car1_pos,car1,next_idx)
    car1_move   = get_min_dist(next_idx,car2) + dist1
    
    dist2       = get_dist(car2_pos,car2,next_idx)
    car2_move   = get_min_dist(car1,next_idx) + dist2

    dp[car1][car2] = min(car1_move,car2_move)
    return dp[car1][car2]

def get_seq(car1,car2): # get the visit orders
    if w == car1 or w == car2:  return 'Max'
    
    next_idx    = max(car1,car2) + 1 # step up
    dist1       = get_dist(car1_pos,car1,next_idx)
    car1_move   = get_min_dist(next_idx,car2) + dist1
    
    dist2       = get_dist(car2_pos,car2,next_idx)
    car2_move   = get_min_dist(car1,next_idx) + dist2
    
    if car1_move < car2_move:   print(1);get_seq(      next_idx, car2)
    else:                       print(2);get_seq(car1, next_idx      )

### BEGIN THE LOGIC ###
ans = get_min_dist(0,0) # print answer
print(ans);get_seq(0,0) # print sequences