def get_natural_number():
    n = 0
    while True:
        yield n
        n += 1


g = get_natural_number()
for _ in range(0, 100):
    print(next(g))