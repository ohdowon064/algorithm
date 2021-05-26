def solution(n, k, cmd):
    answer = ['O'] * n
    discard = []

    for op in cmd:
        if op[0] == 'U':
            x = int(op[-1])

            i = 0
            while i < x:
                if answer[k] == 'O':
                    i += 1
                k -= 1

        elif op[0] == 'D':
            x = int(op[-1])

            i = 0
            while i < x:
                if answer[k] == 'O':
                    i += 1
                k += 1
                

        elif op[0] == 'C':
            answer[k] = 'X'
            discard.append(k)

            if 'O' not in answer[k:]:
                while answer[k] == 'X':
                    k -= 1
            else:
                while answer[k] == 'X':
                    k += 1

        else: # op[0] == 'Z'
            answer[discard.pop()] = 'O'

    return ''.join(answer)

n = 8
k = 2
cmd = ["D 3","C","U 3","C","D 4","C","U 2"]

print(solution(n, k, cmd))