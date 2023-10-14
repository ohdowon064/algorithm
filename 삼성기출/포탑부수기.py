from collections import deque
from pprint import pprint

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 우하좌상
direction_for_lazer = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_for_bomb = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]
attack_order = []

def attacker_and_defender():
    max_value = float('-inf')
    min_value = float('inf')
    attack_candidates = []
    defend_candidates = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue

            if board[i][j] > max_value:
                max_value = board[i][j]
                defend_candidates = [(i, j)]
            elif board[i][j] == max_value:
                defend_candidates.append((i, j))

            if board[i][j] < min_value:
                min_value = board[i][j]
                attack_candidates = [(i, j)]
            elif board[i][j] == min_value:
                attack_candidates.append((i, j))

    for attacker in attack_order[::-1]:
        if attacker in attack_candidates:
            min_r, min_c = attacker
            break
    else:
        attack_candidates.sort(key=lambda x: (-(x[0] + x[1]), -x[1]))
        min_r, min_c = attack_candidates[0]

    not_attacker_candidates = list(filter(lambda x: x not in attack_order, defend_candidates))
    if not_attacker_candidates:
        not_attacker_candidates.sort(key=lambda x: (x[0] + x[1], x[1]))
        max_r, max_c = not_attacker_candidates[0]
    else:
        for attacker in attack_order:
            if attacker in defend_candidates:
                max_r, max_c = attacker
                break

    board[min_r][min_c] += n + m
    return min_r, min_c, max_r, max_c


def get_adjacent_for_lazer(node):
    adjacent_nodes = []
    for dx, dy in direction_for_lazer:
        nx, ny = (node[0] + dx) % n, (node[1] + dy) % m
        adjacent_nodes.append((nx, ny))

    return adjacent_nodes

def _lazer(start, end):
    visited = {start}
    q = deque()
    q.append((start, []))

    while q:
        pos, path = q.popleft()
        if pos == end:
            return path

        for adj in get_adjacent_for_lazer(pos):
            if board[adj[0]][adj[1]] == 0 or adj in visited:
                continue
            q.append((adj, path + [adj]))
            visited.add(adj)

    return None


def lazer(attack_r, attack_c, defend_r, defend_c):
    path = _lazer((attack_r, attack_c), (defend_r, defend_c))
    if path is None:
        return None
    power = board[attack_r][attack_c]
    for x, y in path[:-1]:
        board[x][y] = max(0, board[x][y] - power // 2)
    board[defend_r][defend_c] = max(0, board[defend_r][defend_c] - power)
    return path[:-1]

def get_adjacent_for_bomb(node):
    adjacent_nodes = []
    for dx, dy in direction_for_bomb:
        nx, ny = (node[0] + dx) % n, (node[0] + dy) % m
        adjacent_nodes.append((nx, ny))

    return adjacent_nodes


def bomb(attack_r, attack_c, defend_r, defend_c):
    power = board[attack_r][attack_c]
    participants = []
    for adj in get_adjacent_for_bomb((defend_r, defend_c)):
        if board[adj[0]][adj[1]] == 0 or adj == (attack_r, attack_c):
            continue
        elif adj == (defend_r, defend_c):
            board[adj[0]][adj[1]] = max(0, board[adj[0]][adj[1]] - power)
        else:
            participants.append(adj)
            board[adj[0]][adj[1]] = max(0, board[adj[0]][adj[1]] - power // 2)

    return participants

def repair(participants):
    participants = set(participants)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 or (i, j) in participants:
                continue
            board[i][j] += 1

def step():
    attack_r, attack_c, defend_r, defend_c = attacker_and_defender()
    if (attack_r, attack_c) == (defend_r, defend_c):
        return True
    attack_order.append((attack_r, attack_c))
    participants = lazer(attack_r, attack_c, defend_r, defend_c)
    if participants is None:
        participants = bomb(attack_r, attack_c, defend_r, defend_c)
    participants += [(attack_r, attack_c), (defend_r, defend_c)]
    repair(participants)
    return False

for _ in range(k):
    end = step()
    if end:
        break

print(max([max(row) for row in board]))