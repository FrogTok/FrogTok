# O(N^2) 이지만 거의 정렬된 상태라면 O(N)이 걸린다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i, 0, -1):
        if (array[j] < array[j - 1]):
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)