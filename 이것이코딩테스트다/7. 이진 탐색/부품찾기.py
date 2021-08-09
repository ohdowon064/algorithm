import sys
input = sys.stdin.readline

n = int(input())
total = list(map(int, input().split()))
total.sort()

m = int(input())
request = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else: # array[mid] < target
            start = mid + 1
    return None

for target in request:
    if binary_search(total, target, 0, n-1) == None:
        print("no")
    else:
        print("yes")
