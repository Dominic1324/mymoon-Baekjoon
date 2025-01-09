li = [-1 for _ in range(26)]
s = input()
for i in range(len(s)):
    if li[ord(s[i])-97] == -1:
        li[ord(s[i])-97] = i 
for i in li:
    print(i, end=" ")