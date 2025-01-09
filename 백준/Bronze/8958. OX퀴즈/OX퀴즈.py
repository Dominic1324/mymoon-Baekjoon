n = int(input())
for i in range(n):
    cnt = 1
    jum = 0
    m = input()
    for i in m:
        if i == "O":
            jum += cnt
            cnt += 1
        if i == "X":
            cnt = 1
    print(jum)
