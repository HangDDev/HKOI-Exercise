# https://judge.hkoi.org/task/D105

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

if y1 > y2:
    print("After")
elif y1 < y2:
    print("Before")
elif y1 == y2:
    if m1 > m2:
        print("After")
    elif m1 < m2:
        print("Before")
    elif m1 == m2:
        if d1 > d2:
            print("After")
        elif d1 < d2:
            print("Before")
        elif d1 == d2:
            print("Same")
