import sys
sys.setrecursionlimit(9999999)
f = sys.stdin.readline
dbg = 1
if dbg: f=open("input.txt").readline
n = int(f())
n += 1
s= int(f())
dp = [ [] for _ in range(n) ]
arr = [ [0 for _ in range(n)] for _ in range(n) ]
for _ in range(s):
    a,b = map(int,f().split())
    arr[a][b] = 1
    arr[b][a] = 1
    if arr[a][b]:
        dp[a].append(b)
        dp[b].append(a)
tmp = [ [ 0 for _ in range(n) ] for _ in range(n) ]
def foo(s,d, t):
    t[d] = arr[s][d] = 1
    for D in dp[d]:
        if 0 == t[D]:
            foo(s,D, t)
for s in range(n):
    for d in dp[s]:
        foo(s,d, tmp[s])
print(sum(arr[1])-1)