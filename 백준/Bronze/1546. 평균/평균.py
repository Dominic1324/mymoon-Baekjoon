import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
m = max(li)
n_li = []
for i in li:
    n_li.append(i/m*100)
print(sum(n_li)/len(li))
          