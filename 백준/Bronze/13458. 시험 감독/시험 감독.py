n = int(input())
li = list(map(int, input().split()))
b, c = map(int, input().split())
tot = 0
for i in li:
    tot += 1
    i -= b
            
    if i > 0:
        tot += i//c
        i = i%c
        if i > 0:
            tot+=1
print(tot)