# hexlib.py
# Everything related to hexes

from collections import namedtuple
import math

Point = namedtuple("Point", ["x", "y"])

Hex = namedtuple("Hex", ["q", "r", "s"])

DoubledCoord = namedtuple("DoubledCoord", ["col", "row"])

Orientation = namedtuple(
    "Orientation", ["f0", "f1", "f2", "f3", "b0", "b1", "b2", "b3", "start_angle"])

Layout = namedtuple("Layout", ["orientation", "size", "origin"])


def qdoubled_from_cube(h):
    col = h.q
    row = 2 * h.r + h.q
    return DoubledCoord(col, row)


def qdoubled_to_cube(h):
    q = h.col
    r = (h.row - h.col) // 2
    s = -q - r
    return Hex(q, r, s)


def rdoubled_from_cube(h):
    col = 2 * h.q + h.r
    row = h.r
    return DoubledCoord(col, row)


def rdoubled_to_cube(h):
    q = (h.col - h.row) // 2
    r = h.row
    s = -q - r
    return Hex(q, r, s)


def hex_to_pixel(layout, hex):
    M = layout.orientation
    size = layout.size
    origin = layout.origin
    x = (M.f0 * hex.q + M.f1 * hex.r) * size.x
    y = (M.f2 * hex.q + M.f3 * hex.r) * size.y
    return Point(x + origin.x, y + origin.y)


def hex_corner_offset(layout, corner):
    M = layout.orientation
    size = layout.size
    angle = 2.0 * math.pi * (M.start_angle - corner) / 6.0
    return Point(size.x * math.cos(angle), size.y * math.sin(angle))


def polygon_corners(layout, hex):
    corners = []
    center = hex_to_pixel(layout, hex)
    for i in range(0, 6):
        offset = hex_corner_offset(layout, i)
        corners.append(Point(center.x + offset.x, center.y + offset.y))
    return corners


def pixel_to_hex(layout, point):
    M = layout.orientation
    size = layout.size
    origin = layout.origin
    pt = Point((point.x - origin.x) / size.x, (point.y - origin.y) / size.y)
    q = M.b0 * pt.x + M.b1 * pt.y
    r = M.b2 * pt.x + M.b3 * pt.y
    return Hex(q, r, -q - r)


def hex_round(hex):
    qi = int(round(hex.q))
    ri = int(round(hex.r))
    si = int(round(hex.s))
    q_diff = abs(qi - hex.q)
    r_diff = abs(ri - hex.r)
    s_diff = abs(si - hex.s)
    if q_diff > r_diff and q_diff > s_diff:
        qi = -ri - si
    else:
        if r_diff > s_diff:
            ri = -qi - si
        else:
            si = -qi - ri
    return Hex(qi, ri, si)


hex_directions = [Hex(1, 0, -1), Hex(1, -1, 0), Hex(0, -1, 1),
                  Hex(-1, 0, 1), Hex(-1, 1, 0), Hex(0, 1, -1)]

layout_pointy = Orientation(math.sqrt(3.0), math.sqrt(
    3.0) / 2.0, 0.0, 3.0 / 2.0, math.sqrt(3.0) / 3.0, -1.0 / 3.0, 0.0, 2.0 / 3.0, 0.5)

layout_flat = Orientation(3.0 / 2.0, 0.0, math.sqrt(3.0) / 2.0,
                          math.sqrt(3.0), 2.0 / 3.0, 0.0, -1.0 / 3.0, math.sqrt(3.0) / 3.0, 0.0)
