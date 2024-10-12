# https://judge.hkoi.org/task/D111

w, h = map(float, input().split())
bmi = w /h**2
print(f'{bmi:.3f}')
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 23.0:
    print("Normal")
elif 23.0 <= bmi < 25.0:
    print("Overweight")
else:
    print("Obese")
