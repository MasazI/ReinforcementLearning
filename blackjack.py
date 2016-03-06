# encoding: utf-8

import random

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
        self.player_cards = []
        self.player_total = 0
        self.player_ace = 0

        self.dealer_cards = []
        self.dealer_total = 0
        self.dealer_ace = 0
        
        self.finish = False

        # プレイヤーの初期化(控除率を上げるため11以下の場合は強制的にヒットしてカードをひく)
        while(self.player_total < 12):
            self.player_draw()

        # ディーラーの初期化(2枚のカードを引く)
        for i in xrange(2):
            self.dealer_draw()

    def draw_card(self):
        '''
        カードをランダムに1枚引く
        '''
        return random.choice(self.CARD)

    def player_draw(self):
        '''
        プレイヤーがカードを1枚引く
        '''
        card = self.draw_card()
        self.player_cards.append(card)
        if card == 'A':
            self.player_ace += 1
        self.player_total += self.CARD_VALUE[card]
        if (self.player_total > 21) & (self.player_ace > 0):
            self.player_total -= 10
            self.player_ace -= 1

    def dealer_draw(self):
        '''
        ディーラーがカードを1枚引く
        '''
        card = self.draw_card()
        self.dealer_cards.append(card)
        if card == 'A':
            self.dealer_ace += 1
        self.dealer_total += self.CARD_VALUE[card]
        if (self.dealer_total > 21) & (self.dealer_ace > 0):
            self.dealer_total -= 10
            self.dealer_ace -= 1

    def dealer_keep_draw(self):
        '''
        ディーラーが17以上になるまでカードを引く
        '''
        while(self.dealer_total < 17):
            self.dealer_draw()

    def player_hit(self):
        '''
        プレイヤーがカードを1回引く
        '''
        self.player_draw()

        # 21を超えた場合修了フラグをたてる
        if self.player_total > 21:
            self.finish = True

    def player_stand(self):
        '''
        プレイヤーがスタンドする(カードを引くのをやめる)
        '''
        if self.finish:
            print("blackjack game hasfinished.")
            return
        self.finish = True
        self.dealer_keep_draw()

    def judgement_result(self):
        '''
        勝負結果の判定
        '''
        if not self.finish:
            print("blackjack plaing")
        win = 0
        if self.player_total > 21:
            win = -1
        elif self.dealer_total > 21:
            win = 1
        elif self.player_total > self.dealer_total:
            win = 1
        elif self.player_total < self.dealer_total:
            win = -1
        else:
            win = 0

        return win

    def output(self):
        '''
        状況もしくは結果の出力
        '''  
        print("--"*30)
        print("Player total %d" % (self.player_total))
        print("Cards: %s" % (self.player_cards))

        if self.finish:
            print("Dealer total %d" % (self.dealer_total))
            print("Cards: %s" % (self.dealer_cards))
        else:
            print("Dealer total ?")
            print("Cards: [%s, ??]" % (self.dealer_cards[0]))
        print("--"*30)
        

def test():
    blackjack = Blackjack() 
    print blackjack.player_cards   
    print blackjack.dealer_cards

if __name__ == '__main__':
    '''
    Blackjack game.
    '''
    game = Blackjack()
    while(True):
        game.output()
        
        print("Choice your action:")
        print("[h] hit")
        print("[s] stand")
        print("[q] quit")

        input_line = raw_input()

        if input_line == 'q':
            print('quit')
            break
        elif input_line == 'h':
            game.player_hit()
        elif input_line == 's':
            game.player_stand()
        else:
            print("invalide action.")
            continue

        if game.finish:
            break

    game.output()
    result = game.judgement_result()
    if result > 0:
        print("You Win!!!")
    elif result < 0:
        print("You Lose...")
    else:
        print("Draw")

