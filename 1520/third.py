import sys ; f=sys.stdin
f = open('input5.txt','r')
sys.setrecursionlimit(10000)
h,w = map(int,(f.readline().split()))
arr = [[0]*(w+2)]+[[0]+[*(map(int,f.readline().split()))]+[0] for _ in range(h)]+[[0]*(w+2)]
vs = {};vs[h,w] = 1
def visit(x,y):
    s=0;sx = x-1 ; sy = y-1
    if arr[y][sx] < arr[y][x]:
        s += vs[y,sx] if (y,sx) in vs else visit(sx,y)
    if arr[sy][x] < arr[y][x]:
        s += vs[sy,x] if (sy,x) in vs else visit(x,sy)
    sx = x+1 ; sy = y+1
    if arr[y][sx] < arr[y][x] and x < w:
        s += vs[y,sx] if (y,sx) in vs else visit(sx,y)
    if arr[sy][x] < arr[y][x] and y < h:
        s += vs[sy,x] if (sy,x) in vs else visit(x,sy)
    vs[y,x] = s
    return s
print(visit(1,1))