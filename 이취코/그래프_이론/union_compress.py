# 10-2 경로압축 서로소 집합 알고리즘
# 입력 예시
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6
# 출력 예시
# 각 원소가 속한 집합: 1 1 1 1 5 5
# 부모 테이블: 1 1 1 1 5 5

n, m = map(int, input().split())

# i의 부모노드 값 저장
parents = [ i for i in range(n + 1)]

def find_root(node):
    if (parents[node] != node):
        parents[node] = find_root(parents[node])
    return parents[node]

for _ in range(m):
    n1, n2 = map(int, input().split())
    root_n1 = find_root(n1)
    root_n2 = find_root(n2)

    if (root_n1 < root_n2):
        parents[root_n2] = root_n1
    else:
        parents[root_n1] = root_n2

print("각 원소가 속한 집합:", end = ' ')
for node in range(1, n + 1):
    print(find_root(parents[node], node), end = ' ')
print("\n부모 테이블:", end = ' ')
for node in parents[1:]:
    print(node, end = ' ')
