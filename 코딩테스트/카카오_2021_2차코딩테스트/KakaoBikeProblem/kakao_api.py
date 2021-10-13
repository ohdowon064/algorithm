import requests

def index_to_id(row, col, size):
    id = size - row - 1 + size * col
    return id


# Kakao API들을 호출하는 클래스
class KakaoAPI:
    BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
    BASE_HEADERS = {"Content-Type": "application/json"}
    AUTH_TOKEN = "cb3c38b487ca9199e8fd39bc4d3ff6ec"

    trucks_by_problem = {1: 5, 2: 10} # 문제당 트럭 수
    bikes_by_problem = {1: 4, 2: 3} # 문제당 초기 id마다 자전거 수

    def __init__(self, problem: int): # 문제를 파라미터로 받아 객체생성
        self.problem = problem
        self.auth_key = self.start_api(problem)
        self.headers = dict(Authorization=self.auth_key, **self.BASE_HEADERS)
        self.truck_count = self.trucks_by_problem[problem]
        self.bike_count_init = self.bikes_by_problem[problem]

        if problem == 1:
            self.size = 5
            self.ref_value = 2
        elif problem == 2:
            self.size = 60
            self.ref_value = 3
        else:
            raise Exception("문제 번호는 1 또는 2만 가능합니다.")

        self.locations = [
            [index_to_id(row, col, self.size) for col in range(self.size)]
            for row in range(self.size)
        ]
        # dict에서 이중 for는 outer loop가 안쪽에 있다.
        self.id_to_index = {
            self.locations[i][j]: (i, j) for i in range(self.size)
            for j in range(self.size)
        }


    def start_api(self, problem: int):
        """
        문제를 풀기 위한 key를 발급한다. Start API를 실행하면 파라미터로 전달한 문제 번호에 맞게 각 자전거 대여소 및 트럭에 대한 정보를 초기화한다.

        :param problem: 문제번호
        :return: 문제를 위한 auth_key를 반환한다.
        """
        headers = {"X-Auth-Token": self.AUTH_TOKEN, **self.BASE_HEADERS}
        req_body = dict(problem=problem)

        res = requests.post(self.BASE_URL + "/start",
                            headers=headers,
                            json=req_body)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "auth_key" in res_body.keys(), res_body

        return res_body["auth_key"]


    def locations_api(self):
        """

        :return:
        현재 카카오 T 바이크 서비스 시각에 각 자전거 대여소가 보유한 자전거 수를 반환한다.
        """
        res = requests.get(self.BASE_URL + "/locations",
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "locations" in res_body.keys(), res_body

        return res_body["locations"]


    def trucks_api(self):
        """

        :return:
        현재 카카오 T 바이크 서비스 시각에 각 트럭의 위치와 싣고 있는 자전거 수를 반환한다.
        """
        res = requests.get(self.BASE_URL + "/trucks",
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body

        return res_body["trucks"]

    def simulate_api(self, commands):
        """
        현재 시각 ~ 현재 시각 + 1분 까지 각 트럭이 행할 명령을 담아 서버에 전달한다.

        :param commands: 각 트럭이 현재 시각 ~ 현재 시각 + 1분 까지 수행할 명령
        :return:
        status: 현재 카카오 T 서버의 상태/
        time: 현재 시각 (요청 시각에서 1분 경과)/
        failed_requests_count: 실패한 요청 수/
        distance: 모든 트럭이 현재까지 이동한 거리의 총합(km 단위)
        """
        req_body = dict(commands=commands)

        res = requests.put(self.BASE_URL + "/simulate",
                           headers=self.headers,
                           json=req_body)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "status" in res_body.keys(), res_body

        return res_body

    def score_api(self):
        """
        점수는 높을수록 좋다. 카카오 T 바이크 서버의 상태가 finished가 아닐 때 본 API를 호출하면 response의 score는 무조건 0.0이다.

        :return: 해당 Auth key로 획득한 점수를 반환한다.
        """
        res = requests.get(self.BASE_URL + "/score",
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "score" in res_body.keys(), res_body

        return res_body["score"]












