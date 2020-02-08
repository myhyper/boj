import sys;f=sys.stdin
dbg = True
if dbg: f = open('in','r')
w = int(f.readline())
arr = [0] * 310
dp  = [[0 for _ in range(6)] for _ in range(310)]
for _ in range(w): arr[_] = int(f.readline())
dp[0][1] = dp[0][2] = dp[0][4] = dp[1][5] = dp[1][3] = arr[0]
dp[1][1] = dp[1][4] = arr[1]
dp[1][2] = arr[1] + arr[0]
for _ in range(2,w):
    if dp[_-1][1] or dp[_-1][4]:
        dp[_][2] = max(dp[_-1][1],dp[_-1][4]) + arr[_]
        dp[_][5] = max(dp[_-1][1],dp[_-1][4])
    if dp[_-1][2]:
        dp[_][3] = dp[_-1][2]
    if dp[_-1][3]:
        dp[_][1] = dp[_-1][3] + arr[_]
    if dp[_-1][5]:
        dp[_][4] = dp[_-1][5] + arr[_]
ans = -99999
for y in range(1,6):
    if y in [3,5]: continue
    if ans < dp[w-1][y]: ans = dp[w-1][y]
print(ans)