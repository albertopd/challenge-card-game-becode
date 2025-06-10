import random
from typing import List
from utils.card import Card
from utils.card import Symbol
from utils.player import Player


class Deck:
    """
    Class to encapsulate a Deck object that contains a list of cards
    """

    def __init__(self) -> None:
        """
        Constructor for creating a new Deck object with an empty list of cards.
        """
        self.cards: List[Card] = []

    def __str__(self) -> str:
        """
        Method that returns a string representation of a Deck object.

        :return: A str containing the comma separated list of all the cards in the deck.
        """
        return ", ".join([str(card) for card in self.cards])

    def fill_deck(self) -> None:
        """
        Method that will fill cards with a complete card game 
        (an instance of 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K')
        for each possible symbol [♥, ♦, ♣, ♠]).
        """
        self.cards = [Card(icon, value) for icon in Symbol.RED_SYMBOLS + Symbol.BLACK_SYMBOLS for value in Card.CARD_VALUES]

    def shuffle(self) -> None:
        """
        Method that will shuffle all cards in the list.
        """
        random.shuffle(self.cards)

    def distribute(self, players: List[Player], equal_num_of_cards: bool = False) -> int:
        """
        Method that take a list of Player as parameter and will distribute
        the cards evenly between all the players.

        :param players: A list of objects Player to which the cards should be distribute to.
        :param equal_num_of_cards: A bool to enforce the same number of cards per player (default is False).
        :return: An int representing the number of distributed cards.
        """
        if players:
            player_index = 0

            if equal_num_of_cards:
                num_cards_to_distribute = (len(self.cards) // len(players)) * len(players)
            else:
                num_cards_to_distribute = len(self.cards)

            for _ in range(num_cards_to_distribute):
                card = self.cards.pop()
                player = players[player_index]

                player.receive_card(card)

                if player_index == len(players) - 1:
                    player_index = 0
                else:
                    player_index += 1

            return num_cards_to_distribute
        else:
            return 0
