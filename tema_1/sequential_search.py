import random

n = 10
v = random.sample(range(n*10), n)
search = v[random.randint(0, n-1)]

i = 0
while i < n and v[i] != search:
    i += 1