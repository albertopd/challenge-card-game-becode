from typing import List
from utils.card import Card
from utils.deck import Deck
from utils.player import Player


class Board:
    """
    Class to encapsulate a board game object.
    """

    def __init__(self, players: List[Player], equal_num_of_cards: bool = False) -> None:
        """
        Constructor for creating a new Board object.

        :param players: A list of Player objects.
        :param equal_num_of_cards: A bool to enforce the same number of cards per player (default is False).
        """     
        self.players = players
        self.equal_num_of_cards = equal_num_of_cards
        self.turn_count = 0
        # List of last cards played by each player.
        self.active_cards: List[Card | None] = [None for _ in range(len(players))]
        # List of all the cards played since the start of the game, except for active_cards.
        self.history_cards: List[Card] = []

    def __str__(self) -> str:
        """
        Method that returns a string representation of a Board object.

        :return: A str containing the current turn + number of card in the history + active cards.
        """
        return f"TURN {self.turn_count} | {len(self.history_cards)} cards in history | Active cards: {", ".join([str(card) for card in self.active_cards])}"
    
    def start_game(self) -> None:
        """
        Method that start a card game and runs until all cards all played.
        """
        print(">>> Game started!")

        # Fill a Deck and shuffle it
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()

        # Distribute the cards on the Deck to the players
        distributed_cards = deck.distribute(self.players, self.equal_num_of_cards)

        for player in self.players:
            print(f"Player {player.name} got {len(player.cards)} cards")

        cards_played = 0

        # Do turns until all cards are played
        while cards_played < distributed_cards:

            for player_index in range(len(self.players)):

                current_player = self.players[player_index]

                # Make each Player play a card (if they still have some to play)
                played_card = current_player.play()

                if played_card:
                    # Set the last card played by the current player
                    self.active_cards[player_index] = played_card

                    # If if not the last card of the player
                    # we add it to the board history
                    if current_player.number_of_cards > 0:
                        self.history_cards.append(played_card)

                    cards_played += 1

            self.turn_count += 1

            print(self)
        
        print("<<< Game ended!")
