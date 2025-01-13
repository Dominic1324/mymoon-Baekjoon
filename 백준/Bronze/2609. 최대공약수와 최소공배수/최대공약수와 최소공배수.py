a, b = map(int, input().split())
c, d = a, b
k = 1
while True:
    a, b = b, a%b
    if b == 0:
        print(a)
        k = a
        break
print(c*d//k)

