n = int(input())
li = []
best = [0 for _ in range(n+1)]
for i in range(n):
    li.append(list(map(int, input().split())))

for i in range(len(li)):
    t = li[i][0]
    p = li[i][1]
    if i+t >= n+1:
        continue

    elif best[i+t] < p + best[i]:
        for j in range(i+t, n+1):
            if best[j] < p + best[i]:
                best[j] = p + best[i]
    
    elif best[i+t] == 0:
        for j in range(i+t, n+1):
            if best[j] < p + best[i]:
                best[j] = p + best[i]


print(max(best))