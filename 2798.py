n, m = map(int, input().split())
l = list(map(int, input().split()))

output = 0

for a in range(n-2):
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            now = l[a]+l[b]+l[c]
            if (now <= m) and (now > output):
                output = now
print(output)
