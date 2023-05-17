import copy
import sys
import pygame
import random
import numpy as np

from var import *

# --- PYGAME SETUP ---

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill(BG_COLOR)

# ---CLASSES---


class Board:

    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.lines()

    def mark_squares(self, row, col, player):
        self.squares[row][col] = player

    def empty_squares(self, row, col):
        return self.squares[row][col] == 0

    def lines(self):
        # vertical
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0),
                         (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0),
                         (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)
        # horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE),
                         (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE),
                         (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

    def final_state(self, show=False):
        '''
            @return 0 if there is no win yet
            @return 1 if play 1 wins
            @return 2 if player 2 wins
        '''
        # VERTICAL W's
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20)
                    fPos = (col*SQSIZE + SQSIZE//2, HEIGHT - 20)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col]

        # HORIZONTAL W's
        for row in range(ROWS):
            if self.squares[round][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    iPos = (20, row * SQSIZE + SQSIZE//2)
                    fPos = (WIDTH - 20, row * SQSIZE+SQSIZE//2)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]


class Gameplay:
    def __init__(self) -> None:
        self.board = Board()
        self.player = 1

    def next_turn(self):
        self.player = self.player % 2 + 1


board = Board()
gameplay = Gameplay()

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(board.squares)
            pos = event.pos
            row = pos[1] // SQSIZE  # horizontal
            col = pos[0] // SQSIZE  # vertical
            # print(row, col)
            if board.empty_squares(row, col):
                board.mark_squares(row, col, gameplay.player)
                gameplay.next_turn()
                print(board.squares)

    pygame.display.update()

pygame.quit()
