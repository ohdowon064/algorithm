import requests


class KakaoAPI:
    BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
    AUTH_TOKEN = "a2950aff9c8a9ead2fb5fb2689f6e31e"
    base_headers = {"Content-Type": "application/json"}

    start_url = BASE_URL + "/start"
    locations_url = BASE_URL + "/locations"
    trucks_url = BASE_URL + "/trucks"
    simulate_url = BASE_URL + "/simulate"
    score_url = BASE_URL + "/score"

    def __init__(self, problem: int):
        result = self.start_api(problem)
        self.auth_key = result["auth_key"]
        self.headers = {"Authorization": self.auth_key, **self.base_headers}
        self.server_status = None

    @classmethod
    def start_api(cls, problem: int):
        headers = {"X-Auth-Token": cls.AUTH_TOKEN, **cls.base_headers}
        payload = dict(problem=problem)

        res = requests.post(url=cls.start_url,
                            json=payload,
                            headers=headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "auth_key" in res_body.keys()

        print(res_body)
        return res_body

    def locations_api(self):
        res = requests.get(url=self.locations_url,
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "locations" in res_body.keys()

        print(res_body)
        return res_body

    def trucks_api(self):
        res = requests.get(url=self.trucks_url,
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "trucks" in res_body.keys()

        print(res_body)
        return res_body


    def simulate_api(self, commands: dict):
        res = requests.put(url=self.simulate_url,
                           json=commands,
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "status" in res_body.keys()

        # print(res_body)
        self.server_status = res_body["status"]
        return res_body


    def score_api(self):
        if self.server_status is None:
            raise Exception("현재 서버의 상태가 finished가 아닙니다.")

        res = requests.get(url=self.score_url,
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "score" in res_body.keys()

        print(res_body)
        return res_body