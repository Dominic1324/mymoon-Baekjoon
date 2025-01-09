h, m = map(int, input().split())
if m>=45:
    print(h, m-45)
else:
    m = m-45+60
    if h == 0:
        print(23, m)
    else:
        print(h-1, m)