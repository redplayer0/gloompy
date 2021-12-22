# Useful drawing functions

import pyxel

from hexlib import *

width = 260
height = 260
camera = Point(0, 0)
hex_size = Point(14, 14)
# Layouts
layout = Layout(layout_pointy, hex_size, camera)

# TODO adjust camera with keys instead of cursor position
def adjust_camera():
    global camera
    global layout
    if pyxel.btn(pyxel.KEY_RIGHT):
        camera = Point(camera.x - 5, camera.y)
    if pyxel.btn(pyxel.KEY_DOWN):
        camera = Point(camera.x ,camera.y - 5)
    if pyxel.btn(pyxel.KEY_LEFT):
        camera = Point(camera.x + 5, camera.y)
    if pyxel.btn(pyxel.KEY_UP):
        camera = Point(camera.x ,camera.y + 5)
    layout = Layout(layout_pointy, hex_size, camera)


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


def draw_grid(grid, color):  # TODO refactor to draw_hex and rename it to draw_grid maybe
    for hex in grid:
        hex_corners = polygon_corners(layout, hex)
        draw_hex(hex_corners, color)


def draw_cursor_cell(color):
    active_hex = hex_round(pixel_to_hex(
        layout, Point(pyxel.mouse_x, pyxel.mouse_y)))
    active_corners = polygon_corners(layout, active_hex)
    draw_hex(active_corners, color)


def draw_characters(chars):
    for char in chars:
        #TODO add a try block in case a char does not have a valid position
        p = hex_to_pixel(layout, char.position)
        pyxel.blt(
                p.x - hex_size.x/2,
                p.y - hex_size.y/2,
                0,
                char.sprite.row*16,
                char.sprite.col*16,
                16,
                16,
                pyxel.COLOR_BLACK,
)
        
       
