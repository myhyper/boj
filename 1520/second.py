import sys; f=sys.stdin
sys.setrecursionlimit(10000)
h,w = map(int,f.readline().split())
arr = [[0]*(w+2)]+[[0]+[*(map(int,f.readline().split()))]+[0] for _ in range(h)]+[[0]*(w+2)]
vs  = [[0 for _ in range(w+2)] for _ in range(h+2)]
vs[1][1] = 1
def visit(x,y,s=0):
    a = x-1
    if arr[y][x] < arr[y][a] and arr[y][a]:
        if not vs[y][a]: vs[y][a] = visit(a,y)
        s += vs[y][a]
    a = x+1
    if arr[y][x] < arr[y][a] and arr[y][a]:
        if not vs[y][a]: vs[y][a] = visit(a,y)
        s += vs[y][a]
    a = y-1
    if arr[y][x] < arr[a][x] and arr[a][x]:
        if not vs[a][x]: vs[a][x] = visit(x,a)
        s += vs[a][x]
    a = y+1
    if arr[y][x] < arr[a][x] and arr[a][x]:
        if not vs[a][x]: vs[a][x] = visit(x,a)
        s += vs[a][x]
    if not s: arr[y][x] = 0
    return s
ans = visit(w,h)
print(ans)