import pyxel

from draw_functions import *
from hexlib import *
from loader import *


# Main class wrapping pyxel
class GloomPy:
    def __init__(self):
        pyxel.init(260, 260)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        draw_grid(grid, pyxel.COLOR_GRAY)
        draw_cursor_cell(pyxel.COLOR_YELLOW)



# Runs the game
GloomPy()
