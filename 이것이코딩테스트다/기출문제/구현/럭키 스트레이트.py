score = list(map(int, input()))
mid = len(score) // 2
if sum(score[:mid]) == sum(score[mid:]):
    print("LUCKY")
else:
    print("READY")