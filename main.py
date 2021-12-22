import pyxel

from graphics import *
from hexlib import *
from utils import *


# Main class wrapping pyxel
class GloomPy:
    def __init__(self):
        pyxel.init(width, height, title="GloomPy")
        pyxel.load("my_resource.pyxres")
        # pyxel.clip(200, 200, 200, 200)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        adjust_camera()

    def draw(self):
        pyxel.cls(pyxel.COLOR_WHITE)
        draw_grid(grid, pyxel.COLOR_BROWN)
        draw_cursor_cell(pyxel.COLOR_YELLOW)
        draw_characters(chars)
        # pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 0, 16, 16, pyxel.COLOR_BLACK)
        pyxel.text(0, 0, f"x:{pyxel.mouse_x} y:{pyxel.mouse_y}", pyxel.COLOR_BLACK)

# Game setup
file = "chapter1.txt"
grid = load_grid_file(file)
char_positions = []

chars = [
        Character(
                Sprite(1, 1),
                "rogue",
                "Ilya",
                1,
                0,
                11,
                11,
                0,
                [],
                [],
                [],
    )
]

# TODO make a fuction to assign initial positions to chars
assign_position(chars[0], rdoubled_to_cube(DoubledCoord(4,6)), char_positions)

# Runs the game
GloomPy()
