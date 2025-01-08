import sys

n, new, p = map(int, sys.stdin.readline().split())
if n > 0:
    rank_li = list(map(int, sys.stdin.readline().split()))
else:
    rank_li = []

if n == p and new <= rank_li[-1]:
    print(-1)
else:
    rank_li.append(new)
    rank_li.sort(reverse=True)
    rank = rank_li.index(new) + 1  
    if rank > p:  
        print(-1)
    else:
        print(rank)