import sys;f=sys.stdin
dbg = 1
if dbg: f=open("input.txt",'r')
t = int(f.readline())
MAX_VAL = 99
dp = [ [MAX_VAL,MAX_VAL,MAX_VAL] for _ in range(10) ]
BOTH = 0
UP = 1
DOWN = 2
# Case 1,2,3,4 에 대한 dp
for _ in range(t):
    n,w = map(int,(f.readline().split()))
    arr1 = list(map(int,f.readline().split()))
    arr2 = list(map(int,f.readline().split()))

def get_min_count(idx, dir):
    if idx == 0:
        if BOTH == dir:
            if arr1[idx] + arr2[idx] <= w: # 위아래를 둘다 합쳐본다.
                val = 1 
                dp[0][BOTH] = min(dp[0][BOTH], 1)
            else:
                val = 2 # 2부대 투입 
                dp[0][BOTH] = min(dp[0][BOTH], 2)
        else:
            val = 1 # 윗 혹은 아래 한칸만 쓰므로
            dp[0][dir] = 1
        return val
    if dp[idx][dir] != MAX_VAL: return dp[idx][dir]

    val = 0

    if arr1[idx] + arr2[idx] <= w: # 위아래를 둘다 합쳐본다.
        val = 1 # 1개로 처리 가능
    else:
        val = 2 # 2부대 투입
    dp[idx][BOTH] = min(dp[idx][BOTH],get_min_count(idx-1, BOTH) + val)
    if 0 < idx \
        and arr1[idx-1] + arr1[idx] <= w\
        and arr2[idx-1] + arr2[idx] <= w:
            if idx == 1: # 가로 막대 2개로 2칸뛰기
                x = 0
            else:    
                x = get_min_count(idx-2, BOTH)
            dp[idx][BOTH] = min(dp[idx][BOTH],x + 2)

    if arr1[idx-1] + arr1[idx] <= w: # 위만 합쳐 본다.
        count2 = get_min_count(idx-1, DOWN) + 1 # 왼쪽칸과 합체
        dp[idx][UP] = min(dp[idx][UP], count2)
    count2 = get_min_count(idx-1, BOTH) + 1 # 한칸 그냥 추가
    dp[idx][UP] = min(dp[idx][UP], count2)

    if arr2[idx-1] + arr2[idx] <= w: # 아래만 합쳐본다.
        count3 = get_min_count(idx-1, UP) + 1 # 왼쪽칸과 합체 
        dp[idx][DOWN] = min(dp[idx][DOWN], count3)
    count3 = get_min_count(idx-1, BOTH) + 1 # 한칸 그냥 추가
    dp[idx][DOWN] = min(dp[idx][DOWN], count3)
    
    rtv = dp[idx][dir]
    return rtv

for i in range(n):
    get_min_count(i, UP)
    get_min_count(i, DOWN)
    get_min_count(i, BOTH)
print(dp[n-1][0])
print(dp[n-1][1])
print(dp[n-1][2])
