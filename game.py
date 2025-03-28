from deck import Deck, Card

class Hand:
    def __init__(self, deck):
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    @property
    def is_flush(self):
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def num_matches(self):
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        if self.num_matches == 2:
            return True
        return False

    @property
    def is_2pair(self):
        if self.num_matches == 4:
            return True
        return False

    @property
    def is_trips(self):
        if self.num_matches == 6:
            return True
        return False

    @property
    def is_quads(self):
        if self.num_matches == 12:
            return True
        return False

    @property
    def is_fullhouse(self):
        if self.num_matches == 8:
            return True
        return False

matches = 0
count = 0
while matches < 10000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    count += 1
    if hand.is_quads:
        # print(hand)
        matches += 1
        # break

print(f"The probability of quads is {100*matches/count}%")