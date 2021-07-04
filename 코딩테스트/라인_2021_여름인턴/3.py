from collections import defaultdict
from itertools import product
n = 2
data = ["a1 1 5 9", "a2 1 9 5", "b1 2 3 3"]
limit = "0 10"
limit = list(map(int, limit.split()))
best = []

algo = defaultdict(list)
for datum in data:
    datum = datum.split()
    index, info = datum[1], [datum[0], int(datum[2]), int(datum[3])]
    algo[index].append(info)

case = list(product(*[algo[k] for k in algo]))
print(case)

for c in case:
    time_complex = sum([algorithm[1] for algorithm in c])
    if limit[0] != 0 and time_complex > limit[0]:
        continue
    space_complex = sum([algorithm[2] for algorithm in c])
    if limit[1] != 0 and space_complex > limit[1]:
        continue

    best.append(([algorithm[0] for algorithm in c], time_complex + space_complex))

print(sorted(best, key=lambda x: (x[1], x[0]))[0][0])
