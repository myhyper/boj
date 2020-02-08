import sys
f = sys.stdin.readline
n = int(f())
arr = []
dp = [ [] for _ in range(n) ]
for _ in range(n):
    arr.append(list(map(int,f().split())))
    for d in range(n):
        if arr[_][d]:
            dp[_].append(d)
tmp = [ [ 0 for _ in range(n) ] for _ in range(n) ]
def foo(s,d, t):
    t[d] = arr[s][d] = 1
    for D in dp[d]:
        if 0== t[D]:
            foo(s,D, t)
for s in range(n):
    for d in dp[s]:
        foo(s,d, tmp[s])
for y in range(len(arr)):
    for x in range(len(arr[y])):
        print(arr[y][x],end=' ')
    print("")