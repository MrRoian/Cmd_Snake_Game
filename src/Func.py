import curses
import random
import time
import numpy as np
from curses import wrapper

saved = []
score = 0


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
    apple(game_board)

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

    
    global score
    global saved

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

    saved.append([x[0], x[1]])
    print(saved)

    game_board[x[0]][x[1]] = " " # before x gonna edit
    x[0] = x[0]+(line) # editing
    x[1] = x[1]+(colum) # editing

    if game_board[x[0]][x[1]] == "#": # game over check
        print("Game Over")
        print(f"Score: {score}")
        return False
    else:
        if game_board[x[0]][x[1]] == "A":
            apple(game_board)
            score += 1

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


def apple(game_board):

    RED = curses.color_pair(3)
    apple_spawn_range = []

    for i, r in enumerate(game_board):
        for j, char in enumerate(r):
            if game_board[i][j] == "#" or game_board[i][j] == "X":
                pass
            else:
                apple_spawn_range.append([i, j])

    apple_spawn = random.choice(apple_spawn_range)
    game_board[apple_spawn[0]][apple_spawn[1]] = "A"