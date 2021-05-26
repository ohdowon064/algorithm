def solution(n, k, cmd):
    answer = ['O'] * n
    size = n
    discard = []
    for op in cmd:
        if op[0] == 'U':
            k -= int(op[-1])

        elif op[0] == 'D':
            k += int(op[-1])

        elif op[0] == 'C':
            discard.append(k)
            if k + 1 == size:  
                k -= 1
            size -= 1
            
        else: # op[0] == 'Z'
            size += 1
            if discard.pop() <= k:
                k += 1

    for num in discard:
        move = num + answer[:num].count('X')
        while answer[move] == 'X':
            move += 1
        answer[move] = 'X'

    return ''.join(answer)

n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]

print(solution(n, k, cmd))