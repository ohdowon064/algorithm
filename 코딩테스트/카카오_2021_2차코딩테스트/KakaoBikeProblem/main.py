import random

from 코딩테스트.카카오_2021_2차코딩테스트.KakaoBikeProblem.kakao_api import KakaoAPI
from 코딩테스트.카카오_2021_2차코딩테스트.KakaoBikeProblem.utils import Truck, get_loaded_bikes_count, get_move_command, \
    get_truck_command


def solution(kakao_api: KakaoAPI):
    bikes = [0 for _ in range(kakao_api.size ** 2)]
    prev_bikes = [kakao_api.bike_count_init for _ in range(kakao_api.size ** 2)]

    trucks = [Truck() for _ in range(kakao_api.truck_count)]
    move_commands = [[] for _ in range(kakao_api.truck_count)]

    for try_number in range(720):
        truck_ends = [
            int(random.uniform(0, kakao_api.size ** 2)) for _ in range(kakao_api.truck_count)
        ]

        min_cnt = 9999999
        max_cnt = -min_cnt
        min_id = max_id = 0

        ref_values = [prev_bikes[i] - bikes[i] for i in range(len(bikes))]
        for i, cnt in enumerate(ref_values):
            if min_cnt > cnt:
                min_cnt, min_id = cnt, i
            if max_cnt < cnt:
                max_cnt, max_id = cnt, i

        trucks = get_loaded_bikes_count(kakao_api, trucks)

        emergency = [i for i, cnt in enumerate(bikes) if cnt == 0]

        i = 0
        while i < min(min_cnt // 20, kakao_api.truck_count):
            truck_ends[i] = min_id
            i += 1

        while i < min(max_cnt // 20, kakao_api.truck_count):
            truck_ends[i] = max_id
            i += 1

        for i in range(kakao_api.truck_count):
            truck = trucks[i]
            if len(emergency) > 0:
                truck_ends[i] = emergency.pop()

            move_commands[i] = get_move_command(kakao_api.id_to_index,
                                                truck.location_id,
                                                truck_ends[i])
        truck_commands = []
        for i in range(kakao_api.truck_count):
            truck = trucks[i]
            truck_command = get_truck_command(truck,
                                              bikes,
                                              kakao_api.locations,
                                              kakao_api.id_to_index,
                                              move_commands[i],
                                              kakao_api.ref_value)

            truck_commands.append(
                dict(truck_id=i, command=truck_command)
            )

        res_body = kakao_api.simulate_api(truck_commands)
        if try_number % 50 == 0:
            print(res_body)

        prev_bikes = bikes.copy()

if __name__ == "__main__":
    kakao_api_1 = KakaoAPI(1)
    solution(kakao_api_1)
    score1 = kakao_api_1.score_api()
    print(f"{'=' * 10}첫번째 스코어{'=' * 10}")
    print(score1)

    kakao_api_2 = KakaoAPI(2)
    solution(kakao_api_2)
    score2 = kakao_api_2.score_api()
    print(f"{'=' * 10}두번째 스코어{'=' * 10}")
    print(score2)
