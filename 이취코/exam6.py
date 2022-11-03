import heapq

# 최소힙
def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)
    
    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result

# 최대 힙
# def heapsort(iterable):
#     h = []
#     result = []

#     for value in iterable:
#         heapq.heappush(h, -value)
    
#     for _ in range(len(h)):
#         result.append(-heapq.heappop(h))

#     return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)