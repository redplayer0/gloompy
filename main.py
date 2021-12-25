import pyxel

from engine import *
from graphics import *
from hexlib import *
from settings import *
from utils import *


# Main class wrapping pyxel
class GloomPy:
    def __init__(self):
        pyxel.init(width, height, title=title)
        pyxel.load("my_resource.pyxres")
        # pyxel.clip(200, 200, 200, 200)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        global selected_cells
        global toggle
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_T):
            toggle = not toggle
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if active_hex() in grid:
                selected_cells.add(active_hex())
        if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
            try:
                selected_cells.remove(active_hex())
            except:
                pass

        adjust_camera()

    def draw(self):
        pyxel.cls(pyxel.COLOR_WHITE)
        draw_grid(grid, pyxel.COLOR_GRAY)
        if selected_cells:
            draw_iner_grid(selected_cells, 2, pyxel.COLOR_DARK_BLUE)
        draw_iner_hex(active_hex(), 1, pyxel.COLOR_YELLOW)
        if toggle:
            draw_characters(chars, hex_size)
        else:
            draw_hps(chars, hex_size)
        # pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 0, 16, 16, pyxel.COLOR_BLACK)
        pyxel.text(
            0, 0, f"x:{pyxel.mouse_x} y:{pyxel.mouse_y}", pyxel.COLOR_BLACK)


# Game setup

file = "chapter1.txt"
grid = load_grid_file(file)
char_positions = []
selected_cells = set()

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
assign_position(chars[0], rdoubled_to_cube(DoubledCoord(4, 6)), char_positions)

# Runs the game
GloomPy()
