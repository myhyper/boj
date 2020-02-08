import sys
f = sys.stdin.readline
f = open('input.txt','r').readline
t = int(f())


UP   = 0
DOWN = 1
SKIP = 2

# pos 0 up  1 down  2 skip
def foo(idx):
    if 0 == idx == n-1:
        return max(arr1[idx], arr2[idx])
    if n-2 <= idx: return 0
    if 0 < dp[idx][UP] and 0 < dp[idx][DOWN] and 0 < dp[idx][SKIP]:
        return max(dp[idx][UP], max(dp[idx][DOWN], dp[idx][SKIP]))
    rtv = 0
    for j in range(3):
        i = idx + j
        if n-2 < i: break
        for k in range(3):        
            for l in range(3):
                if j == 0 and k == 0: continue
                if l == 0 and k == 0: continue
                if j == 1 and k == 1: continue
                if l == 1 and k == 1: continue
                val = 0      
                #print(j,k,l)
                if     0 == j and 0 != k           : val += arr1[idx]
                if idx < n-1:
                    if 0 != j and 0 == k and 0 != l: val += arr1[idx+1]
                if idx < n-2: 
                    if            0 != k and 0 == l: val += arr1[idx+2]
                
                if     1 == j and 1 != k           : val += arr2[idx]
                if idx < n-1: 
                    if 1 != j and 1 == k and 1 != l: val += arr2[idx+1]
                if idx < n-2: 
                    if            1 != k and 1 == l: val += arr2[idx+2]
                rtv = max(rtv, val)
                if 0 < idx:
                    if UP == j:
                        dp[idx][j] = max(dp[idx-1][DOWN],dp[idx-1][SKIP]) + val
                    elif DOWN == j:
                        dp[idx][j] = max(dp[idx-1][UP],dp[idx-1][SKIP]) + val
                    else: # j 머리가 스킵인 경우 그대로 가져온다.
                        dp[idx][j] = max(dp[idx-1][UP],dp[idx-1][SKIP])
                    rtv = dp[idx][j]
                else:
                    dp[idx][j] = rtv
    print("[i={}] val = {}".format(idx,val))
    return max(max(dp[idx][UP],max(dp[idx][DOWN],dp[idx][SKIP])), foo(idx+1))

for _ in range(t):
    n = int(f())
    arr1 = list(map(int, f().split()))
    arr2 = list(map(int, f().split()))
    
    dp = [ [0,0,0] for _ in range(100000) ]
    print(foo(0))
    #print(arr1)
    #print(arr2)