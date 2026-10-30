import curses
from curses import wrapper

game_board = [["#", "#", "#", "#", "#", "#", "#", "#", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
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


def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)



    stdscr.clear()
    field(game_board, stdscr)
    stdscr.refresh()
    stdscr.getch()


wrapper(main)