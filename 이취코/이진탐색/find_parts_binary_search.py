import sys

def binary_search(array, target, start, end):
    if (start > end):
        return False
    
    mid = (start + end) // 2

    if (array[mid] == target):
        return True
    elif (target < mid):
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

n = int(input())
array_n = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
array_m = list(map(int, sys.stdin.readline().rstrip().split()))

array_n.sort()

for target in array_m:
    if (binary_search(array_n, target, 0, n - 1)):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
