#encoding: utf-8
'''
方策(Policy)クラス
'''

import blackjack
from collections import defaultdict
import re

class Policy:
    def __init__(self):
        # 方策
        # 構造: Aceを保持[yes, no] - プレイヤーのトータル数 - ディーラーのオープンしているカード - hit(True or False)
        self.policy = [defaultdict(lambda: defaultdict(lambda: True)), defaultdict(lambda: defaultdict(lambda: True))]

        # 出力ヘッダの準備
        self.print_bar = "-------" + "--------------" * 9
        self.print_header = "   |"
        for i in xrange(12, 22, 1):
            self.print_header += "   %02d   " % (i)

    def hit(self, player_total, player_has_ace, dealer_face_value):
        '''
        方策の取得(hitするかどうか)
        arguments:
            プレイヤーのトータル数
            プレイヤーがAceをもっているかどうか
            ディーラーのオープンしているカード
        return:
            方策 True:hit, False:stand
        '''
        ace_index = 1
        if player_has_ace:
            ace_index = 0
        return self.policy[ace_index][player_total][dealer_face_value]

    def set(self, player_total, player_has_ace, dealer_face_value, hit):
        '''
        方策の設定
        arguments:
            プレイヤーのトータル数
            プレイヤーがAceをもっているかどうか
            ディーラーのオープンしているカード
            方策 True:hit, False:stand
        '''
        ace_index = 1
        if player_has_ace:
            ace_index = 0
        self.policy[ace_index][player_total][dealer_face_value] = hit

    def output(self):
        '''
        現状の出力
        '''
        print(re.sub('-----', '[ace]', self.print_bar, 1))
        print(self.print_header)
        print(self.print_bar)
        print_format = ""
        for i in xrange(2, 12, 1):
            print_format += "%02d |" % (i)
            for j in xrange(12, 22, 1):
                action = 'stand'
                if self.hit(j, True, i):
                    action = 'hit'
                print_format += "%06s  " % (action)
            print_format += "\n"
        print(print_format)
        print(self.print_bar)
        
        print(re.sub('-------', '[noace]', self.print_bar, 1))
        print(self.print_header)
        print(self.print_bar)
        print_format = ""
        for i in xrange(2, 12, 1):
            print_format += "%02d |" % (i)
            for j in xrange(12, 22, 1):
                action = 'stand'
                if self.hit(j, False, i):
                    action = 'hit'
                print_format += "%06s  " % (action)
            print_format += "\n"
        print(print_format)
        print(self.print_bar)

        
def test():
    policy = Policy()
    policy.policy[0][12][4] = False
    policy.output()

if __name__ == '__main__':
    test()
