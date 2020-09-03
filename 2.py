n = int(input())
l = list(map(int, input().split()))
s = sum(l)
dups = n * (n + 1) // 2
print(dups - s)
