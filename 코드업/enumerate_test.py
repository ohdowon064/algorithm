import time
import random
from string import ascii_lowercase as al
print(list(al))
a = [f'{random.choice(al)}{i}' for i in range(1, 100000)]

# 인덱스와 함께 출력
# 1
start = time.time()
for i in range(len(a)):
    print(i, a[i])
# print(f'time : {time.time() - start}')
end1 = time.time() - start

# 2
start = time.time()
for i, v in enumerate(a):
    print(i, v)
# print(f'time : {time.time() - start}')
end2 = time.time() - start

print(end1)
print(end2)

