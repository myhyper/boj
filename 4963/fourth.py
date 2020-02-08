import sys; f=sys.stdin
class MyStack:
    def __init__(self):
        self.arr = [0] * 2500
        self.idx = 0
    def push(self,a):
        self.arr[self.idx] = a
        self.idx += 1
    def pop(self):
        self.idx -= 1
        return self.arr[self.idx]
class Arr:
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.cnt = 0
    def read_map(self):
        self.arr = [[ 0 ] * 52]
        self.arr+= [[0] + list(map(int,f.readline().split()))+[0] for _ in range(self.h)]
        self.arr+= [[ 0 ] * 52]
        self.stack = MyStack()
    def search(self):
        for y in range(1,self.h+1):
            for x in range(1,self.w+1):
                if self.is_island(x,y):
                    self.search_deeper(x,y)
    def is_island(self,x,y):
        return self.arr[y][x]
    def search_deeper(self,x,y):
        self.cnt += 1
        self.visit(x,y)
        while self.stack.idx:
            x,y = self.stack.pop()
            for x,y in [(x-1,y-1),(x,y-1),(x+1,y-1), (x-1,y),(x,y),(x+1,y), (x-1,y+1),(x,y+1),(x+1,y+1), ]:
                if self.is_island(x,y):
                    self.visit(x,y)
    def visit(self,x,y):
        self.stack.push((x,y))
        self.arr[y][x] = 0
    def print(self):
        print(self.cnt)
while 1:    
    w,h = map(int,f.readline().split())
    a = Arr( w,h )
    if not h: break
    a.read_map()
    a.search()
    a.print()