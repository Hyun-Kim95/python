n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')
#f-string 표기법
#따옴표 앞에 f를 붙혀서 표현, {}안에 변수 삽입가능
#f-string 중괄호 { } 안에서 : 구분자를 이용하고 : 구분자 오른편에. 자릿수 f를 써준다.
#자릿수 뒤에 붙는 f는 실수의 f를 의미한다.
#-----------------------------------------------------------------------------------
num = set(range(1,10001))

generated_num = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)
self_num = num - generated_num
for k in sorted(self_num):
    print(k)

#set() 함수로 만든 집합은 add() 함수로 새로운 요소를 추가
#sorted(): 숫자의 오름차순정렬
