from rocket import Rocket, RocketBoard

board = RocketBoard(5)

# board.rockets[0].altitude = 40
# print(board.rockets[0].altitude)
print(board[0].get_distance(board[1]))
print(board[0].get_all_chosen_rockets_distances(board[1], board[2], board[3], board[4]))