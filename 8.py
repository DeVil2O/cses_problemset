n = int(input())
if (n * (n + 1) // 2) % 2 == 1:
    print("NO")
else:
    x = n // 4
    a, b = [], []
    if n % 2 == 1:
        a = [n]
        j = 0
        for i in range(1, x + 1):
            a.append(i)
            a.append(n-i)
            j += 1
        for k in range(j+1, n - j):
            b.append(k)
    else:
        j = 0
        for i in range(1, x + 1):
            a.append(i)
            a.append(n-i+1)
            j += 1
        for k in range(j+1, n - j+1):
            b.append(k)
    print("YES")
    print(len(a))
    print(*sorted(a)[::-1])
    print(len(b))
    print(*sorted(b)[::-1])
