import sys;f=sys.stdin
sys.setrecursionlimit(9999999)
dbg = 1
if dbg: f=open("input3.txt",'r')
t = int(f.readline())
MAX_VAL = 99999

BOTH = 0
UP = 1
DOWN = 2

# Case 1,2,3 에 대한 dp
for _ in range(t):
    dp0 = [ [MAX_VAL,MAX_VAL,MAX_VAL] for _ in range(11011) ] # 안 연결 
    dp1 = [ [MAX_VAL,MAX_VAL,MAX_VAL] for _ in range(11011) ] # 위 만 연결
    dp2 = [ [MAX_VAL,MAX_VAL,MAX_VAL] for _ in range(11011) ] # 아래만 연결
    dp3 = [ [MAX_VAL,MAX_VAL,MAX_VAL] for _ in range(11011) ] # 둘다 연결
    n,w = map(int,(f.readline().split()))
    arr1 = list(map(int,f.readline().split()))
    arr2 = list(map(int,f.readline().split()))

    def foo(dp, idx, dir):
        if dp[idx][dir] != MAX_VAL: return dp[idx][dir]
        if idx < 0: return 0
        
        val = 0
        if arr1[idx] + arr2[idx] <= w: # 위아래를 둘다 합쳐본다.
            val = 1 # 1개로 처리 가능
        else:
            val = 2 # 2부대 투입
        dp[idx][BOTH] = min(dp[idx][BOTH],foo(dp, idx-1, BOTH) + val)
        if ((0 < idx and dp == dp0) or (1 < idx and dp != dp0)) \
            and arr1[idx-1] + arr1[idx] <= w\
            and arr2[idx-1] + arr2[idx] <= w:
                if idx == 1: # 가로 막대 2개로 2칸뛰기
                    x = 0
                else:    
                    x = foo(dp, idx-2, BOTH)
                dp[idx][BOTH] = min(dp[idx][BOTH],x + 2)

        if arr1[idx-1] + arr1[idx] <= w: # 위만 합쳐 본다.
            count2 = foo(dp, idx-1, DOWN) + 1 # 왼쪽칸과 합체
            dp[idx][UP] = min(dp[idx][UP], count2)
        count2 = foo(dp, idx-1, BOTH) + 1 # 한칸 그냥 추가
        dp[idx][UP] = min(dp[idx][UP], count2)

        if arr2[idx-1] + arr2[idx] <= w: # 아래만 합쳐본다.
            count3 = foo(dp, idx-1, UP) + 1 # 왼쪽칸과 합체 
            dp[idx][DOWN] = min(dp[idx][DOWN], count3)
        count3 = foo(dp, idx-1, BOTH) + 1 # 한칸 그냥 추가
        dp[idx][DOWN] = min(dp[idx][DOWN], count3)
        
        dp[idx][BOTH] = min(dp[idx][BOTH], dp[idx][UP] + 1)
        dp[idx][BOTH] = min(dp[idx][BOTH], dp[idx][DOWN] + 1)

        return dp[idx][dir]


    # 기본 dp 세팅 
    a=b=c=False
    dps = [dp0]
    if 1 < n:
        a = (arr1[-1] + arr1[0]) <= w
        b = (arr2[-1] + arr2[0]) <= w
        c = a and b
        if a: dps.append(dp1)
        if b: dps.append(dp2)
        if c: dps.append(dp3)
    for dp in dps:
        if arr1[0] + arr2[0] <= w: # 위아래를 둘다 합쳐본다.
            dp[0][BOTH] = 1
        else:
            dp[0][BOTH] = 2
        dp[0][UP] = 1
        dp[0][DOWN] = 1

    # 끝끼리 이어본다.
    if 1 < n:
        if a: # 연결 가능 할때
            dp1[0][BOTH] = 2
            dp1[0][DOWN] = 2
        if b: # 연결 가능 할때
            dp2[0][BOTH] = 2
            dp2[0][UP] = 2
        if c: # 연결 가능 할때
            dp3[0][BOTH] = 2
            dp3[0][UP] = 2
            dp3[0][DOWN] = 2

    for i in range(n):
        foo(dp0, i, BOTH)
        if a: foo(dp1, i, BOTH)
        if b: foo(dp2, i, BOTH)
        if c: foo(dp3, i, BOTH)

    ans1 = min(dp0[n-1][BOTH], min(dp1[n-1][DOWN], min(dp2[n-1][UP], dp3[n-2][BOTH])))
    ans = dp0[n-1][BOTH]
    if a:
        ans = min(ans,dp0[n-1][UP])
    if b:
        ans = min(ans,dp0[n-1][DOWN])
    if 1 < n and c:
        ans = min(ans, dp0[n-2][BOTH])
    print(ans)