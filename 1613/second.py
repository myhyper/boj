import sys
sys.setrecursionlimit(1000000);f=sys.stdin
n,k=map(int,f.readline().split());n+=1
arr = [ [False for _ in range(n)] for _ in range(n) ]
dp = [ [] for _ in range(n) ]
tmp = [[ False for _ in range(n) ] for _ in range(n) ]
for _ in range(k):
    s,d=map(int,f.readline().split())
    arr[s][d] = True
    dp[s].append(d)
def foo(s, d, t):
    t[d] = arr[s][d] = True
    for D in dp[d]:
        if not t[D]:
            foo(s, D, t)
for s in range(n):
    for d in range(n):
        foo(s, d, tmp[s])
S=int(f.readline())
for _ in range(S):
    s,d=map(int,f.readline().split())
    if arr[s][d]: print("-1")
    elif arr[d][s]: print( "1")
    else: print( "0")