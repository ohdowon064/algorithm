"""
문제
1. 일부 자릿수 영단어 -> 원래 숫자 찾기
"""

def solution(s):
    numbers = {
        "zero" : "0",
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : '4',
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }

    origin = ""
    word = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            origin += s[i]
        else:
            word += s[i]
            if word in numbers:
                origin += str(numbers[word])
                word = ""
        i += 1

    return origin

s = input()
print(solution(s))