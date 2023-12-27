import pygame
class Piece:
    def __init__(self,position,nature,colour):
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.nature = None
        self.colour = None

class Pawn(Piece):
    def __init__(self,position,colour):
        super().__init__(position,colour)

    def move(self):
        pass