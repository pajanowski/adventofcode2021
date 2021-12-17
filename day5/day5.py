import numpy as np

readlines = open("input.txt", "r").readlines()
data = readlines
data1 = readlines

# get(x1, y1, x2, y2)
coordinates = []
for d in data:
    x1, y1, x2, y2 = list(map(int, d.replace(" -> ", ",").split(",")))
    coordinates.append((x1, y1, x2, y2))

coordinates = np.array(coordinates)
mxx,mxy = coordinates[[0, 2]].max(), coordinates[[1, 3]].max()

board = np.zeros((mxx*2, mxy*2))

# check only horizontal or vertical line
m1 = coordinates[:, 0]==coordinates[:, 2]
m2 = coordinates[:, 1]==coordinates[:, 3]
m = m1 | m2

masked = coordinates[m]
for co in masked:
    for x in range(min(co[0], co[2]), max(co[0], co[2])+1):
        for y in range(min(co[1], co[3]), max(co[1], co[3])+1):
            board[x, y] += 1
print((board.flatten()>1).sum())

# diagonal line
m1 = coordinates[:, 0]!=coordinates[:, 2]
m2 = coordinates[:, 1]!=coordinates[:, 3]
m=m1*m2
masked = coordinates[m]

for co in masked:
    # add or sub to x1?
    dx = int(co[2]>co[0]) or -1
    dy = int(co[3]>co[1]) or -1

    for dp in range(abs(co[2]-co[0])+1):
        x = co[0]+dx*dp
        y = co[1]+dy*dp
        board[x,y]+=1

print((board.flatten()>1).sum())
