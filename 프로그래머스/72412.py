"""
문제
1. cpp, java, python
2. backend, frontend
3. junior, senior
4. chicken, pizza
5. [조건] 중 x점 이상인 사람 수
6. -는 고려 안함

알고리즘
1. 중첩 filter
"""
import re

def solution(info, query):
    # 지원자 정보
    people = [p.split() for p in info]
    # print(people)

    ans = []
    # 쿼리
    for _q in query:
        # 쿼리 전처리
        q = re.split(r' and | ', _q)
        # print(q)

        # 중첩 필터
        this = people.copy()
        for i in range(4):
            if q[i] == '-':
                continue
            this = list(filter(lambda x: x[i] == q[i], this))

        # X점 이상 필터
        this = list(filter(lambda x: int(x[4]) >= int(q[4]), this))

        ans.append(len(this))

    return ans



info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info, query)