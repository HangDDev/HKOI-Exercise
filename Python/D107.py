# https://judge.hkoi.org/task/D107

import math

def isSquare(n):
    if n < 0:
        return False
    x = int(math.sqrt(n))
    return x * x == n

def isTriangular(n):
    if n < 0:
        return False
    k = (-1 + math.sqrt(1 + 8 * n)) / 2
    return k.is_integer()

num = int(input())
sqNum = isSquare(num)
trNum = isTriangular(num)

if sqNum:
    if trNum:
        print("Both")
    else:
        print("Square")
elif trNum:
    if sqNum:
        print("Both")
    else:
        print("Triangular")
else:
    print("Neither")
