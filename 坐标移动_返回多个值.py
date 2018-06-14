import cmath

def move(x, y, step, angle=0):
    nx = x + step * cmath.cos(angle)
    ny = y - step * cmath.sin(angle)
    return nx, ny
print(move(200, 200, 60, cmath.pi / 6))
print(cmath.pi/6)