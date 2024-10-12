# https://judge.hkoi.org/task/D101

num = input()

if num.startswith("2") or num.startswith("3"):
  print("Fixed")
  
if num.startswith("5") or num.startswith("6") or num.startswith("9"):
  print("Mobile")
