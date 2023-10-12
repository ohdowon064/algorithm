
k = 3
some_list = list(range(6))
visited = set()
result = 0
def dfs(perm):
    global result
    if len(perm) == k:
        print(perm)
        result += 1
        return

    for i, val in enumerate(some_list):
        if i in visited:
            continue

        perm.append(val)
        visited.add(i)
        dfs(perm)
        visited.discard(i)
        perm.pop()

dfs([])
print(result)