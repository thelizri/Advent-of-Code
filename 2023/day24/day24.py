import numpy as np

# px py pz @ vx vy vz
example_input = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3""".splitlines()

vectors = []
for row in example_input:
    row = row.replace(" @", ",")
    px, py, pz, vx, vy, vz = [int(x) for x in row.split(",")]
    A = py
    B = -px
    C = py * vx - px * vy
    vectors.append((A, B, C))

print(vectors)

for i, a in enumerate(vectors):
    for j, b in enumerate(vectors[i + 1 :], i + 1):
        first = np.array([[a[0], a[1]], [b[0], b[1]]])
        second = np.array([a[2], b[2]])
        x, y = np.linalg.solve(first, second)
        print("x: {:.1f}, y: {:.1f}".format(x, y))
