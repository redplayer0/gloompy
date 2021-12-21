# Useful drawing functions

import pyxel

from hexlib import *

# Layouts
normal_layout = Layout(layout_flat, Point(14, 14), Point(0, 0))

# Draws a hex by drawing lines connecting all corners.
def draw_hex(hex_corners, color):
    for p in range(5):
        x1 = hex_corners[p].x
        y1 = hex_corners[p].y
        x2 = hex_corners[p+1].x
        y2 = hex_corners[p+1].y
        pyxel.line(x1, y1, x2, y2, color)
    x1 = hex_corners[0].x
    y1 = hex_corners[0].y
    pyxel.line(x2, y2, x1, y1, color)


def draw_grid(grid, color):# TODO refactor to draw_hex and rename it to draw_grid maybe
    for hex in grid:
        hex_corners = polygon_corners(normal_layout, hex)
        draw_hex(hex_corners, color)

def draw_cursor_cell(color):
    active_hex = hex_round(pixel_to_hex(normal_layout, Point(pyxel.mouse_x, pyxel.mouse_y)))
    active_corners = polygon_corners(normal_layout, active_hex)
    draw_hex(active_corners, color)
