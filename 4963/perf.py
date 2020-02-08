import sys
st=[0]*2500
while 1:
    w,h=map(int,sys.stdin.readline().split())
    if not h:break
    cnt=0
    arr = [[0]*(w+2)]
    arr += [[0]+list(map(int,sys.stdin.readline().split()))+[0] for _ in range(h)]
    arr += [[0]*(w+2)]
    def foo():
        i=1
        while i:
            i-=1;x,y=st[i]
            if arr[y-1][x+1]: arr[y-1][x+1]=0;st[i]=x+1,y-1;i+=1
            if arr[y-1][x]: arr[y-1][x]=0;st[i]=x,y-1;i+=1
            if arr[y-1][x-1]: arr[y-1][x-1]=0;st[i]=x-1,y-1;i+=1
            if arr[y][x+1]: arr[y][x+1]=0;st[i]=x+1,y;i+=1
            if arr[y][x]: arr[y][x]=0;st[i]=x,y;i+=1
            if arr[y][x-1]: arr[y][x-1]=0;st[i]=x-1,y;i+=1
            if arr[y+1][x+1]: arr[y+1][x+1]=0;st[i]=x+1,y+1;i+=1
            if arr[y+1][x]: arr[y+1][x]=0;st[i]=x,y+1;i+=1
            if arr[y+1][x-1]: arr[y+1][x-1]=0;st[i]=x-1,y+1;i+=1
    for y in range(1,h+1):
        for x in range(1,w+1):
            if arr[y][x]:st[0]=x,y;arr[y][x]=0;foo();cnt+=1
    print(cnt)