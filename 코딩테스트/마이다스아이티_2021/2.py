"""
    1. 팀단위
    2. 팀 인원제한 없음 - 혼자 가능
    3. 팀원 벌점 -> 팀 상점 깎음
    4. 상점 음수 가능
    5. 대표 : 가장 작은 번호 학생
    6. (학생번호, 상벌점)
    7. 양수 : 상점, 음수 : 벌점

    출력 : 높은 상점 팀 대표 번호
    복수 -> 대표번호 낮은 팀
"""

# n = 10
# v1 = [1, 10, 6, 5, 6, 9]
# v2 = [3, 7, 2, 8, 7, 3]
# num = [3, 4, 5, 1, 8, 7, 9, 2]
# amount = [10, 7, 6, -6, -8, 2, -2, 5]

n = 4
v1 = [1, 3]
v2 = [2, 4]
num = [2, 2]
amount = [1, -2]

parents = [i for i in range(n)]

def find(x):
    if x == parents[x]:
        return x
    return find(parents[x])

def merge(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if x < y:
        x, y = y, x
    parents[x] = y

for i in range(len(v1)):
    merge(v1[i] - 1 , v2[i] - 1)

teams = []
for i, k in enumerate(parents):
    if i == k:
        teams.append(set([i + 1]))

for i, k in enumerate(parents):
    parent = find(i)
    if i == parent:
        continue
    for j in range(len(teams)):
        if parent + 1 in teams[j]:
            teams[j].add(i + 1)
            break


teams = [{1, 3, 9}, {2, 6, 7, 10}, {4}, {5, 8}]
scores = [0] * len(teams)


for number, score in zip(num, amount):
    for i, team in enumerate(teams):
        if number in team:
            scores[i] += score

result = list(zip(teams, scores))
print(min(sorted(result, key=lambda x : (x[1], -min(x[0])), reverse=True)[0][0]))


