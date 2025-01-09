a, b = 0, 0
while True:
    try:
        a,b = map(int,input().split())
    except:
        break
    print(a+b)