import sys;f=sys.stdin
sys.setrecursionlimit(9999999)
dbg = 1
if dbg: f=open("input6.txt",'r')
t = int(f.readline())
MAX_VAL = 99999

UP   = 0
DOWN = 1
BOTH = 2
NONE = 3

# Case 1,2,3 에 대한 dp
for _ in range(t):
    dp = [ [[2*_,2*_,2*_] for _ in range(1,11011)] for _ in range(4) ]
    n,w = map(int,(f.readline().split()))
    arr1 = list(map(int,f.readline().split()))
    arr2 = list(map(int,f.readline().split()))
    
    # last 는 끝블록 상태를 나타낸다.
    def foo (idx, TOP):
        rtv = MAX_VAL
        if idx == n: # 마지막 칸 인경우
            if TOP == NONE:
                rtv = min(rtv, dp[NONE][idx-1][BOTH])
            if TOP ==  UP : rtv = min(rtv, dp[ UP ][idx-1][DOWN])
            if TOP == DOWN: rtv = min(rtv, dp[DOWN][idx-1][ UP ])
            if TOP == BOTH:
                rtv = min(rtv, dp[BOTH][idx-2][BOTH])
            return rtv
        
        COL_MOVE    = (arr1[idx] + arr2[idx]) <=w
        UP_MOVE     = (arr1[idx-1] + arr1[idx]) <=w
        DOWN_MOVE   = (arr2[idx-1] + arr2[idx]) <=w
        if TOP == UP and idx <= 1:
            UP_MOVE = False
        if TOP == DOWN and idx <= 1:
            DOWN_MOVE = False
        DOUBLE_MOVE = (UP_MOVE and DOWN_MOVE)

        # dp[인덱스 idx][마지막블록점유상태 TOP][다음블록점유상태 x3]
        if 0 == idx: # 첫칸인 경우
            rtv1 = MAX_VAL
            # 기본 출발 세팅
            dp[NONE][0][ UP ] = 1
            dp[NONE][0][DOWN] = 1
            if COL_MOVE:
                dp[NONE][0][BOTH] = 1
            else: # 위아래로 안합치면 UP/DOWN/BOTH로 합치는 경우의 수가 가능 하다.
                pass#dp[NONE][0][BOTH] = 2
            rtv1 = min(rtv1, foo(idx+1,NONE))
            if UP_MOVE  : 
                dp[ UP ][0][ UP ] = 1
                dp[ UP ][0][BOTH] = 2
                rtv1 = min(rtv1, foo(idx+1,UP))
            if DOWN_MOVE:
                dp[DOWN][0][DOWN] = 1
                dp[DOWN][0][BOTH] = 2
                rtv1 = min(rtv1, foo(idx+1,DOWN))
            if DOUBLE_MOVE:
                dp[BOTH][0][BOTH] = 2
                rtv1 = min(rtv1, foo(idx+1,BOTH))
            return rtv1
        else: # 그 이후는 더해나간다.
            dp[TOP][idx][ UP ] = min(dp[TOP][idx][ UP ], dp[TOP][idx-1][BOTH] + 1)
            if UP_MOVE:
                dp[TOP][idx][ UP ] = min(dp[TOP][idx][ UP ], dp[TOP][idx-1][DOWN] + 1)
            dp[TOP][idx][DOWN] = min(dp[TOP][idx][DOWN], dp[TOP][idx-1][BOTH] + 1)
            if DOWN_MOVE:
                dp[TOP][idx][DOWN] = min(dp[TOP][idx][DOWN], dp[TOP][idx-1][ UP ] + 1)
            dp[TOP][idx][BOTH] = min(dp[TOP][idx][BOTH], dp[TOP][idx-1][BOTH] + 2)
            if COL_MOVE:
                dp[TOP][idx][BOTH] = min(dp[TOP][idx][BOTH], dp[TOP][idx-1][BOTH] + 1)
            if DOUBLE_MOVE and 2 < n:
                if 0 == idx:
                    dp[TOP][idx][BOTH] = min(dp[TOP][idx][BOTH], 2)
                if 1 == idx:
                    if TOP == BOTH:
                        if COL_MOVE:
                            dp[TOP][idx][BOTH] = min(dp[TOP][idx][BOTH], 3)
                        else:
                            dp[TOP][idx][BOTH] = min(dp[TOP][idx][BOTH], 4)
                        dp[TOP][idx][UP] = 3
                        dp[TOP][idx][DOWN] = 3
                    else:
                        dp[TOP][idx][BOTH] = min(dp[TOP][idx][BOTH], 2)
                elif 1 < idx:
                    dp[TOP][idx][BOTH] = min(dp[TOP][idx][BOTH], dp[TOP][idx-2][BOTH] + 2)
            
            # 여기가 최적일 수도 있다.
            dp[TOP][idx][BOTH] = min(dp[TOP][idx][BOTH], dp[TOP][idx][ UP ] + 1)
            dp[TOP][idx][BOTH] = min(dp[TOP][idx][BOTH], dp[TOP][idx][DOWN] + 1)
            rtv = foo(idx+1,TOP)
        
        return rtv

    ans = foo(0, NONE)
    #print("")
    print(ans)
