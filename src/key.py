import curses
import random
import time
import numpy as np
from curses import wrapper
from Screen import *

def key(game_board, stdscr):

    key = "w"

    while True:
        stdscr.getch()
        key = stdscr.getch()

        if key == ord("q"):
            break
        elif key == ord("w"):
            return 1
        elif key == ord("a"):
            return 2
        elif key == ord("s"):
            return 3
        elif key == ord("d"):
            return 4
        else:
            pass # Real Pass

    return 0

def update(game_board, stdscr):
    return 0

def tracking(game_board, stdscr):
    for i, line in enumerate(game_board):
        for j, value in enumerate(line):
            if game_board[i][j] == "X":
                x = [i, j]
                print(x)