import sys;f=sys.stdin
dbg = 1
if dbg: f=open("input6.txt",'r')
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
                val = 1 # 1개로 처리 가능
            else:
                val = 2 # 2부대 투입 
        else:   val = 1 # 윗 혹은 아래 한칸만 쓰므로
        return val
    if dp[idx-1][dir] != MAX_VAL: return dp[idx-1][dir]

    val = 0
    rtv = MAX_VAL

    if BOTH == dir:
        if arr1[idx] + arr2[idx] <= w: # 위아래를 둘다 합쳐본다.
            val = 1 # 1개로 처리 가능
        else:
            val = 2 # 2부대 투입
        dp[idx][BOTH] = min(dp[idx][BOTH],get_min_count(idx-1, BOTH) + val)
        if 0 < idx \
            and arr1[idx-1] + arr1[idx] <= w\
            and arr2[idx-1] + arr2[idx] <= w:
                if idx == 1:
                    x = 0
                else:    
                    x = get_min_count(idx-2, BOTH)
                dp[idx][BOTH] = min(dp[idx][BOTH],x + 2)
        rtv = min(rtv,dp[idx][dir])

    if dir == UP or BOTH == dir: # 윗칸을 쓸수 있다.
        if arr1[idx-1] + arr1[idx] <= w: # 위만 합쳐 본다.
            val = 1 # 왼쪽칸과 합체
            count2 = get_min_count(idx-1, DOWN) + val
            dp[idx][UP] = min(dp[idx][UP], count2)
        else:
            val = 1 # 한칸 그냥 추가
            count2 = get_min_count(idx-1, BOTH) + val
            dp[idx][UP] = min(dp[idx][UP], count2)
        if BOTH == dir:
            count2 += 1
            dp[idx][BOTH] = min(dp[idx][BOTH],get_min_count(idx-1, BOTH) + count2)
            rtv = min(rtv,dp[idx][dir])
        else:
            dp[idx][UP] = min(dp[idx][UP], count2)
        rtv = min(rtv, count2)

    if dir == DOWN or BOTH == dir: # 아랫칸을 쓸수있다.
        if arr2[idx-1] + arr2[idx] <= w: # 아래만 합쳐본다.
            val = 1 # 왼쪽칸과 합체 
            count3 = get_min_count(idx-1, UP) + val
            dp[idx][DOWN] = min(dp[idx][DOWN], count3)
        else:
            val = 1 # 한칸 그냥 추가
            count3 = get_min_count(idx-1, BOTH) + val
            dp[idx][DOWN] = min(dp[idx][DOWN], count3)
        if BOTH == dir:
            count3 += 1
            dp[idx][BOTH] = min(dp[idx][BOTH],get_min_count(idx-1, BOTH) + count3)
            rtv = min(rtv,dp[idx][dir])
        else:
            dp[idx][DOWN] = min(dp[idx][DOWN], count3)
        rtv = min(rtv, count3)
    dp[idx][dir] = rtv
    return rtv

ans = get_min_count(n-1, BOTH)
print(ans)
