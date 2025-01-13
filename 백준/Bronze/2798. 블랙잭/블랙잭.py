import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
ti = 0
for i in range(len(li)):
    for j in range(len(li)):
        if i == j:
            continue
        for k in range(len(li)):
            if li[i] + li[j] + li[k] > m :
                continue
            elif i == k or j == k:
                continue
            elif li[i] + li[j] + li[k] > ti:
                ti = li[i] + li[j] + li[k]

print(ti)