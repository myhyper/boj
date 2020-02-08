import sys; f=sys.stdin
f = open('input5.txt','r')
sys.setrecursionlimit(10000)
h,w = map(int,f.readline().split())
arr = [ [*(map(int,f.readline().split()))] for _ in range(h) ]
i = 1 ; dbg = 1
vs = [ [0 for _ in range(w)] for _ in range(h) ]
vs[0][0] = 1 # the first coord visited
closed = [ [0 for _ in range(w)] for _ in range(h) ]
def visit(x,y):
    s = 0
    if 0 < vs[y][x]: return vs[y][x]
    found = False
    for sx,sy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1),]:
        if 0 <= sx < w and 0 <= sy < h:
            # not closed and linked between
            if 0 == closed[sy][sx]:
                if arr[y][x] < arr[sy][sx]:
                    if vs[sy][sx] == 0:
                        vs[sy][sx] = visit(sx,sy)
                    s += vs[sy][sx]
                    #if dbg: print("\t{}, {} = {}".format(sx,sy,s))
                    found = True
    if found == False:
        closed[y][x] = 1
    return s
ans = visit(w-1,h-1)
print(ans)