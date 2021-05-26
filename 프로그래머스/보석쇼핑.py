def solution(gems):
    n = len(set(gems))
    answer = [0, len(gems) - 1]
    start, end = 0, 0
    
    while start < len(gems) and end < len(gems):
        chk = len(set(gems[start:end + 1]))
        
        if chk == n:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            
    return answer[0] + 1, answer[1] + 1

gems = 	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))