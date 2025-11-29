class Card:
    """Гральна карта"""

    RANKS = ['Т', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'В', 'Д', 'К']
    # '♠', '♥', '♦', '♣'    
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666' ]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        rep = self.rank + self.suit
        return rep

class UnprintableCard(Card):
    """Гральна карта, яку не можна надрукувати"""

    def __str__(self):
        return "<не можна надрукована >"

class PositionableCard(Card):
    """Гральна карта, яку можна розмістити обличчям вгору або вниз"""

    def __init__(self, rank, suit, face_up=True):
        super().__init__(rank, suit)
        self.is_face_up = face_up
    
    def flip(self):
        """Перевернути карту"""
        self.is_face_up = not self.is_face_up
    
    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = "XX"
        return rep 


card1 = Card("К", Card.SUITS[0])
card2 = UnprintableCard("T", Card.SUITS[1])
card3 = PositionableCard("3", Card.SUITS[2])
print("Друкуємо об'єкт Card:")
print(card1)
print("\nДрукуємо об'єкт UnprintableCard:")
print(card2)
print("\nДрукуємо об'єкт PositionableCard:")
print(card3)
print("Перевертаємо карту PositionableCard...")
card3.flip()
print("Друкуємо об'єкт PositionableCard:")
print(card3)



