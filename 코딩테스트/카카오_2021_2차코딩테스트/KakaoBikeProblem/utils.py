from typing import List

from 코딩테스트.카카오_2021_2차코딩테스트.KakaoBikeProblem.kakao_api import KakaoAPI

command_list = ['not', 'up', 'right', 'down', 'left', 'in', 'out']
command_number = {command_list[i]: i for i in range(7)}
dx = [0, -1, 0, 1, 0, 0, 0]
dy = [0, 0, 1, 0, -1, 0, 0]

class Truck:
    def __init__(self):
        self.location_id = 0
        self.loaded_bikes_count = 0


def get_located_bikes_count(kakao_api: KakaoAPI, bikes):
    """
    {id: 자전거 수}인 dict를 bikes list로 변환하는 함수

    :param kakao_api: api 정보를 저장하고있는 KakaoAPI 객체
    :param bikes: 각 id마다 자전거 수를 저장하는 1차원 배열
    :return: 각 id마다 자전거 수를 bikes 배열에 저장하고 반환
    """
    locations = kakao_api.locations_api()
    for location in locations:
        id, located_bikes_count = location["id"], location["located_bikes_count"]
        bikes[id] = located_bikes_count

    return bikes


def get_loaded_bikes_count(kakao_api: KakaoAPI, trucks: List[Truck]):
    """
    {id: 트럭아이디, location_id: 현재 트럭 위치, loaded_bikes_count: 트럭이 상차한 자전거수} 정보를
    Truck 객체에 저장하는 함수

    :param kakao_api: api 정보를 저장하고있는 KakaoAPI 객체
    :param trucks: Truck 객체 리스트
    :return: 각 트럭들의 정보를 Truck 객체에 저장하고 Truck 객체 리스트를 반환한다.
    """
    truck_infos = kakao_api.trucks_api()
    for truck_info in truck_infos:
        id, location_id, loaded_bikes_count = truck_info["id"], truck_info["location_id"], truck_info["loaded_bikes_count"]

        trucks[id].location_id = location_id
        trucks[id].loaded_bikes_count = loaded_bikes_count

    return trucks


def get_move_command(id_to_index, start, end):
    """
    start id부터 end id까지의 이동 명령을 반환하는 함수

    :param id_to_index: id를 key로 가지고 index (row, col)을 value로 하는 dict
    :param start: 출발지점 id
    :param end: 도착지점 id
    :return: start부터 end까지 이동하는데 필요한 명령어(숫자)를 반환한다.
    """
    row, col = 0, 1

    up_down_dict = abs(id_to_index[start][row] - id_to_index[end][row])
    move_command = [
        command_number['up'] for _ in range(up_down_dict)
        if id_to_index[start][row] > id_to_index[end][row]
    ]
    move_command.extend([
        command_number['down'] for _ in range(up_down_dict)
        if id_to_index[start][row] < id_to_index[end][row]
    ])

    left_right_dist = abs(id_to_index[start][col] - id_to_index[end][col])
    move_command.extend([
        command_number["right"] for _ in range(left_right_dist)
        if id_to_index[start][col] < id_to_index[end][col]
    ])
    move_command.extend([
        command_number["left"] for _ in range(left_right_dist)
        if id_to_index[start][col] > id_to_index[end][col]
    ])

    return move_command

def get_truck_command(truck: Truck, bikes, locations, id_to_index, move_command, ref_value):
    row, col = id_to_index[truck.location_id]
    truck_command = []

    for move in move_command:
        if len(truck_command) >= 10: break
        id = locations[row][col]

        # 자전거 개수가 기준값보다 적다 -> 트럭에서 하차(out) 한다.
        if bikes[id] < ref_value:
            needs = min(ref_value - bikes[id], truck.loaded_bikes_count)
            truck_command.extend([
                command_number['out'] for _ in range(needs) if needs > 0
            ])

        # 자전거 개수가 기준값보다 많다. -> 트럭에서 상차(in) 한다.
        elif bikes[id] > ref_value:
            needs = min(bikes[id] - ref_value, 20 - truck.loaded_bikes_count)
            truck_command.extend([
                command_number['in'] for _ in range(needs) if needs > 0
            ])

        truck_command.append(move)
        row += dx[move]
        col += dy[move]

    return truck_command











