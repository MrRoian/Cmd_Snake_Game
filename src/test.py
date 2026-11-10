game_board = [["#", "#", "#", "#", "#", "#", "#", "#", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", "X", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
              ["#", "#", "#", "#", "#", "#", "#", "#", "#"]]


# for i, index in enumerate(game_board):
#     print(i, index)

# for i, line in enumerate(game_board):
#     for j, value in enumerate(index):
#         if game_board[i][j] == "X":
#             print(f"X is on {i, j}")


for i, line in enumerate(game_board):
    for j, value in enumerate(line):
        if game_board[i][j] == "X":
            x = [i, j]
            print(x)


game_board[x[0]][x[1]] = " "
game_board[x[0]+(-1)][x[1]+1] = "X"
            


for i, index in enumerate(game_board):
    print(i, index)