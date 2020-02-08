import sys
sys.setrecursionlimit(100000)
DEBUG = True
#DEBUG = False
if DEBUG:
    f = open("input_135.txt")
else:
    f = sys.stdin
ans = []
def search(ans_tmp, rem, index):
    global ans, invalid_indices
    #validate if new element is linked to all elements in current list
    if len(ans_tmp):
        if invalid_indices[index]: return
        flag_tmp = True
        for i in ans_tmp:
            if relation_array[i][index] == 0:
                flag_tmp = False
                break
        if flag_tmp == False:
            return
    #apppend
    ans_tmp.append(index)
    # print(ans_tmp, rem)
    #check if the element appended is last one and determine to update to answer key
    if rem == 1:
        if ans == []:
            ans = ans_tmp.copy()
        else:
            for i in range(K):
                if ans_tmp[i] != ans[i]:
                    if ans_tmp[i] < ans[i]:
                        ans = ans_tmp.copy()
                    break
        ans_tmp.pop()
        return
    #continue to append next element
    for i in range(index+1, N-rem+2):
        search(ans_tmp, rem-1, i)
    ans_tmp.pop()
    return
K, N, F = list(map(int, f.readline().split()))
relation_array = [[0 for _ in range(N)]for _ in range(N)]
invalid_indices =[0 for _ in range(N)]
for _ in range(F):
    x, y = list(map(int, f.readline().split()))
    relation_array[x-1][y-1] = relation_array[y-1][x-1] = 1
for i in range(N):
    relation_array[i][i] = 1
    if sum(relation_array[i]) < K:
        invalid_indices[i] = 1
for i in range(N-K+1):
    search([], K, i)
if not ans:
    print("-1")
else:
    for i in ans:
        print(i+1)
f.close()