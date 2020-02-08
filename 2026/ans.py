import sys
fp = sys.stdin.readline
dbg = 1
if dbg: fp = open("random.txt",'r').readline
[K, N, F] = list(map(int,fp().split()))
links = {i:[] for i in range(N)}
for i in range(F):
    [n1, n2] = list(map(int,fp().split()))
    links[min(n1, n2)-1].append(max(n1,n2)-1)
for i in range(N-K+1):
    arr = sorted(links[i], reverse=True)
    fullCon = [i]
    count = 1
    while len(arr):
        nextNode = arr.pop()
        fullCon.append(nextNode)
        arr = [a for a in arr if a in set(links[nextNode])]
        #arr = []
        #if a in set(links[nextNode]):
        #    for a in arr:
        #        arr.append(a)
        count += 1
        if count == K: break
    if count == K:
        count = -10
        for item in fullCon[:K]: print(item+1)
        break
if count != -10: print(-1)