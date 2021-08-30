"""
문제
1. n * n 인형뽑기 격자, 크레인은 상단에 위치
2. j열 위치의 인형줄에서 가장 위에있는 것을 바구니로 이동
    -> 아무것도 없을 경우 무시
3. 바구니에 같은 인형일경우 터짐
    -> 같은 인형 == 같은 숫자
4. 터진 인형 개수
5. 0은 빈칸

알고리즘
1. moves의 있는 값들은 board에서 인형을 가져올 컬럼값이다.
2. 세로 인형들 파싱
3. 각 열의 인형들 개수 리스트
4. moves를 반복문으로 돌면서 값의 위치에 해당하는 인형 가져옴
    -> 가져온 후 해당 열의 인형 개수 -1
5. 바구니의 [-1]값과 같으면 count + 2

"""

def solution(board, moves):
    ans = 0
    bucket = []
    cols = list(zip(*board))

    # 각 세로열에 인형개수 저장
    numbers = [len(list(filter(lambda x: x != 0, col))) for col in cols]

    for move in moves:
        move -= 1
        if (top := numbers[move]) == 0:
            continue

        push = cols[move][-top]
        if len(bucket) > 0 and bucket[-1] == push:
            bucket.pop()
            ans += 2
        else:
            bucket.append(push)
        numbers[move] -= 1

    return ans

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)