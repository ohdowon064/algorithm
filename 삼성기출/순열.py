# n개 중 순서를 고려하여 k개를 고르기

def task(perm):
    print(perm)

k = 3
numbers = list(range(6))

visited = set()
result = []

def dfs(perm: list):
    if len(perm) == k:
        result.append(perm.copy())
        task(perm)
        return

    for i, number in enumerate(numbers):
        if i in visited:
            continue

        perm.append(number)
        visited.add(i)
        dfs(perm)
        perm.pop()
        visited.discard(i)



def generate_permutations(data, k, current_permutation=[]):
    if len(current_permutation) == k:
        print(current_permutation)
        return
    for i in range(len(data)):
        generate_permutations(data[:i] + data[i+1:], k, current_permutation + [data[i]])

# 사용 예:
data = [1, 2, 3, 4, 5, 6]
k = 3
generate_permutations(data, k)


def dfs2(perm):
    if len(perm) == k:
        print(perm)
        return

    for i, val in enumerate(numbers):
        if i in visited:
            continue

        perm.append(val)
        visited.add(i)
        dfs(perm)
        visited.discard(i)
        perm.pop()


dfs([])
# print(result)