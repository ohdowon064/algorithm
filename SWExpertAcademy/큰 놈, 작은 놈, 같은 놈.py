t = int(input())
for i in range(1, t + 1):
    a, b = map(int, input().split())
    if a > b:
        result = ">"
    elif a < b:
        result = "<"
    else:
        result = "="
    print(f"#{i} {result}")