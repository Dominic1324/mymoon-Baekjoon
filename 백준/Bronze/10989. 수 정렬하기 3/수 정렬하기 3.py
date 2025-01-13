import sys
n = int(sys.stdin.readline())
li = [0] * 10001
for i in range(n):
    li[int(sys.stdin.readline())] += 1
for i in range(len(li)):
    if li[i] != 0:
        for _ in range(li[i]):
            print(i)