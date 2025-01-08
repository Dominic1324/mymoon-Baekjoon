import sys
from collections import Counter

ma = 0

def isconti(li):
    li.sort()
    for i in range(len(li)):
        if i == 0:
            be = li[i]
        elif be + 1 != li[i]:
            return False
        be = li[i]
    return True

cl = []
num = []
for _ in range(5):
    clo, nu = sys.stdin.readline().split()
    cl.append(clo)
    num.append(int(nu))

if len(set(cl)) == 1 and isconti(num):
    ma = 900 + max(num)
elif 4 in Counter(num).values():
    re_dic = {v:k for k, v in Counter(num).items()}
    ma = 800 + re_dic[4]
elif 3 in Counter(num).values() and 2 in Counter(num).values():
    re_dic = {v:k for k, v in Counter(num).items()}
    ma = 700 + re_dic[3]*10 + re_dic[2]
elif len(set(cl)) == 1:
    ma = 600 + max(num)
elif isconti(num):
    ma = 500 + max(num)
elif 3 in Counter(num).values():
    re_dic = {v:k for k, v in Counter(num).items()}
    ma = 400 + re_dic[3]
elif list(Counter(num).values()).count(2) == 2:
    s = list(Counter(num).items())
    k = []
    for i in s:
        if i[1] == 2:
            k.append(i[0])
    ma = 300 + max(k) * 10 + min(k)
elif 2 in Counter(num).values():
    re_dic = {v:k for k, v in Counter(num).items()}
    ma = 200 + re_dic[2]
else:
    ma = 100 + max(num)

print(ma)

