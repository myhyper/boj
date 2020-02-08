import sys
debug = True
#debug = False
f = sys.stdin
if debug: f = open("input.txt", "r")
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
while True:
    w,h = map(int, f.readline().split())
    if 0 == w or 0 == h: break
    arr = [ list(map(int,f.readline().split())) for _ in range(h) ]
    cnt = 0
    for y in range(h):
        for x in range(w):
            cnt = foo(x,y,cnt)
    print(cnt)
    if debug:
        for y in range(h):
            print(arr[y])
