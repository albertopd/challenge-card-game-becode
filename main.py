from utils.player import Player
from utils.game import Board

# Create some players
players = [Player("Alb"), Player("Sof"), Player("Evi")]

# Create a board and specify to distribute an equal number of cards among all players 
board = Board(players, True)

board.start_game()
