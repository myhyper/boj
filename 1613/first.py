import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open("input.txt",'r').readline
maxn = 401
n,k = map(int,f().split())
arr = [ [] for _ in range(maxn) ]

def foo(node, neo):
    for _ in range(maxn):
        if node in arr[_]:
            if neo not in arr[_]:
                arr[_].append(neo)
                foo(_, neo)

for _ in range(k):
    y,x = map(int,f().split())
    if x not in arr[y]:
        arr[y].append(x)
        for z in arr[x]:    
            if z not in arr[y]:
                arr[y].append(z)
        foo(y,x)

s = int(f())
for _ in range(s):
    a,b = map(int,f().split())
    
    if b in arr[a]:
        print(-1)
    else:
        if a in arr[b]:
            print(1)
        else:   print(0)