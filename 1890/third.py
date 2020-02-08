import sys;f=sys.stdin
w=int(f.readline());v={};v[9+w,9+w]=1
a=[[0]*(w+20)]*10
a+=[[0]*10+[*(map(int,f.readline().split()))]+[0]*10 for _ in range(w)]
a+=[[0]*(w+20)]*10
def f(x,y):
    if x==10+w-1 and y==10+w-1:return 1
    if a[y][x]==0:return 0
    v[y,x]=0;i=x+a[y][x];j=y+a[y][x]
    v[y,x]+=v[y,i]if(y,i)in v else f(i,y)
    v[y,x]+=v[j,x]if(j,x)in v else f(x,j)
    return v[y,x]
print(f(10,10))