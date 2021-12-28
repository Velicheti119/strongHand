import random


class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit


class Deck:
    def __init__(self):
        self.deck = []

    def makeDeck(self):
        for suite in ["Heart", "Spade", "Diamond", "Club"]:
            for num in range(1, 14):
                self.deck.append(Card(num, suite))

    def shuffle(self):
        random.shuffle(self.deck)

    def printDeck(self):
        for card in self.deck:
            print(card)


class Game:
    def __init__(self, deck):
        self.hand = deck[:5]
        #self.hand = [Card(3, "Heart"), Card(3, "Diamond"), Card(3, "Spade"), Card(3, "Club"), Card(8, "Heart")]
        self.strongestHand = "High Card"
        self.cardRanks = []

        for card in self.hand:
            self.cardRanks.append(card.rank)
        self.cardRanks.sort()

    def royalFlush(self):
        expect = [13, 12, 11, 10, 1]
        for card in self.hand:
            if card.rank in expect and card.suit == "Heart":
                pass
            else:
                return False
        self.strongestHand = "Royal Flush"
        return True

    def straightAndFlush(self):
        isStraight = False
        isFlush = False
        for i in range(4):
            if self.hand[i].rank == self.hand[i + 1].rank - 1:
                pass
            elif self.hand[i].rank == 1 and self.hand[i + 1].rank == 10:
                pass
            else:
                break
        else:
            isStraight = True

        suit = self.hand[0].suit
        for card in self.hand:
            if card.suit == suit:
                pass
            else:
                break
        else:
            isFlush = True

        if isFlush and isStraight:
            print("Straight Flush")
            self.strongestHand = "Straight Flush"
            return True
        if isFlush:
            print("Flush")
            self.strongestHand = "Flush"
            return True
        if isStraight:
            print("Straight")
            self.strongestHand = "Straight"
            return True
        return False

    def repeats(self):
        count = {}
        for rank in self.cardRanks:
            if rank in count:
                count[rank] += 1
            else:
                count[rank] = 1

        print(count)
        size = len(count)
        if size == 2:
            for key in count:
                if count[key] == 4 or count[key] == 1:
                    print("Four of a kind")
                    self.strongestHand = "Four of a kind"
                    return True
                elif count[key] == 3 or count[key] == 2:
                    print("Full House")
                    self.strongestHand = "Full House"
                    return True
        elif size == 3:
            for key in count:
                if count[key] == 3:
                    print("Three of a kind")
                    self.strongestHand = "Three of a kind"
                    return True
                elif count[key] == 2:
                    print("Two Pair")
                    self.strongestHand = "Two Pair"
                    return True
        elif size == 4:
            print("One Pair")
            self.strongestHand = "One Pair"
            return True
        return False

    def getStrongestHand(self):
        if self.royalFlush():
            pass
        elif self.straightAndFlush():
            pass
        elif self.repeats():
            pass
        return self.strongestHand


deck = Deck()
deck.makeDeck()
deck.shuffle()

game = Game(deck.deck)
for card in game.hand:
    print(card.rank, card.suit)

print("Strongest Hand:", game.getStrongestHand())
