T = int(input())
for _ in range(T):
    n, s = input().split()
    print(''.join(map(lambda x : x*int(n), s)))