a = int(input())
b = int(input())
c = int(input())

e = list(str(a * b * c))
for i in range(10):
    print(e.count(str(i)))
#-----------------------------
arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))
#set함수는 중복을 제거하기 위한 필터역할
#---------------------------------------
t = int(input())

for i in range(t):
    a = list(input())
    S = 0
    c = 1
    for r in a:
        if r == 'O':
            S += c
            c += 1
        else:
            c = 1
    print(S)
