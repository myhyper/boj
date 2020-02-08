n = 6 # city size
w = 3 # a number of incidents

car1_history  = [
    (1,1),
    (3,5),
    (5,5),
    (2,3),
]
car1_history += [(0,0) for _ in range(100)]
car2_history  = [
    (n,n),
    (3,5),
    (5,5),
    (2,3),
]
car2_history += [(0,0) for _ in range(100)]

max_dp = 111
dp = [ [-1 for _ in range(max_dp)] for _ in range(max_dp) ]
arr = []
def get_distance(car1,car2):
    if w == car1 or w == car2: return 0
    if -1 != dp[car1][car2]: return dp[car1][car2]
    
    np = max(car1,car2) + 1
    n1 = abs(car1_history[car1][0] - car1_history[np][0]) + abs(car1_history[car1][1] - car1_history[np][1])
    n2 = get_distance(np,car2) + n1
    
    m1 = abs(car2_history[car2][0] - car2_history[np][0]) + abs(car2_history[car2][1] - car2_history[np][1])
    m2 = get_distance(car1,np) + m1

    dp[car1][car2] = min(n2,m2)
    if m2 < n2:
        dp[car1][car2] = m2
        arr.append(2)
    else:
        dp[car1][car2] = n2
        arr.append(1)
    return dp[car1][car2]


ans = get_distance(0,0)
print(ans)
for a in arr:
    print(a)