def suum(k,n):
    if n == 1:
        return 1
    elif k == 0:
        return n
    else:
        return suum(k,n-1) + suum(k-1,n)

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    print(suum(k,n))
