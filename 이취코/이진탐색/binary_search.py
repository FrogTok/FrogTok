# 탐색 범위가 2000만이 넘어가면, 이진탐색을 고려해보자.

# 재귀함수를 이용한 이진탐색
def binary_search_recursive(array, target, start, end):
    if (start > end):
        return None
    mid = (start + end) // 2
    if (target == array[mid]):
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    else:
        return binary_search_recursive(array, target, mid + 1, end)

# 반복문을 이용한 이진탐색
def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (target == array[mid]):
            return mid
        elif(array[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target= map(int, input().split())
array = list(map(int, input().split()))

result = binary_search_recursive(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)