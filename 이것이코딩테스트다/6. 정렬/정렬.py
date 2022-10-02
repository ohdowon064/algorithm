# 선택정렬 - 범위 내에서 제일 작은 것을 선택하고 첫번째와 교환

def select_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    print(array)


select_sort([7, 5, 3, 8, 9, 4, 2, 1, 6])

# 삽입정렬 - 올바른 위치에 삽입하는 정렬

def insert_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break


# 퀵 정렬 - 피벗을 기준으로 작은 값, 큰 값으로 나누어 정렬

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left, right = start + 1, end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


arr = [7, 5, 3, 8, 9, 4, 2, 1, 6]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

def quick_sort_with_python(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_with_python(left_side) + [pivot] + quick_sort_with_python(right_side)
import random
random.shuffle(arr)
print(quick_sort_with_python(arr))

def counting_sort(arr):
    count = [0] * (len(arr) + 1)

    for i in arr:
        count[i] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=" ")

random.shuffle(arr)
counting_sort(arr)