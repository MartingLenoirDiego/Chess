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
    selected = None
    move = True
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                chess = white + black
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    x, y = pygame.mouse.get_pos()
                    selected = pos(x, y, chess)
                    move = True
                    if selected != None:
                        print(selected)
                        selected.movement(chess)
                        print(selected.mov)
                        while move:
                            for click in pygame.event.get():
                                if click.type == pygame.MOUSEBUTTONDOWN:
                                    x, y = pygame.mouse.get_pos()
                                    mouse_presses = pygame.mouse.get_pressed()
                                    if mouse_presses[0]:
                                        move = shift(selected, x, y)
                        display()






def shift(selected, x, y):
    for i in range(len(selected.mov)):
        if selected.mov[i][0] - 50 < x < selected.mov[i][0] + 50 and selected.mov[i][1] - 50 < y < selected.mov[i][1] + 50:
            selected.shift(selected.mov[i][0], selected.mov[i][1])
    return False


def pos(x, y, chess):
    for i in range(len(chess)):
        for j in range(len(chess[i])):
            if chess[i][j].x - 50 < x < chess[i][j].x + 50 and chess[i][j].y - 50 < y < chess[i][j].y + 50:
                selected = chess[i][j]
                return selected




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
