import random
from typing import List
from utils.card import Card


class Player:
    """
    Class to encapsulate a player object.
    """

    def __init__(self, name) -> None:
        """
        Constructor for creating a new Player object.

        :param name: A str representing the name of the player.
        """
        self.name = name
        self.cards: List[Card] = []
        self.turn_count = 0
        self.history: List[Card] = []

    def __str__(self) -> str:
        """
        Method that returns a string representation of a Player object.

        :return: A str containing the name of the player and the turn.
        """
        return f"Player {self.name} on turn {self.turn_count}"
    
    @property
    def number_of_cards(self) -> int:
        """
        Property that returns the numbers of cards left in the player's hand.

        :return: An int representing the numbers of cards.
        """
        return len(self.cards)
    
    def receive_card(self, card: Card) -> None:
        """
        Method that add a Card to the player's hand.

        :param card: An object Card.
        """
        self.cards.append(card)
    
    def play(self) -> Card | None:
        """
        Method that Randomly pick a card to play and return it after adding it to the Player's history.

        :return: An object Card that gets randomily picked or None if the player doesn't have anyore cards to play.
        """
        if self.cards:
            card = self.cards.pop(random.randrange(len(self.cards)))
            self.history.append(card)
            self.turn_count += 1
            print(f"{self} played {card}")
            return card
        else:
            return None
