import requests

def id_to_index(id: int, n: int):
    col, row = divmod(id, n)
    row = n - row - 1
    print(row, col)
    return row, col

def index_to_id(row, col, n):
    id = n - row - 1 + col * n
    return id


# kakao_api_1 = KakaoAPI(1)
# kakao_api_1.score_api()

res = requests.get("https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem1_day-1.json")
res_body = res.json()
max_key = max(res_body.keys(), key=lambda x: int(x))
print(max_key)
print(res_body[max_key])