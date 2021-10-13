"""
1. rows * columns 행렬 (1, 2, ... , rows * columns)
2. query(x1, y1, x2, y2)가 있을 때, 해당 직사각형을 시계방향으로 회전
3. 중앙은 회전하지 않는다.
4. 회전 시 이동하는 수 중 최솟값을 구한다.
5. 각 query의 이동최솟값을 배열에 담아 리턴

알고리즘
1. (x1, y1, x2, y2)에 해당하는 부분배열 조회
2. 어차피 해당하는 부분은 무조건 시계방향으로 이동
    -> 최솟값 배열에 저장
3. 시계방향 회전
    1) 좌측상단 ~ 우측상단이전: (i, j+1)
    2) 우측상단 ~ 우측하단이전: (i + 1, j)
    3) 우측하단 ~ 좌측하단이전: (i, j - 1)
    4) 좌측하단 ~ 좌측상단이전: (i + 1, j)
"""

def solution(rows, columns, queries):
    v = 0
    arr = [[v := v + 1 for j in range(columns)]
           for i in range(rows)]
    ans = []

    def move(arr, x1, y1, x2, y2):
        min_value = temp = arr[x1][y2]

        # 상단부분 회전
        # arr[x1][y1~y2이전]
        min_value = min(min_value, min(arr[x1][y1: y2]))
        arr[x1][y1 + 1: y2 + 1] = arr[x1][y1: y2]

        # 좌측부분 회전
        # arr[x1~x2이전][y1]
        for row in range(x1, x2):
            min_value = min(min_value, arr[row + 1][y1])
            arr[row][y1] = arr[row + 1][y1]

        # 하단후분 회전
        # arr[x2][y2~y1이전]
        min_value = min(min_value, min(arr[x2][y1 + 1: y2 + 1]))
        arr[x2][y1: y2] = arr[x2][y1 + 1: y2 + 1]

        # 우측부분 회전
        # arr[x1~x2이전][y2]
        for row in range(x2, x1 + 1, -1):
            min_value = min(min_value, arr[row - 1][y2])
            arr[row][y2] = arr[row - 1][y2]

        arr[x1 + 1][y2] = temp

        return min_value

    for query in queries:
        query = list(map(lambda x: x - 1, query))
        ans.append(move(arr, *query))

    print(ans)
    return ans




solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
solution(3,	3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
solution(100, 97, [[1,1,100,97]])