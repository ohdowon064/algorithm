from collections import defaultdict


class Excel:
    def __init__(self):
        self.excel = [[""] * 50 for _ in range(50)]
        self.value_index = defaultdict(list)
        self.groups = {i: {i} for i in range(50 * 50)}

    def update(self, r, c, v):
        for cell in list(self.groups[r * 50 + c]):
            x, y = divmod(cell, 50)
            self.excel[x][y] = v
            self.value_index[v].append((x, y))

    def update_by_value(self, v1, v2):
        for r, c in self.value_index[v1]:
            self.update(r, c, v2)
        self.value_index.pop(v1)


    def merge(self, r1, c1, r2, c2):
        min_x, max_x = min(r1, r2), max(r1, r2)
        min_y, max_y = min(c1, c2), max(c1, c2)
        value = self.excel[r1][c1] if self.excel[r1][c1] else self.excel[r2][c2]
        _group = set()
        for r in range(min_x, max_x + 1):
            for c in range(min_y, max_y + 1):
                _group = _group.union(self.groups[r * 50 + c])

        for cell in list(_group):
            x, y = divmod(cell, 50)
            self.groups[x * 50 + y] = _group.copy()
            self.update(x, y, value)

    def unmerge(self, r, c):
        value = self.excel[r][c]
        for cell in list(self.groups[r * 50 + c]):
            self.groups[cell] = {cell}
            x, y = divmod(cell, 50)
            self.update(x, y, "")

        self.update(r, c, value)

    def print_cell(self, r, c, console):
        console.append(self.excel[r][c] if self.excel[r][c] else "EMPTY")


def solution(commands):
    answer = []
    excel = Excel()
    for command in commands:
        _command, *parameters = command.split()
        if _command == "UPDATE":
            if len(parameters) == 3:
                r, c, value = int(parameters[0]), int(parameters[1]), parameters[2]
                excel.update(r-1, c-1, value)
            else:
                excel.update_by_value(*parameters)

        elif _command == "MERGE":
            r1, c1, r2, c2 = map(int, parameters)
            excel.merge(r1-1, c1-1, r2-1, c2-1)

        elif _command == "UNMERGE":
            r, c = map(int, parameters)
            excel.unmerge(r-1, c-1)

        elif _command == "PRINT":
            r, c = map(int, parameters)
            excel.print_cell(r-1, c-1, console=answer)

    return answer

print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))