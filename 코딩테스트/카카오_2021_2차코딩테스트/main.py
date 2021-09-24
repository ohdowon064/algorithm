import random

from 코딩테스트.카카오_2021_2차코딩테스트.kakao_bike import KakaoAPI
from 코딩테스트.카카오_2021_2차코딩테스트.utils import Truck, get_number_of_bikes_by_truck, dist, truck_command_operation

def solution(kakao_api: KakaoAPI):
    bikes = [0 for _ in range(kakao_api.n ** 2)]
    prev_bikes = [kakao_api.bike_count for _ in range(kakao_api.n ** 2)]

    trucks = [Truck() for _ in range(kakao_api.truck_count)]
    commands = [[] for _ in range(len(trucks))]

    for try_cnt in range(720):
        trucks_end =[int(random.uniform(0, kakao_api.n ** 2)) for _ in range(len(trucks))]

        min_cnt = 99999
        max_cnt = -min_cnt
        min_idx = max_idx = 0

        stand = [prev_bikes[i] - bikes[i] for i in range(len(bikes))]
        for i, cnt in enumerate(stand):
            if min_cnt > cnt:
                min_cnt, min_idx = cnt, i
            if max_cnt < cnt:
                max_cnt, max_idx = cnt, i

        truck_info = kakao_api.trucks_api()
        trucks = get_number_of_bikes_by_truck(truck_info, trucks)
        emergency = [i for i, cnt in enumerate(bikes) if cnt == 0]

        i = 0
        while i < min(min_cnt // 20, len(trucks)):
            trucks_end[i] = min_idx
            i += 1

        while i < min(max_cnt // 20, len(trucks)):
            trucks_end[i] = max_idx
            i += 1

        for i in range(len(trucks)):
            truck = trucks[i]
            if len(emergency) > 0:
                trucks_end[i] = emergency.pop()

            commands[i] = dist(kakao_api.pos, truck.location_id, trucks_end[i])

        final_command = []
        for i in range(len(trucks)):
            truck = trucks[i]
            command = truck_command_operation(truck, bikes, kakao_api.pos, kakao_api.rentals, commands[i], kakao_api.mean)

            final_command.append(dict(truck_id=i, command=command))

        res_body = kakao_api.simulate_api(final_command)
        if try_cnt % 10 == 0:
            print(res_body)

        prev_bikes = bikes.copy()

if __name__ == "__main__":
    kakao_api_1 = KakaoAPI(1)
    solution(kakao_api_1)
    score1 = kakao_api_1.score_api()
    print(score1)

    kakao_api_2 = KakaoAPI(2)
    solution(kakao_api_2)
    score2 = kakao_api_2.score_api()
    print(score2)


