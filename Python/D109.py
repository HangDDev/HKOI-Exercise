# https://judge.hkoi.org/task/D109

num = int(input())

while num > 0:
    if num - 1000 >= 0:
        num -= 1000
        print(1000)
        continue
    if num - 500 >= 0:
        num -= 500
        print(500)
        continue
    if num - 100 >= 0:
        num -= 100
        print(100)
        continue
    if num - 50 >= 0:
        num -= 50
        print(50)
        continue
    if num - 20 >= 0:
        num -= 20
        print(20)
        continue
    if num - 10 >= 0:
        num -= 10
        print(10)
        continue
