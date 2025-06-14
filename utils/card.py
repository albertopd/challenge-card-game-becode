from colorama import Fore, Back, Style


class Symbol:
    """
    Class to encapsulate a Symbol object.
    """

    # Allowed colors
    RED_COLOR = "RED"
    BLACK_COLOR = "BLACK"

    # Allowed symbols group by color
    RED_SYMBOLS = ('♥', '♦')
    BLACK_SYMBOLS = ('♣', '♠')

    def __init__(self, icon: str) -> None:
        """
        Constructor for creating a new Symbol object with the specified icon.
        The object symbol will have a color depending on the icon:
        Red for: ♥, ♦
        Black for: ♣, ♠

        :param icon: A str containing one of the characters [♥,♦,♣,♠].
        """
        self.icon = icon

    @property
    def icon(self) -> str:
        """
        Property that returns the icon of the Symbol.

        :return: A str representing the icon.
        """
        return self._icon

    @icon.setter
    def icon(self, icon: str):
        """
        Property setter that updates the icon of the Symbol.

        :param icon: A str representing the icon.
        """
        if icon in self.RED_SYMBOLS:
            self._color = self.RED_COLOR
        elif icon in self.BLACK_SYMBOLS:
            self._color = self.BLACK_COLOR
        else:
            raise ValueError(f"Invalid icon {icon}. Allowed icons: {self.RED_SYMBOLS + self.BLACK_SYMBOLS}")
        self._icon = icon

    @property
    def color(self) -> str:
        """
        Property that returns the color of the Symbol.

        :return: A str representing the color.
        """
        return self._color

    def __str__(self) -> str:
        """
        Method that returns a string representation of a Symbol object.

        :return: A str containing the description of the symbnol in the form of: icon color.
        """
        return f"{self._icon} {self._color}"


class Card(Symbol):
    """
    Class to encapsulate a Card object.
    """

    # Allowed values for a card
    CARD_VALUES = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, icon: str, value: str) -> None:
        """
        Constructor for creating a new Card object with the specified params.

        :param icon: A str containing one of the symbol characters [♥,♦,♣,♠].
        :param value: A str containing one of the following values:
                        ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K'].
        """
        super().__init__(icon)
        self.value = value

    @property
    def value(self) -> str:
        """
        Property that returns the value of the Card.

        :return: A str representing the value.
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """
        Property setter that updates the value of the Card.

        :param value: A str representing the value which must be one of these: ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']
        """
        if value not in self.CARD_VALUES:
            raise ValueError(f"Invalid value {value}. Allowed values: {self.CARD_VALUES}")
        else:
            self._value = value

    def __str__(self) -> str:
        """
        Method that returns a string representation of a Card object.

        :return: A str containing the description of the card in the form of: value icon color.
        """
        return f"{Fore.RED if self._color == self.RED_COLOR else Fore.BLACK}{Back.WHITE}[{self.value}|{self.icon}]{Style.RESET_ALL}"
