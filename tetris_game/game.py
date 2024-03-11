from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.block = [IBlock(), OBlock(), JBlock(), LBlock(), SBlock(), ZBlock(), TBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
       
    def get_random_block(self):
        if len(self.block) == 0:
            self.block = [IBlock(), OBlock(), JBlock(), LBlock(), SBlock(), ZBlock(), TBlock()]
        block = random.choice(self.block)
        self.block.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False:
            self.current_block.move(-1, 0)

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False:
            self.current_block.under_rotate()

    def drop(self):
        self.current_block.move(1, 0)

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
        self.next_block.draw(screen)