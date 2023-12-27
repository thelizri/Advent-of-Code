import numpy as np
import sympy as sp

# px py pz @ vx vy vz
example_input = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3""".splitlines()

input = open("day24.txt").read().splitlines()


class Hailstone:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def getValues(self):
        return self.x, self.y, self.z, self.vx, self.vy, self.vz

    def getStandardFormLine(self):
        return self.vy, -self.vx, self.vy * self.x - self.vx * self.y

    def __repr__(self):
        return "Hailstone({}, {}, {})".format(self.x, self.y, self.z)


vectors = []
for row in input:
    row = row.replace(" @", ",")
    px, py, pz, vx, vy, vz = [int(x) for x in row.split(",")]
    vectors.append(Hailstone(px, py, pz, vx, vy, vz))

mini, maxi = 200000000000000, 400000000000000
count = 0
for i, stoneA in enumerate(vectors[:-1]):
    for j, stoneB in enumerate(vectors[i + 1 :], i + 1):
        firstA, firstB, firstC = stoneA.getStandardFormLine()
        secondA, secondB, secondC = stoneB.getStandardFormLine()
        first = np.array([[firstA, firstB], [secondA, secondB]])
        second = np.array([firstC, secondC])
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

# Part 2
# This is a cheat solution, that I saw on the internet
# Sympy does everything for us we just feed it the equations
xr, yr, zr, vxr, vyr, vzr = sp.symbols("xr yr zr vxr vyr vzr")

equations = []
for stone in vectors:
    x, y, z, vx, vy, vz = stone.getValues()
    equations.append((xr - x) * (vy - vyr) - (yr - y) * (vx - vxr))
    equations.append((yr - y) * (vz - vzr) - (zr - z) * (vy - vyr))

solution = sp.solve(equations, [xr, yr, zr, vxr, vyr, vzr])
x, y, z, vx, vy, vz = solution[0]
print("Part 2:", x + y + z)
