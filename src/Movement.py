from Screen import game_board


def key(game_board, stdscr):

    while True:
        stdscr.getch()
        key = stdscr.getch()

        if key == ord("q"):
            break
        if key == ord("w"):
            pass

    return 0
    



def update(game_board, stdscr):
    return 0

print(game_board)