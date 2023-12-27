import pygame
import sys

# Constants
WIDTH, HEIGHT = 400, 400
SQUARE_SIZE = WIDTH // 8
BOARD_COLOR = (255, 255, 255)
HIGHLIGHT_COLOR = (255, 255, 0, 128)  # Yellow with 50% transparency

def draw_board(screen):
    for row in range(8):
        for col in range(8):
            color = (0, 0, 0) if (row + col) % 2 == 0 else (255, 255, 255)
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Board Highlight")

    clock = pygame.time.Clock()

    highlighted_square = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Get the mouse position
                mouse_x, mouse_y = event.pos

                # Determine the clicked square
                clicked_square = (mouse_x // SQUARE_SIZE, mouse_y // SQUARE_SIZE)

                # Toggle highlighting
                if clicked_square == highlighted_square:
                    highlighted_square = None
                else:
                    highlighted_square = clicked_square

        # Draw the chess board
        draw_board(screen)

        # Highlight the clicked square
        if highlighted_square is not None:
            highlight_rect = pygame.Rect(
                highlighted_square[0] * SQUARE_SIZE,
                highlighted_square[1] * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE
            )
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, highlight_rect)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
