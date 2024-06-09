import collections

# 创建一个和tuple类似的对象Card 拥有rank和suit两个属性
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split(" ")

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    # 该方法是len(obj)的底层
    def __len__(self):
        return len(self._cards)

    # 该方法是 card[xxx]的底层，同时可以使该对象支持切片
    def __getitem__(self, item):
        return self._cards[item]


# 自定义排序规则
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    deck = FrenchDeck()
    print(len(deck))  # 52 实际调用 __len__方法
    # Card(rank='2', suit='spades') 实际调用 __getitem__ 也就是 _cards[0]
    print(deck[0])
    print(random.choice(deck))  # 随机选出一个
    print(deck[:4])  # __getitem__方法的重写使对象支持slicing
    print(deck[12::13])  # 从索引12开始每13张取一张，四种花色的 A
    for card in reversed(deck):  # 同时也支持遍历
        print(card)
    print(Card('4', 'spades') in deck)  # True
    suit_values = dict(spades=3, heart=2, diamonds=1, clubs=0)
    # 根据自定义排序规则遍历
    for card in sorted(deck, key=spades_high):
        print(card)