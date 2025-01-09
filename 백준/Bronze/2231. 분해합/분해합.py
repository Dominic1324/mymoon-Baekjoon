n = int(input())
for i in range(1, n+1):
    str_i = str(i)
    ja = 0
    for j in str_i:
        ja += int(j)
    
    if ja+i == n:
        print(i)
        break

    if i == n:
        print(0)
