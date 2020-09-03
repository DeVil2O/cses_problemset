n = int(input())
l = list(map(int, input().split()))
count = 0
pre = l[0]
for i in range(1, n):
    if pre > l[i]:
        count += pre - l[i]
    else:
        pre = l[i]

print(count)
