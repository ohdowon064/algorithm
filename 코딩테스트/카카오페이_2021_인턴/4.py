from collections import defaultdict
ages = [35,25,3,8,7]
wires = [[1,2,5],[2,1,5],[1,3,2],[3,4,2],[3,5,20],[4,5,1]]

graph = defaultdict(list)
for u, v, w in wires:
    graph[v].append(w)

death = []
for i in range(max(ages)- min(ages) + 1):
    ages = list(map(lambda x: x - i, ages))

    for j in range(len(ages)):
        if ages[j] == 0:
            death.append(j + 1)

