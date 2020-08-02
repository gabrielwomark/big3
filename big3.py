import random
from dataclasses import dataclass, field
from typing import List, Optional, Set


RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck():
    result = []
    for rank in RANKS:
        for suit in SUITS:
            result.append(Card(rank=rank, suit=suit))
    return result


@dataclass(order=True)
class Card:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit))

    def __str__(self) -> str:
        return f'{self.suit}{self.rank}'

    def is_special(self) -> bool:
        return rank in {2, 3, 7, 10}

    def is_lower_rank(self, other) -> bool:
        return self.rank < other.rank

    def is_higher_rank(self, other) -> bool:
        return not self.is_lower_rank(other)


@dataclass
class Agent:
    hand: Set[Card]

    def has_to_pickup(self, top_of_pile: Card) -> bool:
        for card in self.hand:
            if card.is_higher_rank(top_of_pile):
                return False
            elif card.is_special():
                return False
        return True

    def add_to_hand(self, *cards: Card) -> None:
        for card in cards:
            self.hand.add(card)


@dataclass
class Deck:
    cards: List[Card] = field(default_factory=make_french_deck)

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


    def shuffle(self) -> None:
        random.shuffle(cards)

    def draw(self, n: int = 1) -> Set[Card]:
        result = []
        for i in range(n):
            result.append(self.cards.pop(0))
        return set(result)


@dataclass
class State:
    deck: List[Card]
    players: List[Agent]
    whose_move: int  # set(range(num_players))
    pile: List[Card] = field(default_factory=list)

    def clear(self):
        self.pile = []

    def make_move(self, card, current_player: Agent, wants_pickup: bool = False, flash_player: Optional[Agent] = None):
        if not current_player.has_to_pickup():
            if wants_pickup:
                for card in pile:
                    pass


