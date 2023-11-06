# psum[i] = sum(arr[:i])
# psumMax = psum[:1] - psum[:2] + psum[:3] - psum[:4] + ... -/+ psum[:n]
# [1, 2, 4, 4] -> -3이 최대값
# [4, 1, 4, 2] -> psum [4, 5, 9, 11] -> 4 - 5 + 9 - 11 = -3
arr = [1, 2, 4, 4]

def getMaxOfBeuty(arr):
    ...