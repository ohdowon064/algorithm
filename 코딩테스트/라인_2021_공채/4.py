"""
문제
1. len % p = 0이 되는 가장 작은 소수 p
    len == 1이면 생략
2. 길이가 len//p인 p개의 작은 배열을 만든다.
3. 각 배열에 원소를 순서대로 넣는다.
    arr[1]에 첫 번째 원소, arr[2]에 두 번째 원소, ...,
4. 다시 p개의 배열에 반복
"""
from copy import deepcopy
def solution(n):
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    arr = list(range(1, n + 1))

    def split(arr, p):
        result = []
        i, l = 0, len(arr)
        while i < len(arr):
            result.append(arr[i : i + l//p])
            i = i + l // p
        return result

    def shuffle(arr, arr_list, p):
        copy_list = deepcopy(arr_list)
        i = 0
        l = len(arr_list)
        c = 0
        f = 0
        while i < len(arr):
            if f == p:
                c += 1
                f = 0
            copy_list[(l + i) % p][c] = arr[i]
            i += 1
            f += 1

        return copy_list

    print(shuffle(arr, split(arr, 2), 2))



n = 12
solution(n)

