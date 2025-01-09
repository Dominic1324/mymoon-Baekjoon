import sys
n = input()
li = list(map(int, sys.stdin.readline().split()))
n = input()
li_m = list(map(int, sys.stdin.readline().split()))
dic = {}
for i in li:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1
lll = dic.keys()
for i in li_m:
    if i in lll:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")
        