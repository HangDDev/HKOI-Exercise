# https://judge.hkoi.org/task/D104

import math
a, b, c = map(int, input().split())
x = b ** 2 - 4 * a * c

if x < 0:
    print("None")
elif x == 0:
    print(f"{(-b + math.sqrt(x)) / (2 * a): .3f}")
else:
    root1 = (-b + math.sqrt(x)) / (2 * a)
    root2 = (-b - math.sqrt(x)) / (2 * a)
    print(f"{min(root1, root2):.3f} {max(root1, root2):.3f}")
