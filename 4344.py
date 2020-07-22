loop = int(input())

for i in range(loop):
    points = [int(j) for j in input().split()]
    avg = (sum(points) - points[0]) / points[0]
    over = 0
    for k in range(1, points[0]+1):
        if points[k] > avg:
            over += 1
    print("{:.3f}%".format(over/points[0]*100))
