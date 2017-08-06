import spacefill.curvetools as ct
import sys

curve_map = ct.generate_map(64, 48)
print('Byte Size: {}'.format(sys.getsizeof(curve_map)))
print('Amount of points: {}'.format(len(curve_map)))

point = ct.coord_to_position((25, 25), curve_map)
coord = ct.position_to_coord(point, curve_map)
print('Point: {}, Coord: {}'.format(point, coord))

import matplotlib.pyplot as plt
px, py = zip(*curve_map)
plt.plot(px, py)
plt.plot([coord[0]], [coord[1]], 'ro')
plt.show()
