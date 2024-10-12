# https://judge.hkoi.org/task/D208

a = int(input())
max1 = -2147483648
max2 = -2147483648
x = list(map(int, input().split()))
for i in range(a):
  if x[i] > max1:
    temp = max1
    max1 = x[i]
    max2 = temp
  elif (x[i] < max1 and x[i] > max2) or x[i] == max1:
    max2 = x[i]

print(max1)
print(max2)
