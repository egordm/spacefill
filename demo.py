from spacefill import generate_map, coord_to_position, position_to_coord
import sys

# curve_map = generate_map(64, 32)
curve_map = generate_map(512, 384)
print('Byte Size: {}'.format(sys.getsizeof(curve_map)))
print(len(curve_map))
# print(curve_map)
point = coord_to_position((25, 25), curve_map)
coord = position_to_coord(point, curve_map)
print('Point: {}, Coord: {}'.format(point, coord))

import matplotlib.pyplot as plt

px, py = zip(*curve_map)
plt.plot(px, py)
plt.plot([coord[0]], [coord[1]], 'ro')
plt.show()
