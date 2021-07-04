endingTime = 30
jobs = [[1, 10, 20, 6], [2, 12, 20, 8], [3, 20, 30, 2], [4, 25, 40, 10]]
complete = []

sec = 0
for job in jobs:
    if job[2] >= sec:
        complete.append(job[0])

        if job[1] <= sec:
            sec = sec + job[3]
        else:
            sec = job[1] + job[3]

print(complete)