def solution(gems):
    answer = []
    gem_kind = set(gems)
    cur_start, cur_end = 0, 1
    while cur_start < cur_end and cur_end < len(gems):
        chk = set(gems[cur_start:cur_end])
        if chk == gem_kind:
            if (answer == []) or ((answer[1] - answer[0]) > (cur_end - cur_start)):
                answer = [cur_start+1, cur_end]
            cur_start += 1
        else:
            cur_end += 1
    
    if cur_start == 0 and cur_end == len(gems):
        return 1, len(gems)
    
    return answer

gems = 	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))