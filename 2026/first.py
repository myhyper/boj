import sys;fp = sys.stdin.readline
dbg = 1
if dbg: fp = open('random.txt','r').readline

maxn = 909
n_friends = 0 # for array index
# Read Input data / init
k,n,f = map(int,fp().split())
arr = [[0 for _ in range(maxn)] for _ in range(maxn)]
blacklist = [0 for _ in range(maxn)]
for _ in range(f):
    a,b = map(int,fp().split())
    arr[a][b] = 1;arr[b][a] = 1

# get total number of friends each
def calc_number_of_friends():
    for i in range(1,n+1):
        arr[i][i] = 1 # they're a freind of themselves
        arr[i][n_friends] = sum(arr[i])
        if arr[i][n_friends] < k:
            blacklist[i] = 1 # it's an outsider. we don't need them.
calc_number_of_friends()

def get_number_of_mutual_friends(friend1, friend2):
    cnt = 0
    for _ in range(1,n+1): # index 0 is for sum, so skip
        if friend1[_] == 1 and 1 == friend2[_]:
            cnt += 1
    return cnt

def is_candidate(idx):
    return (blacklist[idx] == 0)
def is_not_candidate(idx):
    return (blacklist[idx] == 1)

def kill_his_bad_friends(idx):
    for j in range(1,n+1):
        if is_not_candidate(j):
            arr[i][j] = 0

def get_number_of_common_friends(idx):
    cnt = 0
    for z in range(idx,n+1):
        if k <= get_number_of_mutual_friends(arr[idx], arr[z]):
            cnt += 1
    return cnt

def print_friend_list(idx):
    cnt_selected = 0
    for x in range(idx,n+1):
        if arr[idx][x]: cnt_selected+=1;print(x)
        if k <= cnt_selected: break # cut if enough number of friends have selected

# Search
found = False
for i in range(1,n+1):
    if is_candidate(i): # if it's still alive
        kill_his_bad_friends(i)
        arr[i][n_friends] = sum(arr[i][1:n+1]) # count remain good friends
        if k <= arr[i][n_friends]: # it can be the answer : He has enough friends to be an answer
            if k <= get_number_of_common_friends(i):
                print_friend_list(i)
                found = True;break
    else:   arr[i][n_friends] = 0

# exception : no friends
if not found:
    print("-1")