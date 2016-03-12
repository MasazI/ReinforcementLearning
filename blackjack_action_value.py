#encoding: utf-8
'''
行動価値クラス
'''

import blackjack

from collections import defaultdict

class ActionValue:
    def __init__(self):
        # 状態価値
        # 構造: Aceを保持[yes, no] - プレイヤーのトータル数 - ディーラーのオープンしているカード - アクション(hit, stand)
        self.value = [defaultdict(lambda: defaultdict(lambda:[ 0.0, 0.0])), defaultdict(lambda: defaultdict(lambda: [0.0, 0.0]))]
        
        # 回数
        # 構造: Aceを保持[yes, no] - プレイヤーのトータル数 - ディーラーのオープンしているカード - アクション(hit, stand)
        self.count = [defaultdict(lambda: defaultdict(lambda:[ 0, 0])), defaultdict(lambda: defaultdict(lambda: [0, 0]))]

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
        

def test():
    actionValue = ActionValue()
    print actionValue.value
    print actionValue.value[0][1][2][0]
    actionValue.value[0][1][2][0] = 1.0
    print actionValue.value[0][1][2][0]


if __name__ == '__main__':
    test()
