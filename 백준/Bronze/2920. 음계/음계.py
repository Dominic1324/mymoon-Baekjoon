li = list(map(int, input().split()))
li_a = [i+1 for i in range(8)]
li_d = [8-i for i in range(8)]
if li == li_a:
    print("ascending")
elif li == li_d:
    print("descending")
else:
    print("mixed")