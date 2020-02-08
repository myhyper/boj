import sys
sys.setrecursionlimit(10000)
while 1:
    w,h = map(int,sys.stdin.readline().split())
    if not w:break
    def foo(arr,i,j):
        for x,y in [(i-1,j-1),(i,j-1),(i+1,j-1), (i-1,j),(i,j),(i+1,j), (i-1,j+1),(i,j+1),(i+1,j+1), ]:
            if arr[y][x]:arr[y][x] = 0;foo(arr,x,y)
    cnt = 0
    arr = [[0]*(w+2)]
    arr += [[0]+list(map(int,sys.stdin.readline().split()))+[0] for _ in range(h)]
    arr += [[0]*(w+2)]
    for y in range(1,h+1):
        for x in range(1,w+1):
            if arr[y][x]:
                foo(arr,x,y);cnt += 1
    print(cnt)