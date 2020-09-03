import math
n = int(input())
l = []
if n == 1:
    print(n)
elif n == 4:
    print(2, 4, 1, 3)
elif 1 < n < 5:
    print("NO SOLUTION")
else:
    for i in range(int(math.ceil(n/2))):
        l.append(2 * i + 1)
    x = int(math.ceil(n/2))
    if n % 2 == 0:
        x = int(math.ceil(n/2))+1
    for i in range(1, x):
        l.append(2*i)
    print(*l)
