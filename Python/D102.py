# https://judge.hkoi.org/task/D102

a = input()
b = float(a.replace("$", ""))
c = round(b * 10)

if c % 2 == 0:
    c_half = c // 2
else:
    c_half = c // 2 + 1

print(f"${c_half / 10.0}")
