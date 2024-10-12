# https://judge.hkoi.org/task/D108

a, b, c, d, e = input().split()
a = int(a)
c = int(c)
e = int(e)
ans = 0

if b == "+":
  if d == "-":
    ans = a + c - e
  elif d == "*":
    ans = a + c * e
  else:
    ans = a + c + e
elif b == "-":
  if d == "-":
    ans = a - c - e
  elif d == "*":
    ans = a - c * e
  else:
    ans = a - c + e
elif b == "*":
  if d == "-":
    ans = a * c - e
  elif d == "*":
    ans = a * c * e
  else:
    ans = a * c + e
    
print(ans)
