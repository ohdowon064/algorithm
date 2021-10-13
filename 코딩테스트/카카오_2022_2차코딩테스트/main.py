"""
595턴 동안 game_result_api를 통해 게임 결과 확인
595턴 동안 match_api 사용

1. waiting_line_api로 현재 대기열에 매칭 대기 중인 유저 정보 조회
2. user_info_api로 대기 중인 유저들의 등급확인
3. 등급에 따라서 비슷한 유저들끼리 모아서 pairs 생성
    -> 비슷하다? 기준값을 임의로 설정해본다.
    -> 유저 차이가 기준값 이하이면 pair로 생성
4. match_api로 pairs를 넘겨 호출
"""
from kakao import KakaoAPI
from utils import Game, User


def solution(kakao_api: KakaoAPI):
    users = [User() for _ in range(kakao_api.user_count + 1)]

    for turn in range(596):
        # 모든 유저 정보 조회
        users = Game.get_users(kakao_api, users)

        # 대기열에 대기 중인 유저 조회
        waiting_users = Game.get_waiting_users(kakao_api, users)

        # 대기 유저들로 매칭 쌍 생성
        pairs = Game.get_pairs_from_waiting_users(kakao_api, waiting_users)

        # 매칭 쌍으로 게임 매칭
        kakao_api.match_api(pairs)

        # 게임 결과 조회 후 등급 수정
        Game.set_grade_by_game_result(kakao_api, users)

        if turn % 50 == 0:
            # print(users)
            print(f"{turn} 번째 턴입니다.")

        if turn == 595:
            print("마지막 유저들의 등급")
            print(users)


def print_score(score):
    print(f"{'=' * 10}첫번째 점수{'=' * 10}")
    print(score)
    print(f"{'=' * 10}========={'=' * 10}")

def scenario(kakao_api: KakaoAPI):
    print(f"{kakao_api.problem} 번째 시나리오 시작")
    solution(kakao_api)
    print(f"{kakao_api.problem} 번째 시나리오 종료")

    score = kakao_api.score_api()
    print("매칭 기준 등급차 :", kakao_api.ref_grade_diff)
    print("승리 가중치", kakao_api.win_weight)
    print("패배 가중치", kakao_api.lose_weight)
    print_score(score)

    return score

if __name__ == "__main__":
    # score1 = scenario(KakaoAPI(1))
    score2 = scenario(KakaoAPI(2))

    # print_score(score1)
    print_score(score2)




