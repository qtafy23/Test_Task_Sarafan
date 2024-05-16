n=int(input())
v = []

for i in range(1, n+1):
    c = min(n, i)
    n = n - c
    v += [str(i)] * c
    if n <= 0:
        break

print(" ".join(v))
