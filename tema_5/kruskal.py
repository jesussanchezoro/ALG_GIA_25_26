
def update_components(components, new_id, old_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal(candidates, n):
    candidates.sort(key = lambda x:x[2])
    components = list(range(n+1))
    sol = 0
    i = 0
    number_components = n
    while i < len(candidates) and number_components > 1:
        src, dst, w = candidates[i]
        if components[src] != components[dst]:
            sol += w
            number_components -= 1
            update_components(components, components[src], components[dst])
        i += 1
    return sol


g = [
    (1,3,1), (1,4,2), (1,7,6),
    (2,5,2), (2,6,4), (2,7,7),
    (3,1,1), (3,4,3), (3,7,5),
    (4,1,2), (4,3,3), (4,5,1), (4,6,9),
    (5,2,2), (5,4,1), (5,7,8),
    (6,2,4), (6,4,9),
    (7,1,6), (7,2,7), (7,3,5), (7,5,8)
]
n = 7

sol = kruskal(g, n)
print(sol)