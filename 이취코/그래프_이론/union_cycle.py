# 10-4 서로소 집합을 활용한 사이클 판별 소스코드
# 입력 예시
# 3 3
# 1 2
# 1 3
# 2 3
# 출력 예시 
# 사이클이 발생했습니다.

n, m = map(int, input().split())

parents = [i for i in range(n + 1)]

is_cycle = False

def find_root(node):
    if(parents[node] != node):
        parents[node] = find_root(parents[node])
    return parents[node]

for _ in range(m):
    n1, n2 = map(int, input().split())
    root_n1 = find_root(n1)
    root_n2 = find_root(n2)
    if (root_n1 < root_n2):
        parents[root_n2] = root_n1
    elif(root_n1 > root_n2):
        parents[root_n1] = root_n2
    else:
        cycle = True
        break

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")

