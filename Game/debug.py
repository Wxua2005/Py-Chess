import pygame
import sys
import Engine


pygame.init()

# Parameter variables
WIDTH , HEIGHT = 400 , 400
clock = pygame.time.Clock()
FPS = 120
running = True
GRAY = pygame.Color('gray')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SQUARE_SIZE = 600 // 12
IMAGES = {}
PIECES = ['wp','wK','wQ','wB','wN','wR','bp','bK','bQ','bB','bN','bR']

def load_images():
    for piece in PIECES:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("Images/" + piece + ".png").convert_alpha(),(SQUARE_SIZE,SQUARE_SIZE))


def drawBoard(screen):
    for ROW in range(8):
        for COLUMN in range(8):
            color = WHITE if (ROW + COLUMN) % 2 == 0 else GRAY
            square = pygame.Rect(COLUMN * SQUARE_SIZE, ROW * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, square)


def drawPieces(screen,board):
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece],pygame.Rect(c*SQUARE_SIZE,r*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))

def drawGameState(screen,gs):
    drawBoard(screen)
    drawPieces(screen,gs.board)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    caption = pygame.display.set_caption("Chess Game")
    window_icon = pygame.image.load(r'C:\Users\drpre\Downloads\download.png')
    pygame.display.set_icon(window_icon)
    screen.fill(BLACK)
    gs = Engine.Gamestate()

    load_images()
    drawGameState(screen,gs)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                tst = Engine.Move()
                tst.highlight(screen)

        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()