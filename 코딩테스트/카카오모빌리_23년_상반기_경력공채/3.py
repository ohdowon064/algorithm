from collections import defaultdict


def solution(N, S):
    bookings = defaultdict(set)
    alpha = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "J": 8, "K": 9}
    for booking in S.split():
        row, col = int(booking[:-1]), booking[-1]
        bookings[row].add(alpha[col])

    result = (N - len(bookings)) * 2
    side = {1, 2, 7, 8}
    mid = {3, 4, 5, 6}
    left = {1, 2, 3, 4}
    right = {5, 6, 7, 8}

    for cols in bookings.values():
        if not (cols & side.union(mid)):
            result += 2

        elif (cols & side) and not (cols & mid):
            result += 1

        elif (cols & left) and not (cols & right):
            result += 1

        elif (cols & right) and not (cols & left):
            result += 1

    return result


solution(22, "1A 3C 2B 20G 5A")


