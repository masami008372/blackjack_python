from random import shuffle
import sys

class Card:

    suits = ['♥','♠','◆','♣']

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

class Player():
    def __init__(self, name):
        self.total = 0
        self.name = name
        self.over = False
        
    def match(self):
        if self.total == 21:
            s = '{}\'s total score : {} '
            print(s.format(self.name,self.total))
            w = 'BLACKJACK! {} win.'
            print(w.format(self.name))
            return True
        elif self.total > 21:
            s = '{}\'s total score : {} '
            print(s.format(self.name,self.total))
            l = 'BUST! {} lose.'
            print(l.format(self.name,self.total))
            return True
        else:
            return False
        
        
class Game():
    def __init__(self):
        self.deck = Deck()
        self.p = Player('Player')
        self.d = Player('Dealer')
        
    def draw_msg(self,name,card):
        d = '{} draw {} '
        print(d.format(name,card))

    def score_msg(self,name,score):
        s = '{}\'s total score : {} '
        print(s.format(name,score))

    def hit_stand(self):
        while True:
            hs = input("Hit or Stand(h/s):")
            if hs == "h":
                return True
            elif hs == "s":
                return False
            else:
                continue
                
    def game_continue(self):
        while True:
            yn = input('Continue?(y/n):')
            if yn == "y":
                self.p.total = 0
                self.d.total = 0
                self.play_game()
            elif yn == "n":
                print('Exit game.')
                sys.exit(-1)
            else:
                continue

    def play_game(self):
        
        pc1 = self.deck.draw()
        dc1 = self.deck.draw()
        pc2 = self.deck.draw()
        dc2 = self.deck.draw()
        self.p.total += int(pc1) + int(pc2)
        self.d.total += int(dc1) + int(dc2)

        self.draw_msg(self.p.name, str(pc1))
        self.draw_msg(self.p.name, str(pc2))
        self.draw_msg(self.d.name, str(dc1))
        self.draw_msg(self.d.name, "(Hole Card)")
        
        hs = self.hit_stand()

        while hs:
           pc = self.deck.draw()
           self.p.total += int(pc)
           self.draw_msg(self.p.name, str(pc))
           if self.p.match():
               self.game_continue()
           hs = self.hit_stand()
            
        self.score_msg(self.p.name,self.p.total)
        o = '{}\'s Hole Card : {}'
        print(o.format(self.d.name,str(dc2)))
        
        while self.d.total < 17:
            dc = self.deck.draw()
            self.d.total += int(dc)
            self.draw_msg(self.d.name, str(dc))
            if self.d.match():
                self.game_continue()
                    
        self.score_msg(self.d.name,self.d.total)
                
        if self.d.total < self.p.total:
            print('{} win.'.format(self.p.name))
        elif self.d.total > self.p.total:
            print('{} lose.'.format(self.p.name))
        else:
            print('tie.')
            
        self.game_continue()

            



if __name__ == '__main__':
    game = Game()
    game.play_game()
