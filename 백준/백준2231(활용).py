N = int(input())
print_num = 0
for i in range(1, N+1):
    div_num = list(map(int, str(i)))    #문자열로 바꿔서 각 자리수를 넣음
    sum_num = i + sum(div_num)          #원래숫자와 각 자리수들 더함
    if(sum_num == N):
        print_num = i
        break
print(print_num)
