# https://judge.hkoi.org/task/D202

import math
n = int(input())
factors = []

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        factors.append(i)
        if i != n // i:
            factors.append(n // i)

factors.sort()
for i in factors:
    print(i)
