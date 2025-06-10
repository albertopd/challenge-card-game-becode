import random
from typing import List
from utils.card import Card


class Player:
    """
    Class to encapsulate a player object.
    """

    def __init__(self, name) -> None:
        self.name = name
        self.cards: List[Card] = []
        self.turn_count = 0
        self.history: List[Card] = []

    def __str__(self) -> str:
        return f"Player {self.name} on turn {self.turn_count}"
    
    @property
    def number_of_cards(self) -> int:
        return len(self.cards)
    
    def receive_card(self, card: Card):
        self.cards.append(card)
    
    def play(self) -> Card | None:
        # Randomly pick a card to play and 
        # add it to the Player's history
        if self.cards:
            card = self.cards.pop(random.randrange(len(self.cards)))
            self.history.append(card)
            self.turn_count += 1
            print(f"{self} played {card}")
            return card
        else:
            return None
