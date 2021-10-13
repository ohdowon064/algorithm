import requests


class KakaoAPI:
    BASE_URL = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"
    BASE_HEADERS = {"Content-Type": "application/json"}
    AUTH_TOKEN = "69f6c255863a1f789dfdae1c3fd77316"


    def __init__(self, problem):
        self.problem = problem
        self.auth_key = self.start_api(problem)
        self.headers = dict(Authorization=self.auth_key, **self.BASE_HEADERS)

        if problem == 1:
            self.user_count = 30 # 참여 유저 수
            self.match_rate = 1 # 매칭률
            self.ref_grade_diff = 160 # 매칭 기준 등급차
            self.win_weight = 25 # 승리 가중치
            self.lose_weight = 9 # 패배 가중치
        elif problem == 2:
            self.user_count = 900
            self.match_rate = 45
            self.ref_grade_diff = 140
            self.win_weight = 29
            self.lose_weight = 11
        else:
            raise Exception("문제 번호는 1 또는 2만 가능합니다.")



    def start_api(self, problem: int):
        """
        문제를 풀기 위한 key를 발급한다. 문제 번호에 맞게 모든 유저에 대한 정보를 초기화한다.

        :param problem: 문제 번호
        :return: 문제를 풀기 위한 key를 반환
        """
        start_headers = {"X-Auth-Token": self.AUTH_TOKEN, **self.BASE_HEADERS}
        req_body = dict(problem=problem)

        res = requests.post(self.BASE_URL + "/start",
                            headers=start_headers,
                            json=req_body)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "auth_key" in res_body.keys(), res_body

        return res_body["auth_key"]

    def waiting_line_api(self):
        """
        :return: 현재 대기열에서 매칭을 대기 중인 유저들의 정보를 반환한다.
        id: 매칭을 기다리고 있는 유저 ID
        from: 매칭 대기를 시작한 시각(턴)
        """
        res = requests.get(self.BASE_URL + "/waiting_line",
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "waiting_line" in res_body.keys(), res_body

        return res_body["waiting_line"]


    def game_result_api(self):
        """
        595턴까지 GameResult API를 이용해 게임 결과를 확인해야 한다.

        :return: 이번 턴에 게임이 끝난 유저들의 게임 결과를 반환한다.
        win: 게임에서 이긴 유저 아이디
        lose: 게임에서 진 유저 아이디
        taken: 게임하는데 걸린 시간
        """
        res = requests.get(self.BASE_URL + "/game_result",
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "game_result" in res_body.keys(), res_body

        return res_body["game_result"]


    def user_info_api(self):
        """
        :return: 모든 유저들의 현재 등급을 반환한다.
        id: 유저 아이디
        grade: 현재 유저 등급
        """
        res = requests.get(self.BASE_URL + "/user_info",
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "user_info" in res_body.keys(), res_body

        return res_body["user_info"]

    def match_api(self, pairs):
        """
        대기열에서 매칭 대기 중인 두 유저를 매칭시켜 게임을 시작하도록 한다.
        Match API를 이용해 매치시킬 유저가 없더라도 595턴까지 진행해야 한다.

        :param pairs: 대기 중인 유저 쌍 리스트
        :return: 서버 상태와 현재 시각 반환
        """
        req_body = dict(pairs=pairs)

        res = requests.put(self.BASE_URL + "/match",
                           headers=self.headers,
                           json=req_body)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "status" in res_body.keys(), res_body

        return res_body

    def change_grade_api(self, commands):
        """
        여러 유저의 등급을 수정할 수 있다. 등급 범위는 0 ~ 9,999

        :param commands: id에 해당하는 유저의 점수(grade)를 수정한다.
        :return: 현재 카카오 게임 서버 상태 반환
        """
        req_body = dict(commands=commands)

        res = requests.put(self.BASE_URL + "/change_grade",
                           headers=self.headers,
                           json=req_body)
        res_body = res.json()

        assert res.status_code == 200, print(req_body, res_body)
        assert "status" in res_body.keys(), res_body

        return res_body

    def score_api(self):
        """
        :return: 정확성, 효율성, 총점을 반환
        """
        res = requests.get(self.BASE_URL + "/score",
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "score" in res_body.keys(), res_body

        return res_body





















