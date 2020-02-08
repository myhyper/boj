import sys
fp = sys.stdin.readline
dbg = 1
maxn = 999
if dbg: fp = open('random.txt','r').readline
k,n,f = map(int,fp().split())
arr = [[0 for _ in range(maxn)] for _ in range(maxn)]
skip_list = [0 for _ in range(maxn)]
# get input from the media
for _ in range(f):
    a,b = map(int,fp().split())
    arr[a][b] = 1
    arr[b][a] = 1
# get total number of friends each
for i in range(1,n+1):
    arr[i][i] = 1
    arr[i][0] = sum(arr[i])
    if arr[i][0] < k:
        skip_list[i] = 1
found = False
for i in range(1,n+1):
    if skip_list[i] == 0:
        for j in range(1,n+1):
            if skip_list[j] == 1:
                arr[i][j] = 0
        n_friends = sum(arr[i][1:n+1])
        arr[i][0] = n_friends
        if k <= n_friends: # it can be the answer
            cnt = 0
            for _ in range(1,n+1):
                if arr[i][_]: cnt+=1;print(_)
                if k <= cnt: break
            found = True
            break
    else:
        arr[i][0] = 0
# search it
if not found:
    print("-1")