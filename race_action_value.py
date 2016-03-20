# encoding: utf-8
'''
レースの行動価値
'''
from collections import defaultdict

class RaceActionValue:
    def __init__(self):
        # 状態ごとの各行動の価値を保存
        # [状態][行動]
        self.value = defaultdict(lambda: defaultdict(lambda: 0.0))
        
        # 状態ごとの各行動の合計価値(方策OFFで必要な収益を重み付けした合計)
        self.points = defaultdict(lambda: defaultdict(lambda: 0.0))

        # 状態ごとの各行動の回数(方策ON)または重みの合計(方策OFF)
        self.weights = defaultdict(lambda: defaultdict(lambda: 0.0))
        

    def get(self, state, action):
        '''
        状態文字列と行動を指定して行動価値を取得
        arguments:
            状態文字列
            行動
        return:
            行動価値
        '''
        return self.value[state][action]

    def get_max_action(self, state):
        '''
        最も行動価値の高い行動を取得
        arguments:
            状態文字列
        return:
            指定された状態で最も行動価値の高い行動
        '''
        states = self.value[state]
        max_state_action = max(states)
        return max_state_action

    def update(self, state, action, reward, weight=1.0):
        '''
        価値の更新
        arguments:
            状態
            行動
            報酬
            重み
        '''
        self.points[state][action] += reward * weight
        self.weights[state][action] += weight
        self.value[state][action] = self.points[state][action] / self.weights[state][action]

