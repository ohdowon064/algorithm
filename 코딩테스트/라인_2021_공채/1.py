"""
문제
1. 신입, 재학생 일렬
2. 그룹 한개 생성
3. 그룹 내 그룹아닌 학생있으면 안됨.
4. 그룹에는 재학생 정확히 k명
5. 신입생 수 제한 x -> 0~무한
6. student : 학생 일렬, 0:신입, 1:재학
7. k : 재학생 수
8. 만들 수 있는 그룹 수

알고리즘
1. 재학생 집합 수, 좌우 0개수
2. (좌 + 우) + max(좌, 우) * min(좌, 우) + 1
"""

def solution(student, k):
    if sum(student) < k:
        return 0

    # 재학생 집합, 좌우 0개수
    r = []
    i = j = 0

    while i < len(student) and j < len(student):
        r_num = 0
        group = [0, 0]
        while r_num < k:
            if student[i] == 0:
                group[0] += 1
                i += 1
            elif student[i] == 1:
                r_num += 1
                j = i

                while j < len(student) and student[j] != 1:
                    j += 1




