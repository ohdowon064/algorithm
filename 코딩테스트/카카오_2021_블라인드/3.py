"""
문제
1. 입차, 출차 기록에서 주차요금 계산하기
2. 누적주차시간으로 계산
3. 출차없으면 23:59 출차

알고리즘
1. 시간계산기
2. 주차시간 누적
3. 기본, 단위로 요금계산
"""
from collections import defaultdict
from math import ceil


def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    print(fees)

    def parking_time(start, end='23:59'):
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        total = (end_h-start_h) * 60 + (end_m-start_m)
        return total

    cars = defaultdict(list)
    car_times = defaultdict(int)
    for record in records:
        t, car_id, move = record.split()
        if move == 'IN':
            cars[car_id].append(t)
        else:
            start = cars[car_id].pop()
            car_times[car_id] += parking_time(start, t)

    for car_id in cars.keys():
        if cars[car_id]:
            start = cars[car_id].pop()
            car_times[car_id] += parking_time(start)

    print(car_times)

    def calc_fee(total_time):
        if (remain_time := total_time - base_time) <= 0:
            return base_fee
        return base_fee + ceil(remain_time / unit_time) * unit_fee

    ans = []
    for car in sorted(cars.keys()):
        ans.append(calc_fee(car_times[car]))

    print(ans)
    return ans

# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
#
fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

# fees = [1, 461, 1, 10]
# records = ["00:00 1234 IN"]

solution(fees, records)