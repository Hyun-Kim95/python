n = int(input())

k = []
for i in range(n):
    [a, b] = map(int, input().split())
    k.append([a, b])

k = sorted(k)

for i in range(n):
    print(k[i][0], k[i][1])
