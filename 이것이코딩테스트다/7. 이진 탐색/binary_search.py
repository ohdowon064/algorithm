def binary_search_recursion(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursion(array, target, start, mid - 1)
    else: # array[mid] < target
        return binary_search_recursion(array, target, mid + 1, end)

def binary_search_iterate(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else: # array[mid] < target
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search_iterate(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result)