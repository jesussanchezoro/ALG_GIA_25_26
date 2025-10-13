import random

n = 100
v = random.sample(range(n*10), n)

for i in range(n-1):
    for j in range(n-i-1):
        if v[j] > v[j+1]:
            v[j], v[j+1] = v[j+1], v[j]