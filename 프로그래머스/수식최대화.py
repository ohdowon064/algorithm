# https://programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
import re

def solution(expression):
    expressions = set(re.findall("\D", expression))
    prior = permutations(expressions)
    cand = []

    for op_cand in prior:
        temp = re.compile("(\D)").split('' + expression)
        for exp in op_cand:
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]
        cand.append(abs(int(temp[0])))

    return max(cand)

expression = '100-200*300-500+20'
print(solution(expression))