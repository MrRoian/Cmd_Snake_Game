import curses
import random
import time
import numpy as np
from curses import wrapper


def tracking(game_board):

    for i, line in enumerate(game_board):
        for j, value in enumerate(line):
            if game_board[i][j] == "X":
                x = [i, j]

    return x

def key(gd, stdscr):    

    a = 1
    IsGameOn = True
    stdscr.nodelay(True)
    game_board = gd

    while IsGameOn:
        key = stdscr.getch()

        if key == ord("q"):
            break
        elif key == ord("w"):
            a = 1
        elif key == ord("a"):
            a = 2
        elif key == ord("s"):
            a = 3
        elif key == ord("d"):
            a = 4
        else:
            pass # Real Pass
        
        IsGameOn = update(a, game_board, stdscr)

def update(dir, game_board, stdscr):

    x = tracking(game_board)

    if dir == 1:
        line, colum = -1, 0

    elif dir == 2:
        line, colum = 0, -1

    elif dir == 3:
        line, colum = 1, 0

    elif dir == 4:
        line, colum = 0, 1

    else:
        pass


    game_board[x[0]][x[1]] = " " # before x gonna edit
    x[0] = x[0]+(line) # editing
    x[1] = x[1]+(colum) # editing

    if game_board[x[0]][x[1]] == "#": # game over check
        stdscr.clear()
        stdscr.addstr("Game Over")
        stdscr.refresh()
        return False
    else:
        game_board[x[0]][x[1]] = "X"

        stdscr.clear()
        field(game_board, stdscr)
        player(game_board, stdscr)
        stdscr.refresh()
        time.sleep(0.5)
        return True



def field(game_board, stdscr):

    WHITE = curses.color_pair(1)

    for i, r in enumerate(game_board):
        for j, char in enumerate(r):
            stdscr.addstr(i, j*3, char, WHITE)


def player(game_board, stdscr):

    GREEN = curses.color_pair(2)

    for i, r in enumerate(game_board):
        for j, char in enumerate(r):
            if char == "X":
                stdscr.addstr(i, j*3, char, GREEN)
            else:
                continue