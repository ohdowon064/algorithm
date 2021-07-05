"""
    1. +, -, ()
    2. 괄호없는 식에서 괄호로 최소값 만들기

    알고리즘
    1. + 또는 - 만 있다. -> 순서 상관 없음
    2. 섞여있다. -> + 먼저하면 빼는 수가 커진다.

"""
string = input()
express = []

num = ""

for char in string:
    if char.isdecimal():
        num += char
    else:
        express.append(int(num))
        express.append(char)
        num = ""
express.append(int(num))

i = 0
while i != len(express):
    if express[i] == "+":
        express[i-1] = express[i-1] + express[i+1]
        del express[i]
        del express[i]
    else:
        i += 1

express = "".join(map(str, express))
print(eval(express))








