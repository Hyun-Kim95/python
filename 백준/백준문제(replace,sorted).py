a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()
for t in a:
    alpha = alpha.replace(t, '*')
    
print(len(alpha))

#replace(찾는값,바꿀값,[바꿀횟수]): 무조건 왼쪽부터, 바꿀횟수는 생략가능
#---------------------------------------------------------------------
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)

#sorted(함수,key=):키를 기준으로 함수를 정렬
#sorted(word, key=word.find): 'a'부터 정렬이 아니라 word에서 찾아지는
#                              character순서대로 정렬된다.
