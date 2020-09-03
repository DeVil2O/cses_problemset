s = input()
m = 0
c = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
    else:
        m = max(m, c)
        c = 1
m = max(m, c)
print(m)
