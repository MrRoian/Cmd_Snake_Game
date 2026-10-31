import curses
import random
import numpy as np
from curses import wrapper
from Movement import key

game_board = [["#", "#", "#", "#", "#", "#", "#", "#", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", "X", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", "#", "#", "#", "#", "#", "#", "#", "#"]]



stdscr = curses.initscr()
stdscr.keypad(True)

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


def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)



    stdscr.clear()
    field(game_board, stdscr)
    player(game_board, stdscr)
    stdscr.refresh()
    key()

wrapper(main)