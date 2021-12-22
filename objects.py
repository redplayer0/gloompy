from collections import namedtuple

import pyxel

from hexlib import *

HexData = namedtuple("HexData", ["id", "door", "block_direction", "trap", "loot"])
default_hex_data = HexData(
                        id=None,
                        door=None,
                        block_direction=None,
                        trap=False,
                        loot=False,
)

Sprite = namedtuple("Sprite", ["row", "col"])



class Character:
    def __init__(self, sprite, job, name, lv, exp, maxhp, hp, gold, attack_deck, player_deck, perks):
        self.sprite = sprite
        self.job = job
        self.name = name
        self.lv = lv
        self.exp = exp
        self.maxhp = maxhp
        self.hp = hp
        self.gold = gold
        self.attack_deck = attack_deck
        self.player_deck = player_deck
        self.perks = perks
        self.position = Hex(None, None, None)
        self.status = None
        

class AttackDeck:
    def __init__(self):
        self.cards = []
        self.discarded = []

    def shufle(self):
        pass

    def draw(self):
        pass


class PlayerDeck:
    def __init__(self):
        self.cards = []
        self.discarded = []
        self.burned = []

    def shufle(self):
        pass

    def select(self):
        pass
