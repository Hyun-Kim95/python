from itertools import permutations  # 중복되지 않는 수열찾기
N, M = map(int, input().split())
P = permutations(range(1, N+1), M)  # 1부터 N까지 M개씩
for i in P:
    print(*i)

#-------------------------------------------------------------아래는 중복제거 밑 오름차순
from itertools import permutations  # 중복되지 않는 수열찾기
N, M = map(int, input().split())
P = permutations(range(1, N+1), M)  # 1부터 N까지 M개씩

P = sorted(P)
Q = []
for j in range(len(P)):
    P[j] = sorted(P[j])

for k in range(len(P)):
    if P[k] not in Q:
        Q.append(P[k])

for i in Q:
    print(*i)

#----------------------------------------------------------아래는 중복가능 밑 오름차순
from itertools import product           # product : 모든중복 가능 밑 오름차순 수열
N, M = map(int, input().split())
P = product(range(1, N+1), repeat=M)    # repeat= : 길이

for i in P:
    print(*i)

#-------------------------------------------------------아래는 중복가능 밑 비내림차순 수열
from itertools import combinations_with_replacement         # combinations_with_replacement: 중복가능 비내림차수
N, M = map(int, input().split())
P = combinations_with_replacement(range(1, N+1), M)

for i in P:
    print(*i)
