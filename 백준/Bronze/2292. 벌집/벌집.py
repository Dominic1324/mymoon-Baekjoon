import sys
n = int(sys.stdin.readline())
cnt = 1
s = 1
p = 0
while True:
    if n <= s:
        break
    p+=6
    s += p
    cnt+=1

print(cnt)
