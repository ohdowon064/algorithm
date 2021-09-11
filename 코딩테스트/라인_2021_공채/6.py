"""
문제
1. 재구매율 기준 상품 정렬
2. 재구매율 : 상품 재구매 고객 수
3. 재구매율 = (상품 재구매 고객 수) / (상품 한번 이상 구매 고객 수) * 100
    -> 단 기간 산정 필요
4. 모든 달은 30일 까지
5. records : 구매기록
6. k : 재구매기간
7. date : 재구매율 기준 날짜

알고리즘
1.
"""

def solution(records, k, date):
    date = list(map(int, date.split('-')))
    start = date.copy()
    start[2] -= k - 1
    if start[2] <= 0:
        start[1] -= 1
        if start[1] == 0:
            start[0] -= 1
            start[1] = 12
        start[2] += 30

    record_list = []
    products = set()
    users = set()

    for record in records:
        record = record.split()
        record[0] = list(map(int, record[0].split('-')))
        if start <= record[0] <= date:
            record_list.append(record)
            products.add(record[2])
            users.add(record[1])

    for p in list(products):



records = ["2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1", "2020-02-27 uid3 pid2", "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3", "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1", "2020-03-04 uid2 pid1", "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3", "2020-03-06 uid1 pid4"]
k = 10
date = "2020-03-05"
solution(records, k, date)