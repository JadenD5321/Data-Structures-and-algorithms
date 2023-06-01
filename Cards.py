import unittest
from typing import List
import random


class Card:
    """ Represents a playing card with a value and suit. It will eventually return the value and suit of the card. """

    def __init__(self, value: int, suit: str) -> None:
        self.value = value
        self.suit = suit

    def __lt__(self, other: 'Card') -> bool:
        if self.suit == other.suit:
            return self.value < other.value
        return self.suit < other.suit

    def __repr__(self) -> str:
        return f'Card({self.value} of {self.suit})'


class Deck:
    """ Class which represents a deck of playing cards"""
    # it will create a new deck of 52 cards in total. It would then generate a list of card objects that we have implemented within our functions

    def __init__(self):
        self.card_list = []
        for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            for value in range(1, 14):
                self.card_list.append(Card(value, suit))

    def __len__(self):
        """Gets the number of cards in the deck"""
        return len(self.card_list)

    def sort(self):
        self.card_list = sorted(self.card_list)

    def shuffle(self) -> None:
        random.shuffle(self.card_list)

    def draw_top(self) -> Card:
        if len(self.card_list) == 0:
            raise RuntimeError("The deck is empty")
        return self.card_list.pop()

    def __repr__(self):
        return f"Deck({self.card_list})"


class Hand:
    """Create a hand with given cards. """
    # We will have a list of cards in this section.

    def __init__(self, cards: List[Card] = []) -> None:
        self.cards = cards

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def play(self, card):
        if card not in self.cards:
            raise CardNotFound("The card is not in the hand")
        self.cards.remove(card)
        return card

    def sort(self) -> None:
        self.cards.sort()

    def __len__(self) -> int:
        return len(self.cards)

    def __repr__(self) -> str:
        return f"{self.cards}"


class CardNotFound(Exception):
    pass


class TestCard(unittest.TestCase):

    def test_init(self):
        c = Card(5, 'Hearts')
        self.assertEqual(c.value, 5)
        self.assertEqual(c.suit, 'Hearts')

    def __len__(self) -> int:

        return len(self.card_list)


def shuffle(self) -> None:
    """Shuffles the deck in place"""
    random.shuffle(self.card_list)


def draw_top(self) -> Card:
    """Removes and returns the top card from the deck"""
    try:
        return self.card_list.pop()
    except IndexError:
        raise RuntimeError("Unfortunately, you cannot draw an empty deck")


def sort(self) -> None:
    """Sorts the deck in place"""
    self.card_list.sort()


def __repr__(self) -> str:

    return f'Deck({self.card_list})'


def add_card(self, card: Card) -> None:
    """Adds a card to the hand"""
    self.cards.append(card)


def play(self, card: Card) -> Card:
    """Removes a card from the hand and returns it"""
    try:
        self.cards.remove(card)
        return card
    except ValueError:
        raise CardNotFound(f"card is not in the hand")


""" This function returns number of cards in the deck"""


def __len__(self) -> int:

    return len(self.cards)
# Returns a string representation of the deck object.


def __it__(self, other: 'Card') -> bool:
    """Returns True if the card is less than the other card, False otherwise"""
    if self.suit == other.suit:
        return self.value < other.value
    return self.suit < other.suit


def __repr__(self):
    """Returns a string representation of the deck object."""
    return f"Deck({self.cards})"
