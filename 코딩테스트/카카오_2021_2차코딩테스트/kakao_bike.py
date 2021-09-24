import requests

def id_to_index(id: int, n: int):
    col, row = divmod(id, n)
    row = n - row - 1
    print(row, col)
    return row, col

def index_to_id(row, col, n):
    id = n - row - 1 + col * n
    return id

class KakaoAPI:
    base_url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
    base_headers = {"Content-Type": "application/json"}
    auth_token = "bd593a88021457860daad0e3110417ee"
    trucks_by_problem = {1: 5, 2: 10}
    bikes_by_problem = {1: 4, 2: 3}

    def __init__(self, problem: int):
        self.problem = problem
        self.auth_key = self.start_api(problem)
        self.headers = dict(Authorization=self.auth_key, **self.base_headers)
        self.truck_count = self.trucks_by_problem[problem]
        self.bike_count = self.bikes_by_problem[problem]

        if problem == 1:
            self.n = 5
            self.mean = 2
        elif problem == 2:
            self.n = 60
            self.mean = 3

        self.rentals = [
            [index_to_id(row, col, self.n) for col in range(self.n)]
            for row in range(self.n)
        ]
        self.pos = {
            self.rentals[i][j]: (i, j) for i in range(self.n)
            for j in range(self.n)
        }


    def start_api(self, problem: int):
        headers = {"X-Auth-Token": self.auth_token, **self.base_headers}
        data = dict(problem=problem)

        res = requests.post(self.base_url + "/start",
                            headers=headers,
                            json=data)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "auth_key" in res_body.keys()

        return res_body["auth_key"]

    def locations_api(self):
        res = requests.get(self.base_url + "/locations",
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "locations" in res_body.keys()

        return res_body["locations"]

    def trucks_api(self):
        res = requests.get(self.base_url + "/trucks",
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "trucks" in res_body.keys()

        return res_body["trucks"]

    def simulate_api(self, commands):
        data = dict(commands=commands)

        res = requests.put(self.base_url + "/simulate",
                           headers=self.headers,
                           json=data)
        res_body = res.json()

        assert res.status_code == 200, res_body

        return res_body

    def score_api(self):
        res = requests.get(self.base_url + "/score",
                           headers=self.headers)
        res_body = res.json()

        assert res.status_code == 200, res_body
        assert "score" in res_body.keys()

        return res_body["score"]