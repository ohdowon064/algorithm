cache = [0] * 100

def pibo_top_down(x):
    print(f'f({x})', end=' ')
    if x == 1 or x == 2:
        return 1
    if cache[x] != 0:
        return cache[x]
    cache[x] = pibo_top_down(x - 1) + pibo_top_down(x - 2)
    return cache[x]

pibo_top_down(6)

def pibo_bottom_up(x):
    cache[1], cache[2] = 1, 1
    for i in range(3, x + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[x]

print(pibo_bottom_up(6))