# Useful drawing functions
import pyxel

from hexlib import *
from settings import *

    
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
def draw_hex(hex, color):
    hex_corners = polygon_corners(layout, hex)
    for p in range(5):
        pyxel.line(hex_corners[p].x, hex_corners[p].y, hex_corners[p+1].x, hex_corners[p+1].y, color)
    pyxel.line(hex_corners[0].x, hex_corners[0].y, hex_corners[5].x, hex_corners[5].y, color)

def draw_iner_hex(hex, px, color):
    hex_corners = polygon_corners(layout, hex)
    pyxel.line(hex_corners[0].x-px, hex_corners[0].y, hex_corners[1].x-px, hex_corners[1].y, color)
    pyxel.line(hex_corners[1].x-px, hex_corners[1].y, hex_corners[2].x, hex_corners[2].y+px, color)
    pyxel.line(hex_corners[2].x, hex_corners[2].y+px, hex_corners[3].x+px, hex_corners[3].y, color)
    pyxel.line(hex_corners[3].x+px, hex_corners[3].y, hex_corners[4].x+px, hex_corners[4].y, color)
    pyxel.line(hex_corners[4].x+px, hex_corners[4].y, hex_corners[5].x, hex_corners[5].y-px, color)
    pyxel.line(hex_corners[5].x, hex_corners[5].y-px, hex_corners[0].x-px, hex_corners[0].y, color)


def draw_grid(grid, color):  # TODO refactor to draw_hex and rename it to draw_grid maybe
    for hex in grid:
        draw_hex(hex, color)

def draw_iner_grid(grid, px, color):  # TODO refactor to draw_hex and rename it to draw_grid maybe
    for hex in grid:
        for p in range(1, px+1):
            draw_iner_hex(hex, p, color)

def draw_characters(chars, hex_size):
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
        
def draw_hps(chars, hex_size):
    for char in chars:
        #TODO add a try block in case a char does not have a valid position
        p = hex_to_pixel(layout, char.position)
        pyxel.text(
                p.x - hex_size.x/2 - 2,
                p.y - hex_size.y/2,
                f"{char.maxhp}/{char.hp}\nTEST",
                pyxel.COLOR_BLACK,
)
