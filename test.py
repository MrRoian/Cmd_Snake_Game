import random

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


# game_board[x[0]][x[1]] = " "
# x[0] = x[0]+(-1)
# x[1] = x[1]+1
# print(x)
# game_board[x[0]][x[1]] = "X"
            


def random_range(game_board):

    apple_spawn_range = []

    for i, line in enumerate(game_board):
        for j, value in enumerate(line):
            if game_board[i][j] == "#" or game_board[i][j] == "X":
                pass
            else:
                apple_spawn_range.append([i, j])


    return apple_spawn_range

where_apple_able_to_spawn = random_range(game_board)

apple_spawn = random.choice(where_apple_able_to_spawn)
print(apple_spawn)

game_board[apple_spawn[0]][apple_spawn[1]] = "A"

for i, index in enumerate(game_board):
    print(i, index)