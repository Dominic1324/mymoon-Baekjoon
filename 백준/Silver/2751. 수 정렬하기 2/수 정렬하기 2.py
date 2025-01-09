import sys
li = []
n = int(sys.stdin.readline())
for _ in range(n):
    li.append(int(sys.stdin.readline()))
      
li.sort()
for i in li:
    print(i)