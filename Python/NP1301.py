# https://judge.hkoi.org/task/NP1301

with open("count.in", "r") as f:
    content = f.read()
    n, x = content.split()
    
num = 0

for i in range(1, int(n) + 1):
    num += str(i).count(x)

with open("count.out", "w") as f:
    f.write(str(num) + '\n')
