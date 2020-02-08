import sys
sys.setrecursionlimit(100000)
#DEBUG = True
DEBUG = False
if DEBUG:
    f = open("#2026/input.txt")
else:
    f = sys.stdin
ans = []
def search(rem, index):
    global ans, invalid_indices
    #terminate the method if answer key is already allocated
    if len(ans) > 0:
        return
    #validate if new element is linked to all elements in current list
    if len(ans_tmp) > 0:
        if index in invalid_indices:
            return
        for i in ans_tmp:
            if relation_array[i][index] == 0:
                return
    #apppend
    ans_tmp.append(index)
    # print(ans_tmp, rem)
    #check if the element appended is last one and determine to update to answer key
    if rem == 1:
        if ans == []:
            ans = ans_tmp.copy()
            return
    #continue to append next element
    for i in range(index+1, N-rem+2):
        search(rem-1, i)
    ans_tmp.pop()
    return
K, N, F = list(map(int, f.readline().split()))
relation_array = [[0 for _ in range(N)]for _ in range(N)]
invalid_indices =[]
for _ in range(F):
    x, y = list(map(int, f.readline().split()))
    relation_array[x-1][y-1] = relation_array[y-1][x-1] = 1
for i in range(N):
    if sum(relation_array[i]) < K-1:
        invalid_indices.append(i)
ans_tmp = []
for i in range(N-K+1):
    search(K, i)
if not ans:
    print("-1")
else:
    for i in ans:
        print(i+1)
f.close()