from math import pi as pi
from math import sin as sin
from math import cos as cos

def nearest_sine_extremumes(x):
    whole_minimum = int(x / (pi/2))
    if not whole_minimum % 2:
        whole_minimum -= 1
    minimum = whole_minimum * (pi/2)
    maximum = minimum + pi
    return (minimum, maximum)


def convert_to_basis(x):
    return x - nearest_sine_extremumes(x)[0] - pi/2


def derivative(x, starting_coords):
    return 0.5 * sin(2 * x) - starting_coords[1] * cos(x) + x - starting_coords[0]


def search_root(possible_segment, starting_coords):
    x1 = possible_segment[0]
    x2 = possible_segment[1]
    if x1 - x2 < 0E-10:
        return (x1 + x2) / 2
    else:
        current = (x1 + x2) / 2
        if derivative(x1, starting_coords) * derivative(current, starting_coords) <= 0:
            return search_root((x1, current), starting_coords)
        else:
            return search_root((current, x2), starting_coords)


def find_distance(x, starting_coords):
    return ((x - starting_coords[0])**2 + (sin(x) - starting_coords[1])**2)**0.5


x, y = map(float, input("Input point coordinates: ").split())
if(x < 0):
    x *= -1
    y *= 1
coords = (x, y)

starting_interval = (nearest_sine_extremumes(coords[0])[0], coords[0] + 1 + abs(coords[1]))
nearest_point = search_root(starting_interval, coords)
rez = find_distance(nearest_point, coords)

print(rez)