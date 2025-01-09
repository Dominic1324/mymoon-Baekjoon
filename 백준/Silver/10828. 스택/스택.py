import sys
li = []
n = int(sys.stdin.readline())
for i in range(n):
    m = sys.stdin.readline()
    if m[:2] == "pu":
        m, num = m.split()
        li += [int(num)]
    elif m[0] == "p":
        if len(li) == 0:
            print(-1)
        else:
            print(li.pop(-1))
    elif m[0] == "s":
        print(len(li))
    elif m[0] == "e":
        if len(li) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])