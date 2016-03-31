#encoding: utf-8
'''
Sarsa法によるAIコム
'''
import random
from mark import Mark
from maru_mark import Maru
from batsu_mark import Batsu
from empty_mark import Empty

from tic_tac_toe_state import State
from tic_tac_toe_value import Value

class SarsaCom:
    epsilon = 0.1

    def __init__(self, mark, value, training=True):
        '''
        初期化:
        arguments:
            どちらのマークのPlayerとして行動するか
            行動価値テーブル
        '''
        self.mark = mark
        self.value = value
        self.training = training
        self.previous_reward = None
        self.previous_after_state = None

    def select_index(self, state):
        '''
        AIによる行動選択(ε-greedy)
        arguments:
            状態
        return:
            選択したアクション
        '''
        selected_action = self.value.get_max_action(state, self.mark)

        # 学習時以外は決定論的な方策を利用する
        if self.training:
            if random.random() < self.epsilon:
                selected_action = random.choice(state.get_valid_actions())

        # 選択した行動の事後状態
        after_state = state.set(selected_action, self.mark)
        if self.previous_reward is not None and self.previous_after_state is not None:
            self.value.update(self.previous_after_state, self.previous_reward, after_state)

        # 1つ前の事後状態を保存
        self.previous_after_state = after_state

        # 選択した行動を返す
        return selected_action

    def learn(self, reward, finished=False):
        '''
        学習
        arguments:
            報酬
        '''
        if self.training:
            if finished:
                self.value.update(self.previous_after_state, reward, None)
                self.previous_reward = None
                self.previous_after_state = None
            else:
                self.previous_reward = reward

