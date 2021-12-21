from hexlib import *

_grid = [
    DoubledCoord(1, 4),
    DoubledCoord(2, 4),
    DoubledCoord(3, 4),
    DoubledCoord(4, 4),
    DoubledCoord(5, 4),
    DoubledCoord(6, 4),
]

# grid now in cube coordinates
grid = [qdoubled_to_cube(hex) for hex in _grid]

# testing
# for hex in grid:
#     print(hex, rdoubled_from_cube(hex), qdoubled_from_cube(hex))

