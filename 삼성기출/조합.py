count = 0


def task(comb):
    global count
    print(comb)
    count += 1


k = 3
numbers = list(range(6))


def dfs(comb: list, depth: int):
    if len(comb) == 3:
        task(comb)
        return

    if depth == len(numbers):
        return

    comb.append(numbers[depth])
    dfs(comb, depth + 1)
    comb.pop()
    dfs(comb, depth + 1)


# dfs([], 0)
# print(count)

def combinations(elements, r):
    # 종료 조건: r이 0이면 빈 리스트를 반환
    if r == 0:
        yield []
    # 종료 조건: r이 elements의 길이보다 크면 빈 리스트를 반환
    elif r > len(elements):
        return
    # 첫 번째 요소를 선택하고 나머지 요소에서 r-1개를 선택
    else:
        for i in range(len(elements)):
            for combo in combinations(elements[i+1:], r-1):
                yield [elements[i]] + combo

# 사용 예:
elements = [1, 2, 3, 4, 5, 6]
r = 3
for combo in combinations(elements, r):
    print(combo)


def dfs(comb, depth):
    if len(comb) == k:
        task(comb)
        return

    if depth == len(numbers):
        return

    # numbers[depth]를 선택한 경우
    comb.append(numbers[depth])
    dfs(comb, depth + 1)

    # numbers[depth]를 선택하지 않은 경우
    comb.pop()
    dfs(comb, depth + 1)