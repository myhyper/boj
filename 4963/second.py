# Scope test 5 : NG

def foo():
    global a
    print(a)

def bar():
    a = 1
    foo()

bar()