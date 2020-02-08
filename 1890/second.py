import sys ; f=sys.stdin
f = open('input6.txt','r')
w = int(f.readline())
arr = [[0] * (w+20)] * 10
arr+= [[0] * 10 + list(map(int,f.readline().split()))+[0] * 10 for _ in range(w) ]
arr+= [[0] * (w+20)] * 10
vs = {} ; vs[9+w,9+w] = 1
def visit(x,y):
    if x == 10+w-1 and y == 10+w-1: return 1
    if arr[y][x] == 0: return 0
    vs[y,x]=0 ; sx = x + arr[y][x] ; sy = y + arr[y][x]
    vs[y,x] += vs[y,sx] if (y,sx) in vs else visit(sx,y)
    vs[y,x] += vs[sy,x] if (sy,x) in vs else visit(x,sy)
    return vs[y,x]
print(visit(10,10))