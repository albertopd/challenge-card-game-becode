from utils.player import Player
from utils.game import Board

players = [Player("Alb"), Player("Sof"), Player("Evi")]

board = Board(players)
board.start_game()
