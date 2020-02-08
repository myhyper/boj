import sys ; f=sys.stdin
dbg = True
if dbg: f = open('input6.txt','r')
sys.setrecursionlimit(25000)
w = int(f.readline())
arr = [list(map(int,f.readline().split())) for _ in range(w)]
vs = {};vs[w,w] = 1

def visit(x,y,lv):
    if x == w-1 and y == w-1: return 1
    if arr[y][x] == 0: return 0
    if False and dbg:
        ch = ""
        for _ in range(lv):
            ch += "    "
        print("{}=> {}, {}".format(ch,x,y))
    s=0
    sx = x + arr[y][x]
    sy = y
    if 0 <= sx < w and 0 <= sy < w:
        s += vs[sy,sx] if (sy,sx) in vs else visit(sx,sy,lv+1)
    sx = x
    sy = y + arr[y][x]
    if 0 <= sx < w and 0 <= sy < w:
        s += vs[sy,sx] if (sy,sx) in vs else visit(sx,sy,lv+1)
    vs[y,x] = s
    return s
print(visit(0,0,1))