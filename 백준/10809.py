# 단어 S, a~z 알파벳이 단어에 포함되어있으면 처음 위치, 없으면 -1
s = input()
alpha = [s.index(chr(c)) if chr(c) in s else -1 for c in range(ord('a'), ord('z')+1)]

# from string import ascii_lowercase as alc
# alpha = [s.index(c) if c in s else -1 for c in alc]

print(*alpha)