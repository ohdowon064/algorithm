# n = int(input())

# time = {
#     'h' : 0,
#     'm' : 0,
#     's' : 0
# }
# cnt = 0
#
# while time['h'] != n or time['m'] != 59 or time['s'] != 59:
#     time['s'] += 1
#     if time['s'] == 60:
#         time['s'] = 0
#         time['m'] += 1
#     if time['m'] == 60:
#         time['m'] = 0
#         time['h'] += 1
#
#     for t in time:
#         if '3' in str(time[t]):
#             cnt += 1
#             break
#
# print(cnt)

n = int(input())
cnt = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt += 1
print(cnt)