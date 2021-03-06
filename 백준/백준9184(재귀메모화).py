memo = {}

def w(a,b,c):
    if (a,b,c) in memo:
        return memo[a,b,c]

    elif a <= 0 or b <= 0 or c <= 0:
        memo[a,b,c] = 1
        return 1

    elif a > 20 or b > 20 or c > 20:
        k = w(20, 20, 20)
        memo[a,b,c] = k
        return k

    elif a < b and b < c:
        k = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        memo[a,b,c] = k
        return k

    else:
        k = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        memo[a,b,c] = k
        return k

while True:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) =".format(a,b,c),w(a,b,c))
