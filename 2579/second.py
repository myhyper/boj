import sys;I=sys.stdin.readline;n,d=int(I()),[0]
m=[0]+[int(I())for _ in range(n)];d+=[m[1],m[1]+m[2]]
for i in range(3,n+1):d+=[max(m[i]+m[i-1]+d[i-3],m[i]+d[i-2])]
print(d[n])