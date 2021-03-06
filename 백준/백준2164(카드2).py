import sys                      # 2164 카드2    맨위는 무조건 1이고 밑으로 갈 수록 1씩 커지는 n장의 카드덱에서 맨위의 카드는 버리고
n = int(sys.stdin.readline())   #               다음 카드는 덱의 바닥으로 보내는 동작을 반복할 때 마지막 남은 카드의 숫자를 맞추는 코드
a = [i for i in range(1,n+1)]   # 1부터 n까지의 숫자를 받음
while len(a) > 1:               # 카드덱이 한장이 될때까지 반복
    if len(a) % 2:              # 카드 수가 홀수개라면(조건이 0이 아니어야 실행하므로)
        t = [a[-1]]             # t리스트에 a의 마지막 숫자 추가
        t.extend(a[1::2])       # 후에 a[1] 부터 2칸 간격으로 t에 추가해줌(즉, 짝수번째 카드들을 뒤로 넣어줌)
        a = t                   # a를 t로 바꿈
    else:                       # 카드 수가 짝수라면 그냥 짝수번째 카드만 남김
        a = a[1::2]
print(a[0])
