from math import sin

from z_graph import ZGraph

PI = 3.14159
RANGE = (0, PI/2)

def f(x, y):
    return 4 * sin(x) * sin(y) + 2 * sin(x) + 2 * sin(y)  

if __name__ == "__main__":
    z = ZGraph(RANGE, RANGE, f, 100)
    solid = z.solid_output()
    f_ = open("output.stl", "w")
    solid.write_ascii(f_)
