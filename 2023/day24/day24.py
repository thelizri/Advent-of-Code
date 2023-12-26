import numpy as np

# px py pz @ vx vy vz
example_input = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3""".splitlines()

input = open("day24.txt").read().splitlines()


class Hailstone:
    def __init__(self, x, y, z, vx, vy, vz, A, B, C):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.A = A
        self.B = B
        self.C = C

    def __repr__(self):
        return "Hailstone({}, {}, {})".format(self.x, self.y, self.z)


vectors = []
for row in input:
    row = row.replace(" @", ",")
    px, py, pz, vx, vy, vz = [int(x) for x in row.split(",")]
    A = vy
    B = -vx
    C = vy * px - vx * py
    vectors.append(Hailstone(px, py, pz, vx, vy, vz, A, B, C))

mini, maxi = 200000000000000, 400000000000000
count = 0
for i, stoneA in enumerate(vectors[:-1]):
    for j, stoneB in enumerate(vectors[i + 1 :], i + 1):
        first = np.array([[stoneA.A, stoneA.B], [stoneB.A, stoneB.B]])
        second = np.array([stoneA.C, stoneB.C])
        try:
            x, y = np.linalg.solve(first, second)
            if mini <= x <= maxi and mini <= y <= maxi:
                if (x - stoneA.x) / stoneA.vx >= 0 and (y - stoneA.y) / stoneA.vy >= 0:
                    if (x - stoneB.x) / stoneB.vx >= 0 and (
                        y - stoneB.y
                    ) / stoneB.vy >= 0:
                        count += 1
        except np.linalg.LinAlgError:
            pass

print("Part 1:", count)
