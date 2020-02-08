import sys
f = sys.stdin
dbg = 1
if dbg: f = open("input3.txt",'r')

rnd = 0
if rnd:
    import random
    def make_rand():
        w,h = random.randint(1,5), random.randint(1,5)
        f = open("input3.txt",'w')
        f.write("{} {}\n".format(w,h))
        for _ in range(h):
            for _ in range(w):
                f.write("{} ".format(random.randint(0,1)))
            f.write("\n")
        f.write("0 0\n")
        f.close()

    def foo(x, y, cnt):
        if x < 0 or y < 0 or w <= x or h <= y:
            return cnt
        if 1 == arr[y][x]:
            cnt += 1
            arr[y][x] = 9
            for sy in range(-1, 2):
                for sx in range(-1, 2):
                    foo(x+sx, y+sy, cnt)
        return cnt
while 1:
    ans = None
    if rnd:
        f = open("input3.txt",'r')
        make_rand()

        while True:
            w,h = map(int, f.readline().split())
            if 0 == w or 0 == h: break
            arr = [ list(map(int,f.readline().split())) for _ in range(h) ]
            cnt = 0
            for y in range(h):
                for x in range(w):
                    cnt = foo(x,y,cnt)
            #print(cnt)
        ans = cnt

        f = open("input3.txt",'r')
    w,h = map(int,f.readline().split())
    arr = [ list(map(int,f.readline().split())) for _ in range(h) ]
    if not h: break
    
    x,y = 0,0
    i,cnt = 0,0

    st = [ 0 for _ in range(50*50+1) ]

    while 1:
        if 0 == i:
            x += 1
            if w <= x:
                x = 0
                y += 1
                if h <= y: break
        elif 0 < i:
            x,y = st[i-1]
        elif i < 0:
            i *= -1

        for sx,sy in [(x,y), (x-1,y-1),(x,y-1),(x+1,y-1), (x-1,y),(x+1,y), (x-1,y+1),(x,y+1),(x+1,y+1), ]:
            if 0<= sx < w and 0<= sy < h:
                if arr[sy][sx]:
                    arr[sy][sx] = 0
                    if not i: cnt += 1
                    if dbg: print("PUSH {}, {} ({})".format(x,y,i))
                    st[i] = (x,y)
                    i += 1
                    x,y = sx,sy
                    i *= -1
                    break
        if 0 < i:
            i -= 1
            x,y = st[i]
            if dbg: print("    POP {}, {} ({})".format(x,y,i))
    if rnd: print(ans)
    print(cnt)
    if ans != cnt:
        break