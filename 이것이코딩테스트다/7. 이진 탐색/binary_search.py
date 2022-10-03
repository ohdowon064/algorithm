def binary_search(arr, target, start, end):
    if start > end:
        return

    mid = (start + end) // 2

    if target == arr[mid]:
        return mid

    if arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    return binary_search(arr, target, mid + 1, end)

def binary_search_with_loop(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid

        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
