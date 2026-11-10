import curses
import random
import numpy as np
import time
from curses import wrapper
from Func import *

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

def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    stdscr.clear()
    field(game_board, stdscr)
    player(game_board, stdscr)
    key(game_board, stdscr)
    stdscr.refresh()

wrapper(main)

# Todo List
# Make GameOver Thing ig