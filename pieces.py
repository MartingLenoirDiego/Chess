import pygame
from main import screen


class Piece:
    def __init__(self, x, y, color, img):
        self.x = x
        self.y = y
        self.color = color
        self.img = img

    def draw(self):
        img = pygame.image.load('./assets/'+self.img)
        img.convert()
        rect = img.get_rect()
        rect.center = self.x, self.y
        screen.blit(img, rect)
        pygame.display.update()

    def shift(self, x, y):
        self.x = x
        self.y = y


class Pawn(Piece):
    def __init__(self, x, y, color, img):
        Piece.__init__(self, x, y, color, img)
        self.mov = []

    def __str__(self):
        return 'P'

    def movement(self, board):
        self.mov = []
        if self.color == 'white':
            pygame.draw.circle(screen, (105, 105, 105), (self.x, self.y-100), 12)
            pygame.draw.circle(screen, (105, 105, 105), (self.x, self.y - 200), 12)
            self.mov.append((self.x, self.y - 100))
            self.mov.append((self.x, self.y - 200))
        else:
            pygame.draw.circle(screen, (105, 105, 105), (self.x, self.y+100), 12)
            pygame.draw.circle(screen, (105, 105, 105), (self.x, self.y + 200), 12)
            self.mov.append((self.x, self.y + 100))
            self.mov.append((self.x, self.y + 200))

        pygame.display.update()


class Rook(Piece):
    def __init__(self, x, y, color, img):
        Piece.__init__(self, x, y, color, img)
        self.mov = []

    def movement(self, board):
        self.mov = []
        col = True
        xg = -1
        xd = 1
        yh = -1
        yb = 1

        while col:
            for i in range(len(board)):
                for j in range(len(board[j])):
                    if 100 < self.x + xg * 100 < 900:
                        if board[i][j].x == self.x + xg * 100:
                            xg = -1555
                        else:
                            self.mov.append((self.x + xg * 100, self.y))

                    if 100 < self.x + xd * 100 < 900:
                        if board[i][j].x == self.x + xd * 100:
                            xg = -1555
                        else:
                            self.mov.append((self.x + xd * 100, self.y))

                    if 100 < self.y + yh * 100 < 900:
                        if board[i][j].y == self.y + yh * 100:
                            xg = -1555
                        else:
                            self.mov.append((self.x, self.y + yh * 100))

                    if 100 < self.y + yb * 100 < 900:
                        if board[i][j].y == self.y + yb * 100:
                            xg = -1555
                        else:
                            self.mov.append((self.x, self.y + yb * 100))




        for i in range(-8, 8):
            test = False
            if 100 < self.x+i*100 < 900 and i != 0:
                if i < 0:
                    for j in range(len(board)):
                        for k in range(len(board[j])):
                            if board[j][i].x == self.x + i * 100:
                                self.mov =[]
                            else:
                                self.mov.append((self.x + i * 100, self.y))
                if i > 0:
                    for j in range(len(board)):
                        for k in range(len(board[j])):
                            if not test:
                                if board[j][i].x == self.x + i * 100:
                                    test = True
                                else:
                                    self.mov.append((self.x + i * 100, self.y))

                self.mov.append((self.x + i * 100, self.y))

            if 100 < self.y+i*100 < 900 and i != 0:
                self.mov.append((self.x, self.y + i * 100))




        for i in range(len(self.mov)):
            pygame.draw.circle(screen, (105, 105, 105), (self.mov[i][0], self.mov[i][1]), 12)
            pygame.display.update()

    def __str__(self):
        return 'R'


class Knight(Piece):
    def __init__(self, x, y, color, img):
        Piece.__init__(self, x, y, color, img)
        self.mov = []

    def __str__(self):
        return 'C'


class Bishop(Piece):
    def __init__(self, x, y, color, img):
        Piece.__init__(self, x, y, color, img)
        self.mov = []

    def __str__(self):
        return 'B'


class Queen(Piece):
    def __init__(self, x, y, color, img):
        Piece.__init__(self, x, y, color, img)
        self.mov = []

    def __str__(self):
        return 'Q'


class King(Piece):
    def __init__(self, x, y, color, img):
        Piece.__init__(self, x, y, color, img)
        self.mov = []

    def __str__(self):
        return 'K'
