n = int(input())
li = list(map(int, input().split()))
t, p = map(int, input().split())
T = 0
for i in li:
    if i%t == 0:
        T+=i//t
    else:
        T+=i//t+1
print(T)
if n%p == 0:
    print(n//p, 0)
else:
    print(n//p, n%p)