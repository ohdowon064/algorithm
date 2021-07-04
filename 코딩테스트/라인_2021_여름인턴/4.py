from collections import defaultdict
n = 4
queries = [[1,3],[1,2],[3,6],[3,-1],[4,5],[2,-1],[3,-1],[1,-1]]
mid = 0
stack = defaultdict(list)
pop_list = []

def empty():
    for s in stack.values():
        if s != []:
            return False
    return True

for query in queries:
    if query[1] == -1:
        if empty() and mid == 0:
            pop_list.append(-1)
        elif empty() and mid != 0:
            pop_list.append(mid)
            mid = 0
        elif stack[query[0]] == []:
            next = query[0] % n + 1
            while stack[next] == []:
                next = next % n + 1
            pop_list.append(mid)
            mid = stack[next][0]
            stack[next].pop(0)
        else:
            pop_list.append(stack[query[0]].pop())

    elif empty() and mid == 0:
        mid = query[1]
    else:
        stack[query[0]].append(query[1])

print(pop_list)