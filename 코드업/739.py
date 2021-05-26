def dailyTemperatures(T):
    answer = [0] * len(T)
    stack = []

    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            top = stack.pop()
            answer[top] = i - top

        stack.append(i)
    return answer


temps = list(map(int, input().split()))
print(dailyTemperatures(temps))

