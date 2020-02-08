import random
f = open("input6.txt","w+")
n = 1000 #random.randint(1,1000)
w = 1000 #random.randint(1,1000)
f.write("1\n")
f.write("{} {}\n".format(n, w))
for _ in range(2):
    for _ in range(n):
        if 0 < _: f.write(" ")
        f.write("{}".format(random.randint(1,w)))
    f.write("\n")
f.close