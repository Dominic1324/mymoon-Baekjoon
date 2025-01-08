import sys
n = int(sys.stdin.readline())
num_li = list(map(int, sys.stdin.readline().split()))
oper_li = list(map(int, sys.stdin.readline().split()))
nam = []
for i in range(len(oper_li)):
    for j in range(oper_li[i]):
        nam.append(i)

all_case = []
re_li = []


def make(ch, nam):
    if len(nam) == 0:
        global all_case
        all_case.append(ch[:])
        return

    for i in range(len(nam)):
        t = nam.pop(i)
        ch.append(t)

        make(ch, nam)

        ch.pop()
        nam.insert(i, t)

make([], nam)
all_case = list(set(tuple(i) for i in all_case))

for i in all_case:
    re = 0
    for j, k in zip(num_li, [-1]+list(i)):
        if k == -1:
            re = j
        elif k == 0:
            re += j
        elif k == 1:
            re -= j
        elif k == 2:
            re *= j
        elif k == 3:
            if re<0:
                re = -((-re)//j)
            else:
                re = re//j
        
    re_li.append(re)

print(max(re_li))
print(min(re_li))