p = input()
row = int(p[1])
col = int(ord(p[0])) - int(ord('a')) + 1

moves = [(-2, -1), (-1, -2), (2, -1), (-1, 2), (1, -2), (-2, 1), (1, 2), (2, 1)]

result = 0
for move in moves:
    next_row = row + move[0]
    next_col = col + move[1]

    if 1 <= next_row and next_row <= 8 and 1 <= next_col and next_col <= 8:
        result += 1

print(result)