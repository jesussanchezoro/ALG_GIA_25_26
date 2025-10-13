

import random

n = 10
m1 = [[random.randint(0, 1000) for _ in range(n)] for _ in range(n)]
m2 = [[random.randint(0, 1000) for _ in range(n)] for _ in range(n)]

res = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            res[i][j] = res[i][j] + m1[i][k] * m2[k][j]