#encoding: utf-8
'''
行動価値クラス
'''

import blackjack
from collections import defaultdict
import re

class ActionValue:
    def __init__(self):
        '''
        初期化
        '''
        # 状態価値
        # 構造: Aceを保持[yes, no] - プレイヤーのトータル数 - ディーラーのオープンしているカード - アクション(hit, stand)
        self.value = [defaultdict(lambda: defaultdict(lambda:[ 0.0, 0.0])), defaultdict(lambda: defaultdict(lambda: [0.0, 0.0]))]
        
        # 回数
        # 構造: Aceを保持[yes, no] - プレイヤーのトータル数 - ディーラーのオープンしているカード - アクション(hit, stand)
        self.count = [defaultdict(lambda: defaultdict(lambda:[ 0, 0])), defaultdict(lambda: defaultdict(lambda: [0, 0]))]

        # 出力ヘッダの準備
        self.print_bar = "-------" + "--------------" * 9
        self.print_header = "   |"
        for i in xrange(12, 22, 1):
            self.print_header += "   %02d(h/s)   " % (i)

    def get(self, player_total, player_has_ace, dealer_face_value, player_hit):
        '''
        価値の取得
        '''
        ace_index = 1
        if player_has_ace:
            ace_index = 0

        action_index = 1
        if player_hit:
            action_index = 0
        return self.value[ace_index][player_total][dealer_face_value][action_index]
        
    def update(self, player_total, player_has_ace, dealer_face_value, player_hit, reward):
        '''
        価値の更新
        '''
        ace_index = 1
        if player_has_ace:
            ace_index = 0

        action_index = 1
        if player_hit:
            action_index = 0

        # 回数の更新
        count = self.count[ace_index][player_total][dealer_face_value][action_index]
        count += 1
        self.count[ace_index][player_total][dealer_face_value][action_index] = count

        # 報酬の更新
        value = self.value[ace_index][player_total][dealer_face_value][action_index]
        value += (1.0 / count) * (reward - value)
        self.value[ace_index][player_total][dealer_face_value][action_index] = value

    def output(self):
        print(re.sub('-----', '[ace]', self.print_bar, 1))
        print(self.print_header)
        print(self.print_bar)
        print_format = ""
        for i in xrange(2, 12, 1):
            print_format += "%02d |" % (i)
            for j in xrange(12, 22, 1):
                print_format += " %3.3f/%3.3f " % (self.get(j, True, i, True), self.get(j, True, i, False))
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
                print_format += " %3.3f/%3.3f " % (self.get(j, False, i, True), self.get(j, False, i, False))
            print_format += "\n"
        print(print_format)
        print(self.print_bar)


def test():
    actionValue = ActionValue()
    print actionValue.value
    actionValue.value[1][12][3][0] = -1.023898
    actionValue.count[0][1][2][0] += 1
    actionValue.output()

if __name__ == '__main__':
    test()
