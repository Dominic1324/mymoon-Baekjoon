a = int(input())
b = int(input())
c = int(input())
tot = str(a*b*c)
li = [0 for _ in range(10)]
for i in range(len(tot)):
    li[int(tot[i])] += 1

for i in li:
    print(i)