"""
    문제
    1. (i, j) : i학생이 j학생에게 준 점수
    2. 자기 자신에게 준 점수가 유일한 최고점 또는 유일한 최저점일 경우 제외
    3. 기준
        90이상 : A
        80이상 : B
        70이상 : C
        50이상 : D
        50미만 : F
    4. 학점을 하나의 문자열로 출력
"""
from collections import defaultdict
scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
students = defaultdict(list)
ans = ""

for i in range(len(scores)):
    for j in range(len(scores)):
        students[j].append(scores[i][j])

for k, score in students.items():
    total = sum(score)
    cnt = len(score)
    if (score[k] == max(score) or score[k] == min(score)) and score.count(score[k]) == 1:
        total -= score[k]
        cnt -= 1

    avg = total / cnt
    if avg >= 90:
        ans += "A"
    elif avg >= 80:
        ans += "B"
    elif avg >= 70:
        ans += "C"
    elif avg >= 50:
        ans += "D"
    else:
        ans += "F"

print(ans)
