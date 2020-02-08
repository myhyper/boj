import os
#os.system("cat input3.txt > ./a > o.txt")
#print(os.system("cat input3.txt < a"))

rand = 1
while 1:
    if rand:
        os.system("python3 gen.py")
    a = os.popen("./a").read()
    if not rand: print(a)
    b = os.popen("python3 third.py").read()
    if not rand: print(b)

    if a != b:
        print("Found!")
        print("\n answer should be ",a)
        print(" it was ", b)
        break
    print(".", end='')