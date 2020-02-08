import sys;f=sys.stdin
import random
dbg=0
if dbg: f=open('input.txt','r')
n=int(f.readline())
w=int(f.readline())
arr = [list(map(int,f.readline().split())) for _ in range(w)]
def get_dst(pos, i):
    a = abs(arr[i][0] - pos[0])
    b = abs(arr[i][1] - pos[1])
    return a + b
class Gene:
    def __init__(self):
        self.g = [random.randint(1,2) for _ in range(w)]
        #self.dp = [[0,0] for _ in range(w)]
        self.dp = [0 for _ in range(w)]
        self.c1 = (1,1)
        self.c2 = (n,n)
    def evol(self):
        self.g = [random.randint(1,2) for _ in range(w)]
        for _ in range(len(self.g)):
            if 0 == random.randint(0,5):
                self.g[_] = random.randint(1,2)

    def eval(self):
        i = 0
        for n in self.g:
            if 0 == i:
                if 1 == n:
                    self.dp[i] = (get_dst(self.c1, i))
                    self.c1 = arr[i]
                else:
                    self.dp[i] = (get_dst(self.c2, i))
                    self.c2 = arr[i]
            else:
                if 1 == n:
                    self.dp[i] = self.dp[i-1] + (get_dst(self.c1, i))
                    self.c1 = arr[i]
                else:
                    self.dp[i] = self.dp[i-1] + (get_dst(self.c2, i))
                    self.c2 = arr[i]
            i += 1
        return (self.dp[w-1])
    def print(self):
        print(self.dp[w-1])
        print("")
    def print_all(self):
        print(self.dp[w-1])
        for n in self.g:
            print(n)
gen = Gene()
a = gen.eval()
for i in range(9000):
    if 0:
        gen2 = Gene()
        b = gen2.eval()
        if b < a:
            gen = gen2
            a = b
            gen.print()
        
    gen3 = Gene()
    j = 0
    for x in gen.g:
        gen3.g[j] = x
        j+=1
    gen3.evol()
    c = gen3.eval()
    if c < a:
        gen = gen3
        a = c
        #gen3.print()

gen.print_all()