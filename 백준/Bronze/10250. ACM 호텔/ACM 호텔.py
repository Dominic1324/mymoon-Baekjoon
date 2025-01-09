nu = int(input())
for i in range(nu):
    h, w, n = map(int, input().split())
    a = n%h
    d = n//h+1
    if a == 0:
        a = h
        d = d-1
    if d >= 10:
        print(a, d, sep="")
    else:
        print(a, 0, d, sep="")
