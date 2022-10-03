n, m = map(int, input().split())
bars = list(map(int, input().split()))

def length(h):
    return sum(map(lambda x: x - h if x > h else 0, bars))

def binary_search(target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2

        if length(mid) == target:
            result = mid
            start = mid + 1
            continue

        if length(mid) > target:
            start = mid + 1
        else:
            end = mid - 1
    return result


print(binary_search(m, 0, max(bars)))
