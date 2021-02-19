#shuffle() for randomizing the deck
from random import shuffle

#Class for a Card
class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    """ indices 0 and 1 are 'None' so as to keep the ith index == ith value for 2 to Ace """
    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    #Overriding the less than method
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    #Overriding the greater than method
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    #Overriding this method to show the values of this object instance
    def __repr__(self):
        v = self.values[self.value] +\
            " of " + \
            self.suits[self.suit]
        return v

#class for the whole deck of 52 cards
class Deck:
    def __init__(self):
        self.cards = []
        #initializing the cards' list with all the 52 cards
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        #Shuffling the remaining deck of cards
        shuffle(self.cards)

    #removing the top card from the deck
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

#class defining a player
class Player:
    def __init__(self, name):
        #Number of wins of this player
        self.wins = 0
        #Current card which this player is holding
        self.card = None
        self.name = name

#class for the main game
class Game:
    def __init__(self):
        self.name1 = input("p1 name ")
        self.name2 = input("p2 name ")
        self.deck = Deck()
        self.p1 = Player(self.name1)
        self.p2 = Player(self.name2)

    #To print the winner of the current round
    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    #Prints the drawn cards' details 
    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n,
                     p1c,
                     p2n,
                     p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any " + \
                "key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,
                      p1c,
                      p2n,
                      p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1,
                         self.p2)
        print("War is over.{} wins"
              .format(win))

    #Prints the winner of the game, based on the number of wins
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

#Entry point of the project
game = Game()
game.play_game()



