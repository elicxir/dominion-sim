
import xml.etree.ElementTree as ET
import random

class Game:

    def start():
        pass

    def process():
        pass

    def _if():

        pass


class Field:

    def __init__(self) -> None:
        
        pass


    pass
    

class Player:

    def __init__(self,strategy_file,opener_copper=3) -> None:
        self.strategy=strategy_file
        self.discard=[] # 捨て札の山
        self.hand=[] # 手札
        self.field=[] # 場に出された札
        self.deck=[] # 山札
        self.all_cards=[] 
        self.buy_chance=0
        self.action=0

        for i in range(7):
            self.deck.append("Copper")
        for i in range(3):
            self.deck.append("Estate")

        if opener_copper<2 or opener_copper>5:
            raise

        self.Opener(opener_copper)


    def Opener(self,copper:int):
        for c in range(copper):
            self.deck.remove("Copper")
            self.hand.append("Copper")
        for c in range(5-copper):
            self.deck.remove("Estate")
            self.hand.append("Estate")            

    def play(self,s):
        pass

    def buy(self,s):
        
        pass

    def obtain(self,card):
        self.discard.append(card)
        pass

    def draw(self,num):
        index=0
        while(index<num and len(self.deck)+len(self.discard)>0):
            print(index)
            if len(self.deck)==0:
                print("reshuffle")
                self.reshuffle()
            self.draw_one()
            index+=1
        pass

    def draw_one(self):
        item=self.deck.pop(0)
        self.hand.append(item)

    def reshuffle(self):

        print(self.discard)
        
        while (len(self.discard)>0):
            item=self.discard.pop(0)
            self.deck.append(item)

        random.shuffle(self.deck)
        print(self.deck)

        pass


    def flush(self):

        while (len(self.hand)>0):
            item=self.hand.pop(0)
            self.discard.append(item)

        while (len(self.field)>0):
            item=self.field.pop(0)
            self.discard.append(item)

p=Player("asd",4)

print(p.hand)
p.obtain("Silver")
p.flush()
p.draw(5)
print(p.hand)
p.obtain("Silver")
p.flush()
p.draw(5)
print(p.hand)
p.obtain("Silver")
p.flush()
p.draw(5)
print(p.hand)
p.flush()
p.draw(5)
print(p.hand)