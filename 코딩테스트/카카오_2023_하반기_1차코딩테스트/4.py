import sys

sys.setrecursionlimit(5000)


def is_bin(number):
    mid = len(number) // 2
    if len(number) == 3:
        return number[mid] == "1" or number == "000"
    if len(number) < 3:
        return False

    if is_bin(number[:mid]) and is_bin(number[mid + 1:]):
        return True
    return False

def is_bin(number):
    if sum(number) == 0:
        return True

    mid = len(number) // 2
    if number[mid] == 0:
        return False
    return is_bin(number[:mid]) and is_bin(number[mid + 1:])


def solution(numbers):
    answer = []
    for i, number in enumerate(numbers):
        number = list(map(int, str(bin(number))[2:]))

        if is_bin(number):
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([0]))