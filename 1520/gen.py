import random
f = open('input5.txt','w')

h,w = 500,500

f.write("{} {}\n".format(h,w))
for y in range(h):
    n = 10000-y
    for x in range(w):
        f.write("{} ".format(n + (50 - x)))
    f.write("\n")
    #f.write("{} {} {} {} {}\n".format( n, abs(n - random.randint(1,50)), abs(n - random.randint(1,50)),
    #                                    abs(n - random.randint(1,50)), abs(n - random.randint(1,50))))
#f.write("6 5 4 3 2\n")

f.close