b = 0
n = int(input())
a = list(map(int,input().split()))
for j in range(n):
    k = 0
    if a[j] == 2:
        b += 1
    elif a[j] != 1:
        for q in range(2,a[j]):
            if a[j] % q == 0:
                break
            k += 1
        if k == a[j]-2:
            b += 1
            k = 0
print(b)
