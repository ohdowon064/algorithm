def solution(s):
    numlist = {"zero" : 0, 
                "one" : 1,
                "two" : 2,
                "three" : 3,
                "four" : 4,
                "five" : 5,
                "six" : 6,
                "seven":7,
                "eight": 8,
                "nine": 9
    }
    num = ''
    answer = ''
    for char in s:
        if char.isdigit():
            answer += char
        else:
            num += char
            if num in numlist:
                answer += str(numlist[num])
                num = ''
    
    return int(answer)

s = "one4seveneight"
print(solution(s))