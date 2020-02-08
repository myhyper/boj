import sys; f=sys.stdin
debug = True
debug = False
if debug: f=open("input.txt",'r')

while True:
    w,h = map(int,f.readline().split())
    if not h: break
    arr = [ list(map(int,f.readline().split())) for _ in range(h) ]
    if debug: print(arr)

    a = -1
    i = 0
    s = [(0,0) for _ in range(50*50+1)]
    cnt = 0

    x,y = -1,0
    while True:
        if 0 == i:
            x += 1
            if w <= x:
                y += 1
                x = 0
                if h <= y:
                    print(cnt)
                    break
        elif i < 0: i *= -1
        if arr[y][x] or i:

            for sx,sy in [(0,0),(-1,-1),(-1,0),(-1,1),(0,-1),(0,1), (1,-1),(1,0),(1,1)]:
                
                if 0 <= x+sx and 0 <= y+sy and x+sx < w and y+sy < h:
                    if arr[y+sy][x+sx]:
                        arr[y+sy][x+sx] = 0
                        if not i: cnt += 1
                        s[i] = (x,y);i += 1
                        if debug: print("PUSH {}, {} ({})".format(x,y,i))
                        x = x+sx;y = y+sy
                        i *= -1
                        break
            if 0 < i:
                i-=1;x,y = s[i]
                if debug: print("POP {}, {} ({})".format(x,y,i))