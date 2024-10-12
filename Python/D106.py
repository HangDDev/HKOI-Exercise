# https://judge.hkoi.org/task/D106

N = int(input())

if 11 <= N % 100 <= 13:
    suffix = 'th'
else:
    suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(N % 10, 'th')  
print(f"{N}{suffix}")
