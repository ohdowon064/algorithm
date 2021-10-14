"""
알고리즘
1. 본인이 속한 라인생성
2. 해당 라인에 for문을 돌면서 수익분배
"""

def solution(enroll, referral, seller, amount):
    line = {person: [] for person in enroll}

    for i, parent in enumerate(referral):
        if parent != "-":
            line[enroll[i]].extend([parent] + line[parent])

    print(line)
    sales = list(map(lambda x: x * 100, amount))
    incomes = {person: 0 for person in enroll}

    for person, sale in zip(seller, sales):
        incomes[person] += sale - sale // 10
        sale = sale // 10

        for parent in line[person]:
            if sale < 10:
                incomes[parent] += sale
                break
            incomes[parent] += sale - sale // 10
            sale = sale // 10

    return list(incomes.values())




enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
solution(enroll, referral, seller, amount)