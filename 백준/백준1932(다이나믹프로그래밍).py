n = int(input())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))                 //     .    이런 모양으로 들어감
                                                              //    . .
k = 2    // 두번째 줄부터 진행할거라서                          //   . . .
                                                              //  . . . .
for i in range(1, n):                                         // . . . . .
    for j in range(k):
        if j == 0:
            t[i][j] = t[i][j] + t[i - 1][j]                         // 제일 왼쪽 줄들의 합
        elif i == j:
            t[i][j] = t[i][j] + t[i - 1][j - 1]                     // 제일 오른쪽 줄들의 합
        else:
            t[i][j] = max(t[i - 1][j - 1], t[i - 1][j]) + t[i][j]   // 나머지는 바로 위랑 그 왼쪽 중에 큰 수를 더해주는 식으로 진행
    k += 1

print(max(t[n - 1]))
