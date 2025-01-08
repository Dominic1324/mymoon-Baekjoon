n = int(input())
f = 0
s = 0
cnt = 0
if n < 10:
    s = n
else:
    f = n//10
    s = n%10

cnt+=1
new1 = f+s
f = s
s = new1%10

while n != f*10 + s:
    cnt+=1
    new1 = f+s
    f = s
    s = new1%10

print(cnt)


