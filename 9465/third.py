import sys
sys.setrecursionlimit(999999)
f = sys.stdin.readline
t = int(f())
for _ in range(t):
    n = int(f())
    arr1 = list(map(int,f().split()))
    arr2 = list(map(int,f().split()))
    dp1 = [0,0,0,-1,0,1]
    dp2 = [0,0,0,0,1,-1]
    def foo(idx):
        i=idx-0
        _=(i)%3
        j=(idx-1)%3
        k=(idx-2)%3
        if 0 == idx:
            dp1[_] = arr1[0]
            dp2[_] = arr2[0]
        elif 1 == idx:
            dp1[_] = max(dp1[_], dp2[j]+arr1[_])
            dp2[_] = max(dp2[_], dp1[j]+arr2[_])
        else:
            dp1[_] = max(dp1[_], dp2[j]+arr1[i], dp2[k]+arr1[i-1], dp2[k]+arr1[i])
            dp2[_] = max(dp2[_], dp1[j]+arr2[i], dp1[k]+arr2[i-1], dp1[k]+arr2[i])
        if n-1 ==i: return max(dp1[_],dp2[_])
        return foo(i+1)
    print(foo(0))