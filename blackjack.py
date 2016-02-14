# encoding: utf-8
'''
BlackJackクラス
'''

class Blackjack:
    # CARDの種類
    CARD = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    # Aのデフォルトは11、21を超えた場合のみ1に変化する
    CARD_VALUE = {
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

    def __init__(self):
        self.player_cards = {}
        self.player_total = 0
        self.player_ace = 0

        self.dealer_cards = {}
        self.dealer_total = 0
        self.dealer_ace = 0 
