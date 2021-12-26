from __future__ import annotations
from abc import ABC, abstractmethod

import pyxel

from objects import *
from graphics import *
from hexlib import *
import utils
from time import sleep

class Context:

    _state = None

    screen_width = 240
    screen_height = 240
    title = "Test"

    hex_grid = {}
    hex_size = Point(14, 14)
    camera = Point(0, 0)
    

    allies = [
        Character(
            Sprite(0, 0),
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
        ),
        Character(
            Sprite(0, 1),
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
        ),
        Character(
            Sprite(0, 2),
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
        ),
    ]

    enemies = {}
    positions = {}
    selected_hexes = set()


    layout = Layout(layout_pointy, hex_size, camera)
    

    def __init__(self, state: State):
        pyxel.init(self.screen_width, self.screen_height, self.title, 30)
        pyxel.load("my_resource.pyxres")
        self.setState(state)

    def setState(self, state: State):
        self._state = state
        self._state.context = self

    def update(self):
        self._state.update()
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_RIGHT):
            self._state.onButtonRight()

        if pyxel.btn(pyxel.KEY_LEFT):
            self._state.onButtonLeft()

        if pyxel.btn(pyxel.KEY_UP):
            self._state.onButtonUp()

        if pyxel.btn(pyxel.KEY_DOWN):
            self._state.onButtonDown()

        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            self._state.onMouseLeftClick()

        if pyxel.btnr(pyxel.MOUSE_BUTTON_RIGHT):
            self._state.onMouseRightClick()


    def draw(self):
        pyxel.cls(pyxel.COLOR_WHITE) 
        draw_hex_grid(self.hex_grid, self.layout, pyxel.COLOR_GRAY)
        draw_characters(self.positions, self.layout, self.hex_size)  
        draw_iner_hex(self.active_hex, 1, self.layout, pyxel.COLOR_YELLOW)

        pyxel.text(0, 0, f"x:{pyxel.mouse_x} y:{pyxel.mouse_y}", pyxel.COLOR_BLACK)

        self._state.draw()

    def run(self):
        pyxel.run(self.update, self.draw)


    @property
    def active_hex(self):
        return hex_round(pixel_to_hex(self.layout, Point(pyxel.mouse_x, pyxel.mouse_y)))


class State(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context: Context):
        self._context = context

    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass

class LoadChapter(State):
    def __init__(self, chapter):
        self.chapter = chapter

    def update(self):
        self._context.hex_grid = utils.load_grid_file(self.chapter)
        self._context.setState(AssignPositions())

    def draw(self):
        pass


class AssignPositions(State):
    char = None

    def update(self):
        if not self.char and self._context.allies:
            self.char = self._context.allies.pop(0)
        if not self.char and not self._context.allies:
            self._context.setState(SelectCards())
    
    def onButtonRight(self):
        self._context.camera = Point(self._context.camera.x - 5, self._context.camera.y)
        self._context.layout = Layout(layout_pointy, self._context.hex_size, self._context.camera)

    def onButtonDown(self):
        self._context.camera = Point(self._context.camera.x, self._context.camera.y - 5)
        self._context.layout = Layout(layout_pointy, self._context.hex_size, self._context.camera)
    
    def onButtonLeft(self):
        self._context.camera = Point(self._context.camera.x + 5, self._context.camera.y)
        self._context.layout = Layout(layout_pointy, self._context.hex_size, self._context.camera)
    
    def onButtonUp(self):
        self._context.camera = Point(self._context.camera.x, self._context.camera.y + 5)
        self._context.layout = Layout(layout_pointy, self._context.hex_size, self._context.camera)

    def onMouseLeftClick(self):
        hex = self._context.active_hex
        utils.assign_position(self.char, hex, self._context.positions)
        self.char = None

    def onMouseRightClick(self):
        self._context.selected_hexes.remove(self._context.active_hex)

    def draw(self):
        if self.char:
            draw_char(self.char)
        
        

# class SelectHex(AssignPositions):
#     def __init__(self, char):
#         self.char = char
# 
#     def update(self):
#         pass
# 
#     def draw(self):
#         pass

# Initialize and run the game.
game = Context(LoadChapter("chapter1.txt"))
game.run()
