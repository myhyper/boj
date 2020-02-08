import sys
sys.setrecursionlimit(1000000)
DEBUG = True
#DEBUG = False
if DEBUG:
    f = open("random.txt")
else:
    f = sys.stdin
ans = []
def search(ans_tmp, rem, index):
    global ans
    #validate if new element is linked to all elements in current list
    if 0 < len(ans_tmp):
        flag_tmp = True
        for i in ans_tmp:
            if relation_array[i][index] == 0:
                flag_tmp = False
                break
        if flag_tmp == False:
            return
    #apppend
    ans_tmp.append(index)
    #check if the element appended is last one and determine to update to answer key
    if rem == 1:
        if ans == []:
            ans = ans_tmp.copy()
        else:
            for i in range(K):
                if ans_tmp[i] < ans[i]:
                    ans = ans_tmp.copy()
                    break
        ans_tmp.pop()
        return
    #continue to append next element
    for i in range(index+1, N-rem+2):
        if K <= sum(relation_array[i]): # if the number of friends is greater than K
            search(ans_tmp, rem-1, i)
    ans_tmp.pop()
    return
K, N, F = list(map(int, f.readline().split()))
relation_array = [[0 for _ in range(N)]for _ in range(N)]
for _ in range(F):
    x, y = list(map(int, f.readline().split()))
    relation_array[x-1][y-1] = 1; relation_array[y-1][x-1] = 1
for i in range(N-K+1):
    search([], K, i)
if not ans:
    print("-1")
else:
    for i in ans:
        print(i+1)
f.close()