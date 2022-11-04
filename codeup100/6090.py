a, m, d, n = map(int, input().split())

n_seq = a

for _ in range(1, n):
    n_seq = (n_seq * m) + d

print(n_seq)