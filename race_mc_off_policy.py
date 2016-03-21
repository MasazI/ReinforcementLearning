# encoding:utf-8
'''
方策OFFモンテカルロ法(カーレース)
'''

from race import START
from race import MAX_SPEED
from race import OUT
from race import IN
from race import GOAL

from course import Course
from race_action_value import RaceActionValue
from race_policy import RacePolicy

import random

from collections import deque

class MCOFFPRace:
    def __init__(self, course, value, policy, epsilon=0.1):
        self.course = course
        self.value = value
        self.policy = policy
        self.epsilon = epsilon

    def simulate(self, start=None, training=True, verbose=False):
        '''
        シュミレーション(方策OFFモンテカルロ学習)
        arguments:
            開始地点(Noneの場合はランダムで選択)
            学習フラグ(Trueの場合は学習する)
            デバッグフラグ(Trueの場合はデバッグ実行)
        '''
        if start is None:
            starts = self.course.starts
            start = random.choice(starts)

        # 状態行動列キュー
        states = deque()
        actions = deque()
        rewards = deque()
        weights = deque()

        # 初期の状態文字列
        state = start
        # 状態リストに追加
        states.append(state)

        # シュミレーション開始
        while(True):
            valid_actions = self.course.get_valid_actions(state)
            select_action = self.policy.get_action(state)

            # 学習の場合はソフト方式で行動を選択
            if training:
                select = random.random()
                for i, action in enumerate(valid_actions):
                    if select < ((self.epsilon / len(valid_actions)) * (i+1)):
                        select_action = action
                        break
            # 選択したアクションを状態行動列に追加
            actions.append(select_action)

            # 状態-行動による次の状態と報酬の取得
            next_state, reward = self.course.step(state, select_action)

            states.append(next_state)
            rewards.append(reward)

            state_list = state.split(",")
            action_list = action.split(",")

            if verbose:
                print("position: (%2s, %2s), speed: (%2s, %2s), action: (%2s, %2s), raward: %2d" % (state_list[0], state_list[1], state_list[2], state_list[3], action_list[0], action_list[1], reward))


            if self.course.is_goal(next_state):
                if verbose:
                    print("total rewards: %f" % (sum(rewards)))
                break
            else:
                state = next_state

        if training:
            # 行動価値を更新
            update_info = deque()
            # 終端を切り捨て
            states.pop()

            state = states.pop()
            action = actions.pop()
            reward_sum = rewards.pop()
            weight = 1.0

            while(True):
                actions_size = len(self.course.get_valid_actions(state))
                # 以下の更新は決定論的方策(行動が方策に対して一意に決定する)が前提の計算
                if action == self.policy.get_action(state):
                    # ポリシーと一致する場合はp=1
                    # 分子はrewards(分子に現れる重みはすべて1なので収益のみになる)
                    # 分母はweights
                    update_info.appendleft([state, action, reward_sum, weight])
                    if not states:
                        # 状態が空になったら終了
                        break
                    else:
                        # 次(今計算した時刻の1つ前)を取得
                        state = states.pop()
                        action = actions.pop()
                        reward_sum += rewards.pop()

                        # グリーディな行動に対する方策改善の重み
                        # グリーディでない行動に対する重みはここでは計算する必要がない(p=0)
                        weight *= 1.0/((1-self.epsilon)+(self.epsilon/actions_size))

                else:
                    # ポリシーと一致しない場合はp=0でそれ以前は計算が不要
                    update_info.appendleft([state, action, reward_sum, weight])
                    break

            # 行動価値を更新
            updated = deque()
            for state, action, reward_sum, weight in update_info:
                # 初回のみ更新
                if not [state, action] in updated:
                    self.value.update(state, action, reward_sum, weight)
                    updated.append([state, action])

            # 方策を更新
            for state, action in updated:
                max_action = self.value.get_max_action(state)
                self.policy.set_action(state, max_action)

