#encoding: utf-8
'''
q-learningによるAIコム
'''
import random
from mark import Mark
from maru_mark import Maru
from batsu_mark import Batsu
from empty_mark import Empty

from tic_tac_toe_state import State
from tic_tac_toe_value import Value


class QLearningCom:
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
        AIによる行動選択（決定的な行動による学習の後にε-greedyにって行動を選択する）
        '''
        value_max_action = self.value.get_max_action(state, self.mark)
        selected_action = value_max_action

        # 決定的な行動の事後状態で価値を更新
        if self.training:
            after_state = state.set(value_max_action, self.mark)
            if self.previous_reward is not None and self.previous_after_state is not None:
                #print("update previous_reward: %d %d" %(self.previous_reward, self.mark.to_int()))
                #print self.previous_after_state.output()
                #print state.output()
                #print after_state.output()
                #print("-"*20)
                self.value.update(self.previous_after_state, self.previous_reward, after_state) 
            else:
                pass
                #print("have not enough step.")
                #print self.previous_after_state
                #print self.previous_reward

            # 更新の後にソフト方策を使う
            if random.random() < self.epsilon:
                selected_action = random.choice(state.get_valid_actions())

            self.previous_after_state = state.set(selected_action, self.mark)

        return selected_action

    def learn(self, reward, finished=False):
        '''
        学習
        arguments:
            報酬
            終端状態かどうか
        '''
        #print("#"*10)
        if self.training:
            if finished:
                #print("finished")
                #print self.previous_after_state.output()
                self.value.update(self.previous_after_state, reward, None)
                self.previous_reward = None
                self.previous_after_state = None
            else:
                #print("not finished")
                self.previous_reward = reward
            #print("learn reward: %d %d" % (reward, self.mark.to_int()))

