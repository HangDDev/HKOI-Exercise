# https://judge.hkoi.org/task/D302
space = 0
sentence = input()

for i in sentence:
  if i == " ":
    space += 1

print(len(sentence))
print(space+1)

# OR

space = 0
length = 0
sentence = input()

for i in sentence:
    if i == " ":
        space += 1
    length += 1

print(length)
print(space+1)
