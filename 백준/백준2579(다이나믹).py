n = int(input())                            #2579

s = [0 for i in range(301)]                                       # 최대 300계단

dp = [0 for i in range(301)]                                      # 더해줄 리스트

for i in range(n):                                                # 계단별 점수를 받아옴
    s[i] = int(input())

dp[0] = s[0]                                                      # 더하기 시작

dp[1] = s[0] + s[1]

dp[2] = max(s[1] + s[2], s[0] + s[2])                             # 연속 3개를 밟을 수 없어서

for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])    # 마지막 계단을 무조건 밟아야 하므로 바로 그 전 계단을 밟는지 안밟는지 비교

print(dp[n - 1])
