"""
문제
1. 닉네임, 이메일 모두 유사 -> 동일유저
2. a == b, b == c -> a == c
3. 닉네임 유사
    1) 2개 이하 문제 삭제하여 동일
4. 이메일 유사 : 계정이름@서버이름
    1) 계정이름에서 1개 문자 삭제하여 전체 이메일 주소 동일
    2) 계정이름 동일
5. nicks : 닉네임 배열
6. emails : 이메일 배열

알고리즘
1. 동일여부 판단
2. 닉네임 : 투 포인터로 다른 개수 체크
3. 이메일
    1) 투 포인터로 둘 중 하나 삭제해서 같은지
    2) 계정이름 같은지
"""
from collections import defaultdict


def solution(nicks, emails):
    def is_same(a, b, flag='nick'):
        i = j = 0
        cnt = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
            elif i < len(a) - 1 and j < len(b) - 1:
                if flag == 'nick':
                    if a[:i] + a[i+1:] == b[:j] + b[j+1:]:
                        return True
                    if a[:i] + a[i+1:] == b:
                        return True
                    if a == b[:j] + b[j+1:]:
                        return True
                    return False
                else:
                    if a[:i] + a[i+1:] == b:
                        return True
                    if a == b[:j] + b[j+1:]:
                        return True
                    return False
            return False

    def is_same_email(a, b):
        a_name, a_server = a.split('@')
        b_name, b_server = b.split('@')
        if a_name == b_name:
            return True
        if is_same(a_name, b_name, flag='email') and a_server == b_server:
            return True

        return False

    unique = defaultdict(set)
    user_list = list(zip(nicks, emails))
    for i in range(len(user_list)):
        for j in range(i + 1, len(user_list)):
            if is_same(user_list[i][0], user_list[j][0]) and is_same_email(user_list[i][1], user_list[j][1]):
                flag = False
                for k in unique.keys():
                    if j in unique[k]:
                        unique[k].add(j)
                        flag = True
                if not flag:
                    unique[i].add(j)

    return len(unique)


nicks = ["imhero111", "moneyman", "hero111", "imher1111", "hro111", "mmoneyman", "moneymannnn"]
emails = ["superman5@abcd.com", "batman432@korea.co.kr", "superman@abcd.com", "supertman5@abcd.com", "superman@erty.net", "batman42@korea.co.kr", "batman432@usa.com"]
solution(nicks, emails)