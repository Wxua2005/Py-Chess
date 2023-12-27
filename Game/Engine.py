import pygame
from debug import SQUARE_SIZE,IMAGES,PIECES
from debug import load_images

NOTATION_LETTER = {0 : "A",
           1 : "B",
           2 : "C",
           3 : "D",
           4 : "E",
           5 : "F",
           6 : "G",
           7 : "H"}

NOTATION_NUMBER = {
    0 : "8",
    1 : "7",
    2 : "6",
    3 : "5",
    4 : "4",
    5 : "3",
    6 : "2",
    7 : "1"
}

class Gamestate:
    def __init__(self):
        self.board = [['bR','bN','bB','bQ','bK','bB','bK','bR'],
                      ['bp','bp','bp','bp','bp','bp','bp','bp'],
                      ['--','--','--','--','--','--','--','--'],
                      ['--','--','--','--','--','--','--','--'],
                      ['--','--','--','--','--','--','--','--'],
                      ['--','--','--','--','--','--','--','--'],
                      ['wp','wp','wp','wp','wp','wp','wp','wp'],
                      ['wR','wN','wB','wQ','wK','wB','wN','wR']]
        self.whitetoMove = True
        self.movelog = []

class Move(Gamestate):
    def __init__(self):
        super().__init__()
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.col = self.x // SQUARE_SIZE
        self.row = self.y // SQUARE_SIZE
        load_images()

    def mouseLocation(self):
        return (self.row,self.col)

    def notation(self):
        return NOTATION_LETTER[self.col] + NOTATION_NUMBER[self.row]

    def highlight(self,screen):
        highlight_square = pygame.Rect((self.col * SQUARE_SIZE),(self.row * SQUARE_SIZE),SQUARE_SIZE,SQUARE_SIZE)
        pygame.draw.rect(screen,(255,255,0,128),highlight_square)

        piece = self.board[self.row][self.col]
        if piece != "--":
            screen.blit(IMAGES[piece],pygame.Rect(self.col*SQUARE_SIZE,self.row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
