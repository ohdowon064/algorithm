s = input()
dial = {
    'ABC' : 2,
    'DEF' : 3,
    'GHI' : 4,
    'JKL' : 5,
    'MNO' : 6,
    'PQRS' : 7,
    'TUV' : 8,
    'WXYZ' : 9
}
n = []
for char in s:
    for alphas in dial.keys():
        if char in alphas:
            n.append(dial[alphas])
            break

print(sum(n) + len(n))
