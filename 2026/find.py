import os

rand = 0
while 1:
    if rand:
        os.system("python3 gen.py")
    #a = os.popen("./a.out").read()
    a = os.popen("python3 ans.py").read()
    #b = os.popen("python3 first.py").read()
    #a = os.popen("python3 first.py").read()
    #b = os.popen("python3 gs2.py").read()
    b = os.popen("python3 first.py").read()
    if a != b:
        print("found!")
        print("answer should be \n", a)
        print("your answer was \n", b)
        break
    print(".",end='')
