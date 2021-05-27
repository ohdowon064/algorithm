numbers = set()
self_numbers = set(range(1, 10001))

for n in range(1, 10001):
    n = n + sum(list(map(int, str(n))))
    if n <= 10000:
        numbers.add(n)

self_numbers = sorted(list(self_numbers - numbers))
for n in self_numbers:
    print(n)
