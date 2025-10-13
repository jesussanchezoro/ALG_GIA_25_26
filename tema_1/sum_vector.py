import random

n = 10
v = random.sample(range(n*10), n)

s = 0
for num in v:
    s += num

print(s)
