from random import shuffle
import sys

class Card:

    suits = ['♥','♠','♦','♣']

    ranks = [None, "A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, s, r):
        self.suit = s
        self.rank = r

    def __int__(self):
        r = self.ranks[self.rank]
        if r == "J" or r == "Q" or r == "K":
            r = 10
        elif r == "A":
            r = 1
        return int(r)

    def __str__(self):
        v = self.ranks[self.rank] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(1, 14):
            for j in range (4):
                self.cards.append(Card(j, i))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class PlayerBase():
    def __init__(self, name):
        self.total = 0
        self.name = name
        self.deck = Deck()

    def draw_msg(self,card):
        d = '{} draw {}'
        print(d.format(self.name,card))

    def score_msg(self):
        s = '{} \'s total score : {} '
        print(s.format(self.name,self.total))

    def match(self):
        if self.total == 21:
            s = '{} \'s total score : {} '
            print(s.format(self.name,self.total))
            w = 'BLACKJACK! {} win.'
            print(w.format(self.name))
            return True
        elif self.total > 21:
            s = '{} \'s total score : {} '
            print(s.format(self.name,self.total))
            l = 'BUST! {}lose.'
            print(l.format(self.name,self.total))
            return True
        else:
            return False


class User(PlayerBase):

    def first_draw(self):
        pc1 = self.deck.draw()
        pc2 = self.deck.draw()
        self.total += int(pc1) + int(pc2)
        self.draw_msg(str(pc1))
        self.draw_msg(str(pc2))

    def hit_stand(self):
        while True:
            hs = input("Hit or Stand(h/s):")
            if hs == "h":
                pc = self.deck.draw()
                self.total += int(pc)
                self.draw_msg(str(pc))
                return True
            elif hs == "s":
                return False

class Dealer(PlayerBase):

    def first_draw(self):
        dc1 = self.deck.draw()
        dc2 = self.deck.draw()
        self.total += int(dc1) + int(dc2)
        self.draw_msg(str(dc1))
        self.draw_msg("(Hole Card)")
        return str(dc2)

    def auto_draw(self):
        while True:
            if self.total < 17:
                dc = self.deck.draw()
                self.total += int(dc)
                self.draw_msg(str(dc))
                return True
            else:
                return False

class Game():
    def __init__(self):
        self.u = User('Player')
        self.d = Dealer('Dealer')

    def game_continue(self):
        while True:
            yn = input('Continue?(y/n):')
            if yn == "y":
                self.u.total = 0
                self.d.total = 0
                return True
            elif yn == "n":
                print('Exit game.')
                sys.exit(-1)

    def play_game(self):
        while True:
            continue_flg = False

            self.u.first_draw()
            holecard = self.d.first_draw()

            while self.u.hit_stand():
                if self.u.match():
                    continue_flg = self.game_continue()
                    break
            if continue_flg:
                continue

            self.u.score_msg()

            o = '{} \'s Hole Card : {}'
            print(o.format(self.d.name, holecard))

            while self.d.auto_draw():
                if self.d.match():
                    continue_flg = self.game_continue()
                    break
            if continue_flg:
                continue

            self.d.score_msg()

            if self.d.total < self.u.total:
                print('{} win.'.format(self.u.name))
            elif self.d.total > self.u.total:
                print('{} lose.'.format(self.u.name))
            else:
                print('tie')

            if self.game_continue():
                continue



if __name__ == '__main__':
    game = Game()
    game.play_game()
