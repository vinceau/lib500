"""The game handler
"""
from lib500.fivehundred import FiveHundredDeck
from lib500.cards import Player, Pile

class Game(object):
    def __init__(self):
        self.players = []
        self.started = False
        self.kitty = Pile()

    def add_player(self, name):
        self.players.append(Player(name))

    def start(self):
        no_players = len(self.players)
        if no_players != 4 and no_players != 6:
            print('You don\'t have the right number of people!')
            return
        deck = FiveHundredDeck(no_players == 6)
        for i in [3, 4, 3]:
            for player in self.players:
                player.draw(deck, i)
            self.kitty.add(deck.get_top())

if __name__ == '__main__':
    g = Game()
    for _ in range(1, 5):
        g.add_player('Player %d' % _)
    g.start()
