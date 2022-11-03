from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']
result = list(permutations(data, 2))
print(result)

result = list(combinations(data, 2))
print(result)

result = list(product(data, repeat = 2))
print(result)

result = list(combinations_with_replacement(data, r = 2))
print(result)