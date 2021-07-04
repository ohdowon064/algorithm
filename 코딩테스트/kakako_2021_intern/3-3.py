def solution(n, k, cmd):
    size = n
    discard = []
    data = list(range(n))
    for op in cmd:
        if op[0] == 'U':
            k -= int(op[-1])

        elif op[0] == 'D':
            k += int(op[-1])

        elif op[0] == 'C':
            discard.append(data.pop(k))
            if k + 1 == size:  
                k -= 1
            size -= 1
            
        else: # op[0] == 'Z'
            size += 1
            item = discard.pop()
            data.insert(item, item)
            if item <= k:
                k += 1
    
    print(data)
    print(discard)
    answer = ['O'] * n
    for i in discard:
        answer[i] = 'X'
        

    return ''.join(answer)

n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C", "Z"]

print(solution(n, k, cmd))