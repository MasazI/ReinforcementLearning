#encoding: utf-8
'''
tic tac toeの行動価値クラス
'''
from collections import defaultdict
from tic_tac_toe_state import State

from mark import Mark
from maru_mark import Maru
from batsu_mark import Batsu
from empty_mark import Empty

class Value:
    step_size = 0.1

    def __init__(self):
        '''
        状態ごとに価値を保存
        '''
        self.value = defaultdict(lambda: 0.0)

    def get_value(self, state):
        '''
        状態に対する価値
        arguments:
            状態
        return:
            価値
        '''
        return self.value[state]

    def get_max_action(self, state, mark):
        '''
        状態において最も価値の高い行動を取得する
        arguments:
            状態
            マーク
        return:
            行動
        '''
        # 選択可能な行動
        actions = state.get_valid_actions()

        # 選択可能な行動をとった後の状態価値を取得
        map = {}
        for action in actions:
            after_state = state.set(action, mark)
            map[action] = self.value[after_state]

        # 選択可能な行動をとった後の最大の状態価値を取得
        max_action = max(map.items(), key=lambda x:x[1])[0]
        print map 
        return max_action

    def update(self, state, reward, next_state):
        '''
        行動を行った後の状態stateに対する価値を更新する
        arguments:
            状態
            報酬
            行動を行った後の状態
        '''
        if next_state is None:
            next_state_value = 0.0
        else:
            #状態価値テーブルから価値を取得
            next_state_value = self.value[next_state]
        # 行動価値の更新式
        self.value[state] += self.step_size * (reward + next_state_value - self.value[state])
        print self.value

if __name__ == '__main__':
    value = Value()
    state = State()
    #print value.get_value(state)
    #print value.get_max_action(state, Mark(Maru()))
    new_state = state.set(3, Mark(Maru()))
    new_state1 = state.set(4, Mark(Maru()))
    new_state2 = new_state.set(2, Mark(Batsu())) 
    value.update(state, 10, new_state)
    value.update(new_state, 10, new_state2)
    value.update(new_state, 10, new_state2)
    value.update(new_state1, 10, new_state2)
    value.update(new_state1, 100, new_state2)
    #value.update(state, -3, new_state2)
    print value.get_max_action(state, Mark(Maru()))

