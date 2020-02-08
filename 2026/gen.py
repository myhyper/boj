import random

k = random.randint(1,4)
n = random.randint(k,6)
f = random.randint(1,15)
#k = random.randint(1,62)
#n = random.randint(k,900)
#f = random.randint(1,5600)

a = open("random.txt","w+")
a.write("{} {} {}\n".format(k,n,f))
for _ in range(f):
    A = random.randint(1,n)
    B = random.randint(1,n)
    while A == B:
        B = random.randint(1,n)
    a.write("{} {}\n".format(A,B))
a.close