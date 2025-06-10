
class Symbol:
    """
    Class to encapsulate a symbol object.
    """

    # Allowed colors
    RED_COLOR = "RED"
    BLACK_COLOR = "BLACK"

    # Allowed symbols group by color
    RED_SYMBOLS = ('♥', '♦')
    BLACK_SYMBOLS = ('♣', '♠')

    def __init__(self, icon: str) -> None:
        """
        Construct a new instance of Symbol with the specified icon.
        The object symbol will have a color depending on the icon:
        Red for: ♥, ♦
        Black for: ♣, ♠

        :param icon: A str containing one of the symbol characters [♥,♦,♣,♠].
        """        
        self.icon = icon

    @property
    def icon(self):
        return self.icon
 
    @icon.setter
    def icon(self, icon):
        if icon in self.RED_SYMBOLS:
            self.color = self.RED_COLOR
        elif icon in self.BLACK_SYMBOLS:
            self.color = self.BLACK_COLOR
        else:
            raise Exception(f"Invalid icon {icon}. Allowed icons: {self.RED_SYMBOLS + self.BLACK_SYMBOLS}")
        self._icon = icon

    @property
    def color(self):
        return self.color
    
    @color.setter
    def color(self, color):
        if color in (self.RED_COLOR, self.BLACK_COLOR):
            self._color = color
        else:
            raise Exception(f"Invalid color {color}. Allowed colors: {self.RED_COLOR}, {self.BLACK_COLOR}")

    def __str__(self) -> str:
        return f"{self._icon} {self._color}"
   

class Card(Symbol):
    """
    Class to encapsulate a card object.
    """

    # Allowed values for a card
    CARD_VALUES = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, icon: str, value: str) -> None:
        """
        Construct a new instance of Card with the specified params.

        :param icon: A str containing one of the symbol characters [♥,♦,♣,♠].
        :param value: A str containing one of the following values:
                        ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K'].
        """
        super().__init__(icon)
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} {super().__str__()}"
