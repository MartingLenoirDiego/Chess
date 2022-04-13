import pieces
import pygame
import sys
white = [[1, 1, 1, 1, 1, 1, 1, 1], [2, 3, 4, 5, 6, 4, 3, 2]]
black = [[2, 3, 4, 5, 6, 4, 3, 2], [1, 1, 1, 1, 1, 1, 1, 1]]
pygame.init()
size = width, height = 1080, 1000
screen = pygame.display.set_mode(size)
BLACK = (252, 233, 192)
WHITE = (128, 109, 137)
GRAY = (136, 38, 0)


def init_pieces(tab, row, color, img):
    for i in range(2):
        for j in range(8):
            if tab[i][j] == 1:
                tab[i][j] = pieces.Pawn(100*j+150, 100*row+150, color, img + '-pawn.png')
            if tab[i][j] == 2:
                tab[i][j] = pieces.Rook(100*j+150, 100*row+150, color, img + '-rook.png')
            if tab[i][j] == 3:
                tab[i][j] = pieces.Knight(100*j+150, 100*row+150, color, img + '-knight.png')
            if tab[i][j] == 4:
                tab[i][j] = pieces.Bishop(100*j+150, 100*row+150, color, img + '-bishop.png')
            if tab[i][j] == 5:
                tab[i][j] = pieces.Queen(100*j+150, 100*row+150, color, img + '-queen.png')
            if tab[i][j] == 6:
                tab[i][j] = pieces.King(100*j+150, 100*row+150, color, img + '-king.png')
        row = row + 1


def main():
    init_pieces(white, 6, 'white', 'w')
    init_pieces(black, 0, 'black', 'b')
    display()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    x, y = pygame.mouse.get_pos()
                    print('mouse', x, y)
                    pos(white, x, y)
                    pos(black, x, y)


def pos(color, x, y):
    for i in range(len(color)):
        for j in range(len(color[i])):
            if color[i][j].x - 50 < x < color[i][j].x + 50 and color[i][j].y - 50 < y < color[i][j].y + 50:
                color[i][j].movement(white)
                print(color[i][j].mov)

            for k in range(len(color[i][j].mov)):
                if color[i][j].mov[k][0] - 50 < x < color[i][j].mov[k][0] + 50 and color[i][j].mov[k][1] - 50 < y < \
                        color[i][j].mov[k][1] + 50:
                    color[i][j].shift(color[i][j].mov[k][0], color[i][j].mov[k][1])
                    display()


def display():
    screen.fill(GRAY)
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    pygame.draw.rect(screen, WHITE, (100 * j + 100, i * 100 + 100, 100, 100))
                else:
                    pygame.draw.rect(screen, BLACK, (100 * j + 100, i * 100 + 100, 100, 100))
            if i % 2 != 0:
                if j % 2 != 0:
                    pygame.draw.rect(screen, WHITE, (100 * j + 100, i * 100 + 100, 100, 100))
                else:
                    pygame.draw.rect(screen, BLACK, (100 * j + 100, i * 100 + 100, 100, 100))
    for i in range(len(white)):
        for j in range(len(white[i])):
            white[i][j].draw()
            black[i][j].draw()
    pygame.display.flip()


if __name__ == "__main__":
    main()
