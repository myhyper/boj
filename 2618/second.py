import sys;f=sys.stdin
dbg=1
if dbg: f=open('input.txt','r')
n=int(f.readline())
w=int(f.readline())
c1 = (1,1)
c2 = (w,w)
arr = [list(map(int,f.readline().split())) for _ in range(w)]
dp = [[0,0] for _ in range(1000)]
i = 0
def get_dst(pos):
    a = abs(arr[i][0] - pos[0])
    b = abs(arr[i][1] - pos[1])
    return a + b
dp[i][0] = (get_dst(c1))
dp[i][1] = (get_dst(c2))
for i in range(1,w):
    dp[i][0] = dp[i-1][0] + (get_dst(c1))
    dp[i][1] = dp[i-1][0] + (get_dst(c2))
    c1 = arr[i]
    
    dp[i][0] = dp[i-1][1] + (get_dst(c1))
    dp[i][1] = dp[i-1][1] + (get_dst(c2))
    c2 = arr[i]
print(min(dp[i][0],dp[i][1]))