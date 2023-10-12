def solution(N):
    enable_print = N % 10
    while N > 0:
        if not enable_print and N % 10 != 0:
            enable_print = 1
        if enable_print:
            print(N % 10, end="")
        N = N // 10

solution(12345)
print()
solution(10000)
print()
solution(1)
print()
solution(1000000000)


def solution(N):
    enable_print = N % 10
    while N > 0:
        if not enable_print and N % 10 != 0:
            enable_print = 1
        if enable_print:
            print(N % 10, end="")
        N = N // 10
