"""
input
5 3
1 3 2 3 2

input
8 5
1 5 4 3 2 4 5 2
"""
from itertools import combinations
n, m = map(int, input().split())
balls = list(map(int, input().split()))
indexes = [i for i in range(n)]

cases = list(filter(lambda x: balls[x[0]] != balls[x[1]], combinations(indexes, 2)))
print(len(cases))