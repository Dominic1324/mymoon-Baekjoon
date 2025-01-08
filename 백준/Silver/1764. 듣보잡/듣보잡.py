import sys
n, m = map(int, sys.stdin.readline().strip().split())
re = []
cnt = 0

da = sys.stdin.read().splitlines()
n_set, m_set = set(da[0:n]), set(da[n:])

re = sorted(n_set & m_set)
print(len(re))
print('\n'.join(re))
