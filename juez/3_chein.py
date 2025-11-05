
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def naive_closest_points(P):
    n = len(P)
    min_dist = 0x3f3f3f3f
    for i in range(n):
        for j in range(i+1, n):
            d = euclidean_distance(P[i], P[j])
            min_dist = min(d, min_dist)
    return min_dist


def combine(strip, d):
    min_dist = d
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            d_i = euclidean_distance(strip[i], strip[j])
            min_dist = min(d_i, min_dist)
    return min_dist


def dyv_closest_points(points_x, points_y):
    n = len(points_x)

    if n <= 3:
        return naive_closest_points(points_x)
    else:
        mid = n // 2
        points_x_l = points_x[:mid]
        points_x_r = points_x[mid:]

        mid_x = points_x_l[mid-1][0]

        points_y_l = []
        points_y_r = []
        for p in points_y:
            if p[0] <= mid_x:
                points_y_l.append(p)
            else:
                points_y_r.append(p)

        distance_l = dyv_closest_points(points_x_l, points_y_l)
        distance_r = dyv_closest_points(points_x_r, points_y_r)

        d = min(distance_l, distance_r)

        strip = []
        for p in points_y:
            if abs(p[0]-mid_x) < d:
                strip.append(p)

        d_strip = combine(strip, d)
        return d_strip


n, min_cost = map(int, input().strip().split())
points = []
for id in range(n):
    x, y = map(int, input().strip().split())
    points.append((x, y, id))

points_x = sorted(points, key = lambda p: p[0])
points_y = sorted(points, key = lambda p: p[1])
min_dist = dyv_closest_points(points_x, points_y)
print(f"MINIMO: {round(min_dist,2):.2f}")

m = int(input().strip())
for _ in range(m):
    p1, p2 = map(int, input().strip().split())
    d = euclidean_distance(p1, p2)
    cost = round(min_cost * d / min_dist, 2)
    print(f"{p1} -> {p2}: {cost:.2f}")
