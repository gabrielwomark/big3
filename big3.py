import random
from dataclasses import dataclass, field


RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():
    result = []
    for rank in RANKS:
        for suit in SUITS:
            result.append(Card(rank=rank, suit=suit)
    return result

@dataclass
class State:

@dataclass
class Table:
    Agents: List[Agent]



@dataclass
class Deck:
    cards: List[Card]: field(default_factory=make_french_deck)

    def shuffle(self) -> None:
        random.shuffle(cards)


@dataclass(order=True)
class Card:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str
    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                       + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'


