# 10-6 팀 결성

# 0~n번 학생에 대한 연산을 수행함. 
# 처음엔 모두 다른팀으로 간주 (각 번호에 해당하는 팀이라 생각하면됨.)
# 0이 입력되면, 팀합치기 연산을 수행한다.
# 1이 입력되면, 두 학생이 같은 팀에 속한지 확인한다.

# 입력 예시
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
# 출력 예시
# NO
# NO
# YES

def find_root(parents, a):
    if (parents[a] != a):
        parents[a] = find_root(parents, parents[a])
    return parents[a]

def union(parents, a, b):
    root_a = find_root(parents, a)
    root_b = find_root(parents, b)

    if (root_a < root_b):
        parents[root_b] = root_a
    else:
        parents[root_a] = root_b

n, m = map(int, input().split())

parents = [ i for i in range(n + 1)]
results = []

for _ in range(m):
    oper, a, b = map(int, input().split())

    if (oper == 0):     # 팀 합치기
        union(parents, a, b)
    elif(oper == 1):   # 같은 팀 여부 확인
        results.append(find_root(parents, a) == find_root(parents, b))

for result in results:
    if (result == True):
        print("YES")
    else:
        print("NO")