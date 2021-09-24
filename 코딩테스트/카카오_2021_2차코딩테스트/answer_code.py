import requests
import random
import json

"""
1. 해당 장소 자전거가 많으면 여분의 자전거를 올린다.
2. 해당 장소 자전거가 적으면 자전거를 내린다.
3. 자전거 많고 적고 기준은 임의로 기준값 설정
-> 기준값을 바꿔가면서 score 비교
"""
action = ['not', 'up', 'right', 'down', 'left', 'in', 'out']
truck_command = {action[i]: i for i in range(7)}
dx = [0, -1, 0, 1, 0, 0, 0]
dy = [0, 0, 1, 0, -1, 0, 0]

# 트럭 클래스
class Truck:
    def __init__(self):
        self.p = 0
        self.number_of_bikes = 0

    def __str__(self):
        return f"{self.p}: {self.number_of_bikes}"

# 각 id별 바이크 수를 bikes 배열에 저장
def get_location(url, headers, bikes):
    path = '/locations'
    res = requests.get(url + path, headers=headers)
    res_body = res.json()

    for location in res_body["locations"]:
        id, cnt = location["id"], location["located_bikes_count"]
        bikes[id] = cnt

    return bikes

# 트럭들의 위치와 상차한 바이크 수를 trucks 배열에 저장
def get_truck(url, headers, trucks):
    path = "/trucks"
    res = requests.get(url + path, headers=headers)
    res_body = res.json()

    for truck in res_body["trucks"]:
        id, p, cnt = truck["id"], truck["location_id"], truck["loaded_bikes_count"]
        trucks[id].p = p
        trucks[id].number_of_bikes = cnt

    return trucks

# simulate api
def simulate(url, headers, data):
    path = '/simulate'
    res = requests.put(url + path, headers=headers, json=data)
    return res.json()

# f부터 t까지 이동하기 위한 command를 commands에 저장
def get_dist(loc, f, t):
    commands = [truck_command['up'] for i in range(
        abs(loc[f][0] - loc[t][0])
    ) if loc[f][0] > loc[t][0]]
    commands.extend(
        truck_command['down'] for i in range(
            abs(loc[f][0] - loc[t][0])
        ) if loc[f][0] < loc[t][0]
    )
    commands.extend(
        truck_command['right'] for i in range(
            abs(loc[f][1] - loc[t][1])
        ) if loc[f][1] < loc[t][1]
    )
    commands.extend(
        truck_command['left'] for i in range(
            abs(loc[f][1] - loc[t][1])
        ) if loc[f][1] > loc[t][1]
    )

    return abs(loc[f][0] - loc[t][0]) + abs(loc[f][1] - loc[t][1]), commands

def truck_move(truck, bikes, map, mmap, comm, mean):
    x, y = map[truck.p]
    retcomm = []

    for i in comm:
        # simulate api에 전달할 수 있는 트럭 명령어는 최대 10개
        if len(retcomm) >= 10: break
        id = mmap[x][y]

        if bikes[id] < mean:
            # 자전거수가 평균보다 작으면 트럭의 자전거를 내려준다.
            need = min(mean - bikes[id], truck.number_of_bikes)
            retcomm.extend([truck_command['out'] for _ in range(need) if need > 0])
            bikes[id] += need
        elif bikes[id] > mean:
            # 자전거수가 평균보다 많으면 트럭이 자전거를 가져간다.
            need = min(bikes[id] - mean, 20 - truck.number_of_bikes)
            retcomm.extend([truck_command['in'] for _ in range(need) if need > 0])
            bikes[id] -= need
        retcomm.append(i)
        x += dx[i]
        y += dy[i]

    return retcomm

def main(qid = 1):
    url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
    path = "/start"
    token = "bd593a88021457860daad0e3110417ee"

    param = {"problem": qid}
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

    msize = None
    mean = None
    # 문제 1번과 2번에 따라서 값을 정해놓는다.
    if qid == 1:
        msize = 5
        mean = 2
    else:
        msize = 60
        mean = 3

    """
    mymap: 지도 id를 만듦
    
    4 9 14 19 24
    3 8 13 18 23
    2 7 12 17 22
    1 6 11 16 21
    0 5 10 15 20 
    """

    mymap = [[msize - i -1 + msize*j for j in range(msize)] for i in range(msize)]
    pos = {mymap[i][j] : (i, j) for i in range(msize) for j in range(msize)}

    bikes = [0 for i in range(msize * msize)]
    truck_number = [0, 5, 10] # 1번문제 트럭 5대, 2번문제 트럭 10대
    trucks = [Truck() for i in range(truck_number[qid])]

    res = requests.post(url + path, headers = headers,  json=param)
    res_body = res.json()

    auth_key = res_body['auth_key']
    headers = {"Authorization": auth_key, "Content-Type": "application/json"}

    next_command = [[] for i in range(len(trucks))]
    bikes_number = [0, 4, 3] # 1번문제 초기 id마다 자전거 4대씩, 2번 3대씩
    prev_bikes = [bikes[qid] for i in range(msize*msize)]

    for _ in range(720): # 720번 수행
        # 트럭의 목적지를 랜덤으로 설정한다.
        trucks_des = [int(random.uniform(0, msize * msize)) for i in range(len(trucks))]

        mmin = 99999999999
        mmax = -mmin
        min_idx = max_idx = 0

        stand = [prev_bikes[i] - bikes[i] for i in range(len(bikes))]
        for i, v in enumerate(stand):
            if mmin > v:
                mmin, min_idx = v, i
            if mmax < v:
                mmax, max_idx = v, i

        trucks = get_truck(url, headers, trucks)
        emergen = [idx for idx, bike in enumerate(bikes) if bike == 0]

        i = 0
        while i < min(int(mmin/20), truck_number[qid]):
            trucks_des[i] = min_idx
            i += 1
        while i < min(int(mmax/20), truck_number[qid]):
            trucks_des[i] = max_idx
            i += 1

        for i in range(truck_number[qid]):
            truck = trucks[i]
            if len(emergen) > 0:
                trucks_des[i] = emergen.pop()
            idx, next_command[i] = get_dist(pos, truck.p, trucks_des[i])

        final_command = []
        for i in range(truck_number[qid]):
            truck = trucks[i]
            ncom = truck_move(truck, bikes, pos, mymap, next_command[i], -1)
            final_command.append({'truck_id': i, 'command': ncom})

        res_body = simulate(url, headers=headers, data={'commands': final_command})
        print(res_body['time'])
        prev_bikes = [i for i in bikes]

    res = requests.get(url + '/score', headers=headers)
    print(res.json())

# main()
# main(2)















