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
from typing import List, Tuple

from kakao import KakaoAPI


class User:
    def __init__(self, id: int = 0, grade: int = 0):
        self.id = id
        self.grade = grade
        self.win_count = 0
        self.lose_count = 0
        self.wait_from = None

    def __str__(self):
        return f"{self.id}: {self.grade}"

    def __repr__(self):
        return f"{self.id}: {self.grade}"


class Game:

    @classmethod
    def get_users(cls, kakao_api: KakaoAPI, users: List[User]) -> List[User]:
        """
        users 리스트에 id와 grade를 설정하는 함수

        :param kakao_api: 카카오 API 클래스
        :param users: User 객체 리스트
        :return:
        """
        user_infos = kakao_api.user_info_api()

        for user_info in user_infos:
            id, grade = user_info["id"], user_info["grade"]
            users[id] = User(id, grade)

        return users

    @classmethod
    def get_waiting_users(cls, kakao_api: KakaoAPI, users: List[User]) -> List[User]:
        """
        매칭 대기열에서 대기중인 유저들을 조회하는 함수

        :param kakao_api: 카카오 API 클래스 객체
        :param users: User 객체 리스트
        :return: 대기중인 User 리스트를 반환한다.
        """
        waiting_line = kakao_api.waiting_line_api()
        waiting_users = []

        for wait_user in waiting_line:
            id, wait_from = wait_user["id"], wait_user["from"]
            users[id].wait_from = wait_from

            waiting_users.append(users[id])

        waiting_users.sort(key=lambda x: x.wait_from)

        return waiting_users

    @classmethod
    def get_pairs_from_waiting_users(cls, kakao_api: KakaoAPI, waiting_users: List[User]) -> List[Tuple[int]]:
        """
        대기중인 유저 정보를 받아 매칭 쌍 (pairs)를 생성하는 함수

        :param kakao_api: 카카오 API 클래스 객체
        :param waiting_users: 대기 중인 유저 리스트
        :return: 매칭 쌍 pairs를 반환한다.
        """
        pairs = []

        for i in range(len(waiting_users) - 1):
            for j in range(i + 1, len(waiting_users)):
                if abs(waiting_users[i].grade - waiting_users[j].grade) <= kakao_api.ref_grade_diff:
                    pairs.append((waiting_users[i].id, waiting_users[j].id))

        return pairs

    @classmethod
    def set_grade_by_game_result(cls, kakao_api: KakaoAPI, users: List[User]) -> None:
        """
        게임 결과를 조회한 후 해당 결과를 통해 유저들의 등급 grade를 조정하는 함수

        :param kakao_api: 카카오 API 클래스 객체
        :param users: User 객체 리스트
        :return:
        """
        game_results = kakao_api.game_result_api()
        for game_result in game_results:
            win, lose, taken = game_result["win"], game_result["lose"], game_result["taken"]

            users[win].win_count += 1
            if users[win].lose_count > 1:
                users[win].lose_count -= 1

            users[lose].lose_count += 1
            if users[lose].win_count > 1:
                users[lose].win_count -= 1


            win_score = users[win].win_count * kakao_api.win_weight
            users[win].grade += win_score

            lose_score = users[lose].lose_count * kakao_api.lose_weight
            users[lose].grade = max(users[lose].grade - lose_score, 0)

        commands = [dict(id=user.id, grade=user.grade) for user in users[1:]]

        kakao_api.change_grade_api(commands)



