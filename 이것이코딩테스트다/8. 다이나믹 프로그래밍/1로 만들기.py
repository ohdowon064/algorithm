# n = int(input())

def function(number, count):
    result = []
    if number and number % 5 == 0:
        result.append((number // 5, count + 1))
    else:
        result.append((None, None))
    if number and number % 3 == 0:
        result.append((number // 3, count + 1))
    else:
        result.append((None, None))
    if number and number % 2 == 0:
        result.append((number // 2, count + 1))
    else:
        result.append((None, None))
    result.append((number - 1, count + 1))
    return result

from collections import deque

def bfs(n):
    q = deque([])
    q.append(function(n, 0))
    while q:
        data = q.popleft()

        for number, count in data:
            if not number:
                continue
            if number == 1:
                return count
            else:
                q.append(function(number, count))

print(bfs(26))