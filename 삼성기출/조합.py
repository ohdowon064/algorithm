# n개 중 k개 고르고 그 중 최소, 최대 구하기
def task(comb):
    print(comb)

k = 3
numbers = [1, 2, 3, 4, 5]

def dfs(comb: list, depth: int):
    if len(comb) == k:
        task(comb)
        return

    if depth == len(numbers):
        return

    comb.append(numbers[depth])
    dfs(comb, depth + 1)
    comb.pop()
    dfs(comb, depth + 1)

dfs([], 0)