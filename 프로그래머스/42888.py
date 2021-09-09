"""
문제
1. record : Enter/Leave/Change {유저아이디} {닉네임}
2. 중복 닉네임 허용

알고리즘
1. 유저아이디를 키, 닉네임이 빈칸인 행동리스트를 value로 하는 dict 선언
2. 유저아이디를 키, 닉네임이 value로 하는 dict 선언
3. 행동 순서를 담고있는 act_order 리스트 선언
"""
from collections import defaultdict, deque

def solution(record):
    actions = {
        "Enter" : "{}님이 들어왔습니다.",
        "Leave" : "{}님이 나갔습니다."
    }
    order = []
    nicknames = defaultdict(str)
    user_record = defaultdict(deque)

    for action in record:
        todo = action.split()
        user_id = todo[1]

        if todo[0] in ["Enter", "Leave"]:
            order.append(user_id)
            user_record[user_id].append(actions["Enter"])

        elif todo[0] in ["Enter", "Change"]:
            nicknames[user_id] = todo[2]

    result = []
    for user_id in order:
        result.append(user_record[user_id].popleft().format(nicknames[user_id]))

    return result

records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(records))


