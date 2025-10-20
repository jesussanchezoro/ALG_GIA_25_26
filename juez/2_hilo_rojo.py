
def bin_search(data, start, end, search):
    if start > end:
        return -1
    else:
        mid = (start + end) // 2
        if data[mid] == search:
            return mid
        else:
            if data[mid] > search:
                return bin_search(data, start, mid-1, search)
            else:
                return bin_search(data, mid+1, end, search)


n = int(input().strip())
data1 = list(map(int, input().strip().split()))
m = int(input().strip())
data2 = list(map(int, input().strip().split()))

k = int(input().strip())
for _ in range(k):
    q1, q2 = map(int, input().strip().split())
    p1 = bin_search(data1, 0, n-1, q1)
    p2 = bin_search(data2, 0, m-1, q2)
    if p1 >= 0 and p2 >= 0:
        print(f"{q1} {q2}")
    else:
        print("SIN DESTINO")