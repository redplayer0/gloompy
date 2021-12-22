import pyxel

from draw_functions import *
from hexlib import *
from loader import *


# Main class wrapping pyxel
class GloomPy:
    def __init__(self):
        pyxel.init(width, height)
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
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 0, 16, 16, pyxel.COLOR_BLACK)
        pyxel.text(width - 100, height - 20, f"x:{pyxel.mouse_x} y:{pyxel.mouse_y}", pyxel.COLOR_BLACK)


# Runs the game
GloomPy()
