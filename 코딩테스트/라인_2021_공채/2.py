"""
문제
1. research : 전월 검색기록을 일 기준 분류
2. n일 동안 k번 이상 검색
3. n일 동안 총 2 * n * k번 이상 검색

알고리즘
1. Counter
"""
from collections import Counter, defaultdict


def solution(research, n, k):
    word_list = Counter(''.join(research)).keys()
    table = defaultdict(list)

    for r in research:
        search = Counter(r)

        for word in word_list:
            if word in search.keys():
                table[word].append(search[word])
            else:
                table[word].append(0)

    is_issue = defaultdict(int)
    for word, counts in table.items():
        for i in range(len(counts) - n + 1):
            if len(list(filter(lambda x: x >= k, counts[i: i + n]))) == n and sum(counts[i: i + n]) >= 2 * n * k:
                is_issue[word] += 1
    print(is_issue)
    if not is_issue:
        print(0)
        return "None"
    ans = max(is_issue, key=lambda x: (is_issue[x], -ord(x)))

    return ans



# research = ["abaaaa","aaa","abaaaaaa","fzfffffffa"]
# research = ["yxxy","xxyyy"]
research = ["xy","xy"]
n = 1
k = 1
solution(research, n, k)