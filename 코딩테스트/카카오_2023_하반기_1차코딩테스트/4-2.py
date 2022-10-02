def to_bin(n):
    temp = []
    while n > 0:
        r = n % 2
        n //= 2
        temp.append(r)
    l = 1
    a = 1
    while len(temp) - l > 0:
        a *= 2
        l += a
    while len(temp) < l:
        temp.append(0)
    temp.reverse()
    return temp


def check(binary):
    if sum(binary) == 0:
        return True

    mid = len(binary) // 2
    if binary[mid] == 0:
        return False
    return check(binary[:mid]) and check(binary[mid + 1:])


def solution(numbers):
    return [1 if check(to_bin(n)) else 0 for n in numbers]


if __name__ == '__main__':
    numbers = [1, 2, 3, 1000000000000000]
    print(solution(numbers))