from typing import List

command = ['not', 'up', 'right', 'down', 'left', 'in', 'out']
truck_command = {command[i]: i for i in range(7)}
dx = [0, -1, 0, 1, 0, 0, 0]
dy = [0, 0, 1, 0, -1, 0, 0]


class Truck:
    def __init__(self):
        self.location_id = 0
        self.number_of_bikes = 0

    def __str__(self):
        return f"{self.id}: {self.number_of_bikes}"


def get_number_of_bikes_by_id(locations: List[dict], bikes: List[int]):
    for location in locations:
        id, number_of_bikes = location["id"], location["located_bikes_count"]
        bikes[id] = number_of_bikes

    return bikes

def get_number_of_bikes_by_truck(truck_infos: List[dict], trucks: List[Truck]):
    for truck in truck_infos:
        id, location_id, number_of_bikes = truck["id"], truck["location_id"], truck["loaded_bikes_count"]
        trucks[id].location_id = location_id
        trucks[id].number_of_bikes = number_of_bikes

    return trucks

def dist(pos, start, end):
    row, col = 0, 1

    up_down_dist = abs(pos[start][row] - pos[end][row])
    move_command = [truck_command['up'] for _ in range(up_down_dist)
                if pos[start][row] > pos[end][row]]

    move_command.extend(
        [truck_command['down'] for _ in range(up_down_dist)
        if pos[start][row] < pos[end][row]]
    )

    left_right_dist = abs(pos[start][col] - pos[end][col])
    move_command.extend(
        [truck_command['right'] for _ in range(left_right_dist)
        if pos[start][col] < pos[end][col]]
    )
    move_command.extend(
        [truck_command['left'] for _ in range(left_right_dist)
        if pos[start][col] > pos[end][col]]
    )

    return move_command

def truck_command_operation(truck: Truck, bikes: List[int], pos, rentals, command, mean):
    row, col = pos[truck.location_id]
    return_command = []

    for i in command:
        if len(return_command) >= 10: break
        id = rentals[row][col]

        if bikes[id] < mean:
            needs = min(mean - bikes[id], truck.number_of_bikes)
            return_command.extend(
                [truck_command['out'] for _ in range(needs) if needs > 0]
            )
            bikes[id] += needs

        elif bikes[id] > mean:
            needs = min(bikes[id] - mean, 20 - truck.number_of_bikes)
            return_command.extend(
                [truck_command['in'] for _ in range(needs) if needs > 0]
            )

        return_command.append(i)
        row += dx[i]
        col += dy[i]

    return return_command



