import sys
sys.setrecursionlimit(999999)
f = sys.stdin.readline
dbg = 0
if dbg: f = open('input2.txt','r').readline
t = int(f())
for _ in range(t):
    n = int(f())
    arr1 = list(map(int,f().split()))
    arr2 = list(map(int,f().split()))
        
    dp1 = [0 for _ in range(100001)]
    dp2 = [0 for _ in range(100001)]
    def foo(idx):
        
        if 0 == idx:
            dp1[idx] = arr1[0]
            dp2[idx] = arr2[0]
        elif 1 == idx:
            dp1[idx] = max(dp1[idx] , dp2[idx-1]+arr1[idx])
            dp2[idx] = max(dp2[idx] , dp1[idx-1]+arr2[idx])
        else:
            dp1[idx] = max(dp1[idx] , dp2[idx-1]+arr1[idx] , dp2[idx-2]+arr1[idx-1] , dp2[idx-2]+arr1[idx])
            dp2[idx] = max(dp2[idx] , dp1[idx-1]+arr2[idx] , dp1[idx-2]+arr2[idx-1] , dp1[idx-2]+arr2[idx])
        
        if n-1 == idx:
            return max(dp1[idx],dp2[idx])
        return foo(idx+1)
        
    print(foo(0))