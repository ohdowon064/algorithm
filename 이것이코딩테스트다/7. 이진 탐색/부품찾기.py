n = int(input())
total = list(map(int, input().split()))
total.sort()

m = int(input())
items = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

check_list = [0] * 1000001
for number in total:
    check_list[number] += 1

answer = []
for item in items:
    # if binary_search(total, item, 0, n - 1):
    #     answer.append("yes")
    # else:
    #     answer.append("no")
    if check_list[item]:
        answer.append('yes')
    else:
        answer.append('no')

print(*answer)